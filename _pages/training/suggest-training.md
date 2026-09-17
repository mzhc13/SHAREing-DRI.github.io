---
layout: single
title: "Suggest a Training Course"
permalink: /training/suggest-training
---

<style>
.training-form {
  max-width: 800px;
  margin: 2rem auto;
}

.training-form-intro {
  margin-bottom: 2rem;
}

.training-form label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.4rem;
}

.training-form .field {
  margin-bottom: 1.5rem;
}

.training-form input,
.training-form select,
.training-form textarea {
  width: 100%;
  padding: 0.7rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
  box-sizing: border-box;
}

.training-form textarea {
  min-height: 100px;
  resize: vertical;
}

.training-form .help-text {
  display: block;
  margin-top: 0.35rem;
  font-size: 0.9rem;
  color: #666;
}

.training-form .required {
  color: #b906b9;
}

.training-submit {
  background: #b906b9;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
}

.training-submit:hover {
  background: #940594;
}

.training-note {
  margin-top: 2rem;
  padding: 1rem 1.2rem;
  background: #f5f5f5;
  border-left: 4px solid #b906b9;
}
</style>

<div class="training-form">

  <div class="training-form-intro">
    <p>
      Do you know of a training course that could be useful to researchers
      working with HPC and accelerated computing?
    </p>


<p>
  Suggest it for the SHAREing External Training Catalogue using the form
  below. Your suggestion will be submitted to GitHub for review before
  being added to the catalogue.
</p>


  </div>

  <form id="training-suggestion-form">

<div class="field">
  <label for="course-title">
    Course title <span class="required">*</span>
  </label>
  <input
    type="text"
    id="course-title"
    name="title"
    placeholder="e.g. Introduction to CUDA C/C++"
    required
  >
</div>

<div class="field">
  <label for="organisation">
    Organisation <span class="required">*</span>
  </label>
  <input
    type="text"
    id="organisation"
    name="organisation"
    placeholder="e.g. NHR@FAU"
    required
  >
</div>

<div class="field">
  <label for="format">
    Format <span class="required">*</span>
  </label>
  <select id="format" name="format" required>
    <option value="">Please select...</option>
    <option value="Online (self-service)">Online (self-service)</option>
    <option value="Scheduled (online)">Scheduled (online)</option>
    <option value="Scheduled (hybrid)">Scheduled (hybrid)</option>
    <option value="Scheduled (in-person)">Scheduled (in-person)</option>
    <option value="Other">Other</option>
  </select>
</div>

<div class="field">
  <label for="tags">
    Topics / tags <span class="required">*</span>
  </label>
  <input
    type="text"
    id="tags"
    name="tags"
    placeholder="e.g. CUDA, GPU, C/C++"
    required
  >
  <span class="help-text">
    Separate multiple topics with commas.
  </span>
</div>

<div class="field">
  <label for="dates">
    Dates <span class="required">*</span>
  </label>
  <input
    type="text"
    id="dates"
    name="dates"
    placeholder="e.g. 17–18 September 2026 or Rolling basis"
    required
  >
  <span class="help-text">
    For courses without fixed dates, you can use "Rolling basis",
    "Self-paced", etc.
  </span>
</div>

<div class="field">
  <label for="location">
    Location <span class="required">*</span>
  </label>
  <input
    type="text"
    id="location"
    name="location"
    placeholder="e.g. Online or Durham, UK"
    required
  >
</div>

<div class="field">
  <label for="course-url">
    Course URL <span class="required">*</span>
  </label>
  <input
    type="url"
    id="course-url"
    name="url"
    placeholder="https://example.org/course"
    required
  >
  <span class="help-text">
    Please provide a public webpage with information about the course.
  </span>
</div>

<button type="submit" class="training-submit">
  Submit suggestion
</button>
```

  </form>

  <div class="training-note">
    <strong>What happens next?</strong>
    <p>
      Clicking <strong>Submit suggestion</strong> will open a pre-filled
      GitHub issue containing the information you have provided. You will
      then just need to review the information and click
      <strong>Create</strong> on GitHub.
    </p>
  </div>

</div>

<script>
document.getElementById("training-suggestion-form").addEventListener("submit", function(event) {
  event.preventDefault();

  const title = document.getElementById("course-title").value.trim();
  const organisation = document.getElementById("organisation").value.trim();
  const format = document.getElementById("format").value.trim();
  const tags = document.getElementById("tags").value.trim();
  const dates = document.getElementById("dates").value.trim();
  const location = document.getElementById("location").value.trim();
  const url = document.getElementById("course-url").value.trim();

  const issueTitle = `[Training suggestion] ${title}`;

  const issueBody = `## Training course suggestion

### Course information

**Course title:** ${title}

**Organisation:** ${organisation}

**Format:** ${format}

**Topics / tags:** ${tags}

**Dates:** ${dates}

**Location:** ${location}

**Course URL:** ${url}

---

Thank you for suggesting a training course for the SHAREing External Training Catalogue!`;

const githubUrl =
  "https://github.com/mzhc13/SHAREing-DRI.github.io/issues/new" +
  "?title=" + encodeURIComponent(issueTitle) +
  "&body=" + encodeURIComponent(issueBody);


  window.location.href = githubUrl;
});
</script>
