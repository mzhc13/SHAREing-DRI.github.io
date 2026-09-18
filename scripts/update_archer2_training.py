#!/usr/bin/env python3

import csv
import re
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


ARCHER2_URL = "https://www.archer2.ac.uk/training/"
CSV_FILE = Path("_data/external-training.csv")

HEADERS = {
    "User-Agent": "SHAREing External Training Catalogue"
}

ARCHER2_DOMAIN = "https://www.archer2.ac.uk"

FIELDNAMES = [
    "title",
    "organisation",
    "format",
    "tags",
    "dates",
    "location",
    "url",
]


def clean_text(text):
    """Normalise whitespace in scraped text."""
    return re.sub(r"\s+", " ", text).strip()


def infer_format(venue):
    """Convert ARCHER2 venue information into the SHAREing format."""
    if venue.strip().lower() == "online":
        return "Scheduled (online)"

    return "Scheduled (in person)"


def infer_tags(title):
    """
    Infer SHAREing topics from the course title.

    This is deliberately conservative. Existing CSV tags are
    preserved when updating an existing course.
    """
    title_lower = title.lower()

    tag_rules = {
        "Fortran": ["fortran"],
        "C++": ["c++", "cpp"],
        "Python": ["python"],
        "MPI": ["mpi", "message-passing", "message passing"],
        "OpenMP": ["openmp"],
        "GPU": ["gpu"],
        "CUDA": ["cuda"],
        "HIP": ["hip"],
        "Containers": [
            "container",
            "containers",
            "podman",
            "apptainer",
            "singularity",
            "docker",
        ],
        "Performance Engineering": [
            "performance",
            "optimisation",
            "optimization",
            "profiling",
            "benchmarking",
        ],
    }

    tags = []

    for tag, keywords in tag_rules.items():
        if any(keyword in title_lower for keyword in keywords):
            tags.append(tag)

    return ",".join(tags)


def get_archer2_courses():
    """Scrape scheduled courses from the ARCHER2 Upcoming Training table."""

    print(f"Fetching {ARCHER2_URL} ...")

    response = requests.get(
        ARCHER2_URL,
        headers=HEADERS,
        timeout=30,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    upcoming_heading = soup.find(
        lambda tag: tag.name in ["h2", "h3"]
        and "Upcoming Training" in tag.get_text()
    )

    if not upcoming_heading:
        raise RuntimeError(
            "Could not find the ARCHER2 'Upcoming Training' section."
        )

    table = upcoming_heading.find_next("table")

    if not table:
        raise RuntimeError(
            "Could not find the Upcoming Training table."
        )

    courses = []

    rows = table.find_all("tr")

    for row in rows[1:]:
        cells = row.find_all(["td", "th"])

        if len(cells) < 5:
            continue

        title_cell = cells[0]
        venue_cell = cells[2]
        dates_cell = cells[3]

        title_link = title_cell.find("a")

        if not title_link:
            print(
                f"Skipping '{clean_text(title_cell.get_text())}': "
                "no course details link found."
            )
            continue

        title = clean_text(title_cell.get_text())
        venue = clean_text(venue_cell.get_text())
        dates = clean_text(dates_cell.get_text())

        # Exclude ARCHER2's self-service courses.
        if "always open" in dates.lower():
            print(f"Skipping self-service course: {title}")
            continue

        course_url = urljoin(
            ARCHER2_DOMAIN,
            title_link.get("href"),
        )

        courses.append(
            {
                "title": title,
                "organisation": "ARCHER2",
                "format": infer_format(venue),
                "tags": infer_tags(title),
                "dates": dates,
                "location": (
                    "Online"
                    if venue.lower() == "online"
                    else venue
                ),
                "url": course_url,
            }
        )

    return courses


def load_existing_courses():
    """Load the existing SHAREing external training CSV."""

    if not CSV_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {CSV_FILE}"
        )

    with CSV_FILE.open(
        newline="",
        encoding="utf-8",
    ) as f:
        reader = csv.DictReader(f)

        if reader.fieldnames != FIELDNAMES:
            raise ValueError(
                f"Unexpected CSV columns: {reader.fieldnames}"
            )

        return list(reader)


def update_courses(existing_courses, scraped_courses):
    """
    Add new ARCHER2 courses and update existing ARCHER2 courses.

    Course URL is used as the stable identifier.

    Existing tags are preserved for existing courses.
    """

    existing_by_url = {
        (row.get("url") or "").strip().lower(): row
        for row in existing_courses
        if (row.get("organisation") or "").strip().lower()
        == "archer2"
    }

    new_courses = []
    updated_courses = []
    unchanged_courses = []

    fields_to_update = [
        "title",
        "format",
        "dates",
        "location",
    ]

    for course in scraped_courses:
        url_key = course["url"].strip().lower()

        existing = existing_by_url.get(url_key)

        if existing is None:
            new_courses.append(course)

            existing_courses.append(course)

            continue

        changes = {}

        for field in fields_to_update:
            old_value = (existing.get(field) or "").strip()
            new_value = (course.get(field) or "").strip()

            if old_value != new_value:
                changes[field] = {
                    "old": old_value,
                    "new": new_value,
                }

                existing[field] = new_value

        if changes:
            updated_courses.append(
                {
                    "course": existing,
                    "changes": changes,
                }
            )
        else:
            unchanged_courses.append(existing)

    return (
        new_courses,
        updated_courses,
        unchanged_courses,
        existing_courses,
    )


def write_csv(courses):
    """Write the updated catalogue to the CSV file."""

    with CSV_FILE.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as f:
        writer = csv.DictWriter(
            f,
            fieldnames=FIELDNAMES,
            lineterminator="\n",
        )

        writer.writeheader()

        for course in courses:
            writer.writerow(
                {
                    field: course.get(field, "")
                    for field in FIELDNAMES
                }
            )


def print_results(
    new_courses,
    updated_courses,
    unchanged_courses,
):
    """Print a summary of the changes."""

    print()
    print("=" * 60)
    print("ARCHER2 TRAINING CATALOGUE UPDATE")
    print("=" * 60)

    print()
    print(f"New courses:       {len(new_courses)}")
    print(f"Updated courses:   {len(updated_courses)}")
    print(f"Unchanged courses: {len(unchanged_courses)}")

    if new_courses:
        print()
        print("NEW COURSES")
        print("-" * 60)

        for course in new_courses:
            print(f"+ {course['title']}")
            print(f"  Date:     {course['dates']}")
            print(f"  Location: {course['location']}")
            print(f"  Tags:     {course['tags']}")
            print(f"  URL:      {course['url']}")
            print()

    if updated_courses:
        print()
        print("UPDATED COURSES")
        print("-" * 60)

        for item in updated_courses:
            course = item["course"]

            print(f"~ {course['title']}")
            print(f"  URL: {course['url']}")

            for field, change in item["changes"].items():
                print(
                    f"  {field}: "
                    f"'{change['old']}' → '{change['new']}'"
                )

            print()

    if not new_courses and not updated_courses:
        print()
        print("No changes detected.")


def main():
    scraped_courses = get_archer2_courses()

    print(
        f"Found {len(scraped_courses)} scheduled ARCHER2 courses."
    )

    existing_courses = load_existing_courses()

    (
        new_courses,
        updated_courses,
        unchanged_courses,
        updated_catalogue,
    ) = update_courses(
        existing_courses,
        scraped_courses,
    )

    # Only rewrite the CSV if something actually changed.
    if new_courses or updated_courses:
        write_csv(updated_catalogue)
        print()
        print(f"Updated {CSV_FILE}")
    else:
        print()
        print("CSV unchanged.")

    print_results(
        new_courses,
        updated_courses,
        unchanged_courses,
    )


if __name__ == "__main__":
    main()