---
layout: splash
permalink: /training/external-training-board
classes: wide
---

<div class="cat" id="cat" markdown="0">
<header class="cat-hero">
<div class="hero-text">
<h1>External Training Catalogue</h1>
<p>Discover external training opportunities in HPC, AI, research software engineering, programming, performance optimisation, and related topics. Add courses to build your own learning pathway, or start from a curated one.</p>
</div>
<ul class="hero-stats" id="hero-stats"></ul>
</header>
<div class="cat-layout" id="cat-layout">
<div class="cat-main">
<div class="cat-toolbar">
<div class="toolbar-row">
<div class="cat-tabs" role="tablist" aria-label="Main view">
<button type="button" id="tab-catalogue" class="cat-tab active" role="tab" aria-selected="true">Catalogue</button>
<button type="button" id="tab-curated" class="cat-tab" role="tab" aria-selected="false" style="display:none;">Curated pathways</button>
<button type="button" id="tab-map" class="cat-tab" role="tab" aria-selected="false">Pathway map</button>
</div>
<button type="button" id="pathway-toggle" class="cat-btn cat-btn-primary" aria-expanded="true" aria-controls="pathway-side">My pathway <span id="pathway-count" class="cat-badge">0</span></button>
</div>
<div id="filter-rows" class="filter-rows">
<input type="search" id="cat-search" class="cat-search" placeholder="Search by course, provider or topic" aria-label="Search by course, provider or topic">
<div id="group-chips" class="chip-row" role="group" aria-label="Filter by training group"></div>
<div id="format-chips" class="chip-row" role="group" aria-label="Filter by format"></div>
</div>
</div>
<section id="view-catalogue" aria-label="Training catalogue">
<div id="board-status" class="board-status" aria-live="polite"></div>
<div id="board"></div>
<div id="board-empty" class="board-empty" style="display:none;">
<p class="empty-title">No courses match your search</p>
<p>Try a shorter term, or clear the filters.</p>
<button type="button" id="clear-filters" class="cat-btn">Clear search and filters</button>
</div>
</section>
<section id="view-curated" aria-label="Curated pathways" hidden>
<p class="view-intro">Ready-made routes designed by the SHAREing team. Load one into your pathway, then reorder it or add optional extras.</p>
<div id="curated-grid" class="cur-grid"></div>
</section>
<section id="view-map" aria-label="Pathway map" hidden>
<div class="map-bar">
<div class="map-zoom">
<button type="button" id="pathway-zoom-out" class="cat-btn cat-btn-icon" aria-label="Zoom out">−</button>
<span id="pathway-zoom-indicator">100%</span>
<button type="button" id="pathway-zoom-in" class="cat-btn cat-btn-icon" aria-label="Zoom in">+</button>
<button type="button" id="pathway-reset-view" class="cat-btn">Fit to view</button>
<button type="button" id="auto-arrange" class="cat-btn" title="Put all courses back in a single row">Auto-arrange</button>
</div>
<div class="map-legend">
<span><svg width="36" height="10" aria-hidden="true"><line x1="1" y1="5" x2="35" y2="5" stroke="#940594" stroke-width="2.5" stroke-linecap="round"/></svg>Required</span>
<span><svg width="36" height="10" aria-hidden="true"><line x1="1" y1="5" x2="35" y2="5" stroke="#940594" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="7 5"/></svg>Optional</span>
</div>
</div>
<p class="map-hint">Drag cards to arrange them. Drag from a card's dots to connect two courses. Click a connector to make it optional, and click again to remove it.</p>
<div id="pathway-map" class="pathway-map"></div>
</section>
</div>
<aside id="pathway-side" class="pathway-side" aria-label="My learning pathway">
<div class="side-head">
<h2>My learning pathway</h2>
<div class="side-head-actions">
<button type="button" id="undo-pathway" class="cat-btn cat-btn-small" disabled title="Undo the most recent change (Ctrl/⌘ + Z)">Undo</button>
<button type="button" id="close-side" class="cat-btn cat-btn-small side-close" aria-label="Close pathway">Close</button>
</div>
</div>
<div id="pathway-empty" class="pathway-empty">
<p class="empty-title">Your pathway is empty</p>
<p>Press <strong>+</strong> next to a course to add it here.</p>
<button type="button" id="empty-browse-curated" class="cat-btn" style="display:none;">Browse curated pathways</button>
</div>
<div id="pathway-content" hidden>
<p class="side-summary"><strong id="pathway-summary-count">0 courses</strong>Drag to reorder, or use the arrows.</p>
<div id="pathway-list" class="pathway-list"></div>
<div class="side-actions">
<button type="button" id="download-list" class="cat-btn cat-btn-primary">Download pathway</button>
<button type="button" id="download-map" class="cat-btn">Download map</button>
<button type="button" id="clear-pathway" class="cat-btn cat-btn-danger">Clear</button>
</div>
</div>
</aside>
</div>
<button type="button" id="pathway-fab" class="pathway-fab" aria-controls="pathway-side">My pathway <span id="pathway-fab-count" class="cat-badge">0</span></button>
<div id="toast" class="toast" role="status" aria-live="polite"></div>
<p class="cat-disclaimer"><strong>Disclaimer:</strong> This page is a signposting resource created by the SHAREing project. SHAREing support has been used to curate, organise, and present publicly available training opportunities in a searchable format. The courses listed here are provided by third-party organisations and are not funded, delivered, or maintained by SHAREing unless explicitly stated. Course content, availability, schedules, and registration are the responsibility of the individual providers.</p>
</div>

<style>
/* Everything is sized in px on purpose: Minimal Mistakes scales the root
   font size (16px up to 22px), which made rem-based UI look oversized. */
.cat {
    --brand: #940594; --brand-dark: #6f046f; --deep: #421456;
    --tint: #f7eef7; --tint-2: #efdcef;
    --ink: #1f2937; --mut: #5b6472; --line: #e5e7eb; --soft: #f3f4f6;
    font-size: 15px; line-height: 1.5; color: var(--ink);
    margin: 0 0 32px;
    text-align: left;
}
.cat, .cat * { box-sizing: border-box; }
.cat h1, .cat h2, .cat h3, .cat h4, .cat p, .cat ul, .cat ol, .cat li, .cat summary {
    margin: 0; padding: 0; border: 0; font-family: inherit; text-indent: 0; text-transform: none; letter-spacing: normal;
}
.cat ul, .cat ol { list-style: none; }
.cat p { font-size: 15px; line-height: 1.5; }
.cat button { font-family: inherit; }
.cat a { text-decoration: none; }
.cat [hidden] { display: none !important; }
.cat :focus-visible { outline: 2px solid var(--brand); outline-offset: 2px; }

/* ---------- Hero ---------- */
.cat .cat-hero {
    display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap;
    margin: 24px 0 20px; padding: 28px 32px;
    border-radius: 14px; background: var(--deep); color: #fff;
}
.cat .hero-text { flex: 1 1 420px; max-width: 720px; }
.cat .cat-hero h1 { font-size: 30px; line-height: 1.2; font-weight: 700; color: #fff; margin-bottom: 8px; }
.cat .cat-hero p { color: #e6d3ee; font-size: 16px; }
.cat .hero-stats { display: flex; gap: 32px; }
.cat .hero-stats li { text-align: left; }
.cat .hero-stats strong { display: block; font-size: 30px; line-height: 1.1; font-weight: 700; color: #fff; }
.cat .hero-stats span { font-size: 13px; color: #d9c0e6; }

/* ---------- Buttons ---------- */
.cat .cat-btn {
    display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    height: 38px; padding: 0 14px;
    border: 1px solid #cfd4dc; border-radius: 8px; background: #fff; color: var(--ink);
    font-size: 14px; font-weight: 600; line-height: 1; white-space: nowrap; cursor: pointer;
    transition: background .15s, border-color .15s, color .15s;
}
.cat .cat-btn:hover:not(:disabled) { border-color: var(--brand); background: var(--tint); }
.cat .cat-btn:disabled { opacity: .45; cursor: default; }
.cat .cat-btn-primary { background: var(--brand); border-color: var(--brand); color: #fff; }
.cat .cat-btn-primary:hover:not(:disabled) { background: var(--brand-dark); border-color: var(--brand-dark); }
.cat .cat-btn-danger { color: #b42318; }
.cat .cat-btn-danger:hover:not(:disabled) { border-color: #f04438; background: #fef3f2; }
.cat .cat-btn-small { height: 32px; padding: 0 12px; font-size: 13px; }
.cat .cat-btn-icon { width: 38px; padding: 0; font-size: 18px; }
.cat .cat-badge {
    display: inline-flex; align-items: center; justify-content: center;
    min-width: 22px; height: 22px; padding: 0 6px; border-radius: 11px;
    background: #fff; color: var(--brand); font-size: 12px; font-weight: 700;
}

/* ---------- Layout ---------- */
.cat .cat-layout { display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 28px; align-items: start; }
.cat .cat-layout.side-hidden { grid-template-columns: minmax(0, 1fr); }
.cat .cat-layout.side-hidden .pathway-side { display: none; }
.cat .cat-main { min-width: 0; }

/* ---------- Toolbar ---------- */
.cat .cat-toolbar { position: sticky; top: 0; z-index: 20; padding: 0.5rem; background: #fff; border-bottom: 1px solid var(--line); border-radius: 8px;}
.cat .toolbar-row { display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
.cat .cat-tabs { display: flex; gap: 4px; overflow-x: auto; }
.cat .cat-tab {
    padding: 10px 14px; border: 0; border-bottom: 3px solid transparent; background: none;
    color: var(--mut); font-size: 15px; font-weight: 600; white-space: nowrap; cursor: pointer;
}
.cat .cat-tab:hover { color: var(--brand); }
.cat .cat-tab.active { color: var(--brand); border-bottom-color: var(--brand); }
.cat .filter-rows { padding: 12px 0 12px; }
.cat .cat-search {
    display: block; width: 100%; height: 42px; margin: 0 0 10px; padding: 0 14px;
    border: 1px solid #cfd4dc; border-radius: 8px; background: #fff; color: var(--ink);
    font-size: 15px; box-shadow: none;
}
.cat .cat-search:focus { outline: none; border-color: var(--brand); box-shadow: 0 0 0 3px rgba(148,5,148,.15); }
.cat .chip-row { display: flex; gap: 6px; margin-top: 6px; overflow-x: auto; padding-bottom: 2px; scrollbar-width: thin; }
.cat .chip-row:empty { display: none; }
.cat .chip {
    flex: 0 0 auto; display: inline-flex; align-items: center; gap: 6px; height: 30px; padding: 0 12px;
    border: 1px solid var(--line); border-radius: 15px; background: #fff; color: var(--ink);
    font-size: 13px; font-weight: 600; cursor: pointer; transition: background .15s, border-color .15s;
}
.cat .chip:hover { border-color: var(--brand); }
.cat .chip.active { background: var(--brand); border-color: var(--brand); color: #fff; }
.cat .chip-n { font-weight: 500; opacity: .75; }

/* ---------- Catalogue ---------- */
.cat .board-status { margin: 16px 0 4px; color: var(--mut); font-size: 14px; min-height: 21px; }
.cat .group-section { margin-top: 28px; }
.cat .group-head { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 2px solid var(--tint-2); }
.cat .group-icon { display: flex; align-items: center; justify-content: center; width: 38px; height: 38px; border-radius: 10px; background: var(--tint); font-size: 20px; }
.cat .group-head h2 { font-size: 21px; line-height: 1.2; font-weight: 700; color: var(--deep); }
.cat .group-head small { display: block; color: var(--mut); font-size: 13px; }
.cat .topic { margin-bottom: 22px; }
.cat .topic-head { display: flex; align-items: baseline; gap: 8px; margin-bottom: 8px; }
.cat .topic-head h3 { font-size: 16px; line-height: 1.3; font-weight: 700; color: var(--ink); }
.cat .topic-count { color: var(--mut); font-size: 13px; }
.cat .rows { border: 1px solid var(--line); border-radius: 10px; background: #fff; overflow: hidden; }
.cat .row {
    display: grid; grid-template-columns: minmax(0, 1fr) 200px 36px; gap: 6px 16px; align-items: center;
    padding: 12px 14px; border-top: 1px solid #eef0f3; transition: background .15s;
}
.cat .row:first-child { border-top: 0; }
.cat .row:hover { background: #fafafb; }
.cat .row.in-pathway { background: var(--tint); }
.cat .row-title { display: block; color: var(--ink); font-size: 15px; font-weight: 600; line-height: 1.35; overflow-wrap: anywhere; }
.cat a.row-title:hover { color: var(--brand); text-decoration: underline; }
.cat .row-sub { margin-top: 2px; color: var(--mut); font-size: 13px; }
.cat .row-when { display: flex; flex-direction: column; align-items: flex-start; gap: 4px; font-size: 13px; color: var(--mut); }
.cat .badge { display: inline-block; padding: 2px 9px; border-radius: 10px; font-size: 12px; font-weight: 600; line-height: 1.5; }
.cat .b-demand { background: #e6f4ef; color: #0b6b4d; }
.cat .b-online { background: #e8f0fe; color: #1d4ed8; }
.cat .b-person { background: #fdf0e0; color: #9a5b00; }
.cat .b-other  { background: var(--soft); color: #4b5563; }
.cat .add-btn {
    width: 34px; height: 34px; padding: 0; border: 1.5px solid var(--brand); border-radius: 50%;
    background: #fff; color: var(--brand); font-size: 20px; font-weight: 600; line-height: 1; cursor: pointer;
    transition: background .15s, color .15s, transform .1s;
}
.cat .add-btn:hover { background: var(--tint-2); }
.cat .add-btn:active { transform: scale(.93); }
.cat .row.in-pathway .add-btn { background: var(--brand); color: #fff; }
.cat .more-btn {
    display: block; width: 100%; padding: 10px; border: 0; border-top: 1px solid #eef0f3;
    background: #fafafb; color: var(--brand); font-size: 14px; font-weight: 600; cursor: pointer;
}
.cat .more-btn:hover { background: var(--tint); }
.cat mark { padding: 0 1px; border-radius: 2px; background: #f6d5f6; color: inherit; }
.cat .board-empty { padding: 56px 16px; text-align: center; color: var(--mut); }
.cat .empty-title { margin-bottom: 4px; color: var(--ink); font-size: 16px; font-weight: 700; }
.cat .board-empty .cat-btn { margin-top: 14px; }

/* ---------- Curated pathways ---------- */
.cat .view-intro { margin: 18px 0 16px; color: var(--mut); }
.cat .cur-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; align-items: start; }
.cat .cur-card { display: flex; flex-direction: column; gap: 10px; padding: 18px; border: 1px solid var(--line); border-radius: 12px; background: #fff; }
.cat .cur-card.is-loaded { border-color: var(--brand); background: var(--tint); }
.cat .cur-head { display: flex; align-items: flex-start; gap: 12px; }
.cat .cur-icon { display: flex; flex: 0 0 40px; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 10px; background: var(--tint); font-size: 20px; }
.cat .cur-title { font-size: 17px; line-height: 1.3; font-weight: 700; color: var(--deep); }
.cat .cur-audience { margin-top: 2px; color: var(--mut); font-size: 13px; }
.cat .cur-desc { color: var(--ink); font-size: 14px; }
.cat .cur-stats { color: var(--mut); font-size: 13px; }
.cat .cur-stats .partial { color: #b45309; }
.cat .cur-loaded { display: none; color: var(--brand); font-weight: 700; }
.cat .cur-card.is-loaded .cur-loaded { display: inline; }
.cat .cur-actions { display: flex; flex-wrap: wrap; gap: 8px; }
.cat .cur-route summary { cursor: pointer; color: var(--brand); font-size: 14px; font-weight: 600; }
.cat .cur-steps { margin-top: 12px; }
.cat .cur-step { position: relative; padding: 0 0 14px 34px; }
.cat .cur-step::before { content: ""; position: absolute; left: 11px; top: 26px; bottom: 0; border-left: 2px solid var(--tint-2); }
.cat .cur-step:last-child { padding-bottom: 0; }
.cat .cur-step:last-child::before { display: none; }
.cat .step-dot { position: absolute; left: 0; top: 0; display: flex; align-items: center; justify-content: center; width: 24px; height: 24px; border: 2px solid var(--brand); border-radius: 50%; background: #fff; color: var(--brand); font-size: 12px; font-weight: 700; }
.cat .cur-step.in-pathway .step-dot { background: var(--brand); color: #fff; }
.cat .step-title { display: block; color: var(--ink); font-size: 14px; font-weight: 600; line-height: 1.35; }
.cat a.step-title:hover { color: var(--brand); text-decoration: underline; }
.cat .step-sub { color: var(--mut); font-size: 13px; }
.cat .step-note { margin-top: 2px; color: #475569; font-size: 13px; font-style: italic; }
.cat .step-optional { margin-top: 8px; padding: 8px 10px; border: 1px dashed #c58bc5; border-radius: 8px; background: #fdf9fd; }
.cat .step-optional-label { color: var(--mut); font-size: 12px; font-weight: 600; }
.cat .mini-btn { height: 26px; padding: 0 9px; border: 1px solid #cfd4dc; border-radius: 6px; background: #fff; color: #374151; font-size: 12px; font-weight: 600; cursor: pointer; }
.cat .mini-btn:hover:not(:disabled) { border-color: var(--brand); color: var(--brand); }
.cat .mini-btn:disabled { opacity: .35; cursor: default; }
.cat .mini-btn.added { background: var(--brand); border-color: var(--brand); color: #fff; }
.cat .step-optional .mini-btn { margin-top: 6px; }

/* ---------- Sidebar ---------- */
.cat .pathway-side {
    position: sticky; top: 16px; max-height: calc(100vh - 32px); overflow-y: auto;
    padding: 18px; border: 1px solid var(--line); border-radius: 12px; background: #fff;
    box-shadow: 0 2px 12px rgba(31,41,55,.06);
}
.cat .side-head { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
.cat .side-head h2 { font-size: 17px; line-height: 1.3; font-weight: 700; color: var(--deep); }
.cat .side-head-actions { display: flex; gap: 6px; }
.cat .side-close { display: none; }
.cat .pathway-empty { margin-top: 14px; padding: 22px 16px; border: 1px dashed #cfd4dc; border-radius: 10px; text-align: center; color: var(--mut); }
.cat .pathway-empty .cat-btn { margin-top: 12px; }
.cat .side-summary { margin: 14px 0 10px; color: var(--mut); font-size: 13px; }
.cat .side-summary strong { display: block; color: var(--ink); font-size: 15px; }
.cat .pathway-list { display: flex; flex-direction: column; gap: 8px; }
.cat .pathway-item { display: flex; gap: 10px; padding: 10px; border: 1px solid var(--line); border-radius: 8px; background: #fff; cursor: grab; }
.cat .pathway-item:hover { border-color: #c58bc5; }
.cat .pathway-item.dragging { opacity: .4; }
.cat .pathway-item.drag-over { border-color: var(--brand); box-shadow: 0 0 0 3px rgba(148,5,148,.12); }
.cat .pathway-number { flex: 0 0 26px; display: flex; align-items: center; justify-content: center; width: 26px; height: 26px; border-radius: 50%; background: var(--tint-2); color: var(--brand); font-size: 13px; font-weight: 700; }
.cat .pathway-item-body { flex: 1; min-width: 0; }
.cat .pathway-item-title { display: block; color: var(--ink); font-size: 14px; font-weight: 600; line-height: 1.35; overflow-wrap: anywhere; }
.cat a.pathway-item-title:hover { color: var(--brand); text-decoration: underline; }
.cat .pathway-item-sub { color: var(--mut); font-size: 12px; }
.cat .pathway-item-note { margin-top: 2px; color: #475569; font-size: 12px; font-style: italic; }
.cat .pathway-item-actions { display: flex; gap: 4px; margin-top: 8px; }
.cat .mini-btn.remove { margin-left: auto; color: #b42318; }
.cat .mini-btn.remove:hover { border-color: #fda29b; background: #fef3f2; color: #b42318; }
.cat .side-actions { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 16px; padding-top: 14px; border-top: 1px solid var(--line); }
.cat .side-actions .cat-btn { flex: 1 1 auto; }

/* ---------- Pathway map ---------- */
.cat .map-bar { display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin-top: 16px; }
.cat .map-zoom { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.cat .map-legend { display: flex; gap: 16px; color: var(--mut); font-size: 13px; }
.cat .map-legend span { display: inline-flex; align-items: center; gap: 8px; }
.cat #pathway-zoom-indicator { min-width: 44px; text-align: center; color: var(--mut); font-size: 13px; font-weight: 600; }
.cat .map-hint { margin: 10px 0; color: var(--mut); font-size: 14px; }
.cat .pathway-map {
    position: relative; width: 100%; height: 68vh; min-height: 460px; overflow: hidden;
    border: 1px solid var(--line); border-radius: 12px; background-color: #f8f9fb;
    background-image: radial-gradient(#cfd4dc 0.8px, transparent 0.8px); background-size: 22px 22px;
}
.cat .pathway-viewport { position: absolute; inset: 0; overflow: hidden; cursor: grab; touch-action: none; user-select: none; -webkit-user-select: none; }
.cat .pathway-viewport.is-panning { cursor: grabbing; }
.cat .pathway-world { position: absolute; left: 0; top: 0; width: 0; height: 0; transform-origin: 0 0; }
.cat .pathway-svg { position: absolute; left: -8000px; top: -8000px; width: 16000px; height: 16000px; overflow: visible; pointer-events: none; z-index: 1; }
.cat .pathway-nodes { position: absolute; left: 0; top: 0; width: 0; height: 0; z-index: 2; pointer-events: none; }
.cat .pathway-line { fill: none; stroke: var(--brand); stroke-width: 2.5; opacity: .7; pointer-events: none; }
.cat .pathway-line-dashed { stroke-dasharray: 8 6; }
.cat .pathway-line-hit { fill: none; stroke: transparent; stroke-width: 24px; pointer-events: stroke; cursor: pointer; }
.cat .pathway-line-hit:hover + .pathway-line { stroke-width: 4; opacity: 1; }
.cat .pathway-temp-line { fill: none; stroke: var(--brand); stroke-width: 2; stroke-dasharray: 6 5; opacity: .55; pointer-events: none; }
.cat .pathway-node { position: absolute; width: 230px; min-height: 110px; padding: 14px; border: 1px solid #d8dee6; border-radius: 12px; background: #fff; box-shadow: 0 3px 10px rgba(31,41,55,.08); cursor: grab; user-select: none; touch-action: none; pointer-events: auto; }
.cat .pathway-node:hover { border-color: var(--brand); }
.cat .pathway-node.dragging { cursor: grabbing; z-index: 100; box-shadow: 0 12px 25px rgba(31,41,55,.18); }
.cat .pathway-node-title { margin-right: 24px; color: var(--ink); font-size: 14px; font-weight: 600; line-height: 1.35; }
.cat .pathway-node-title a { color: inherit; }
.cat .pathway-node-title a:hover { color: var(--brand); text-decoration: underline; }
.cat .pathway-node-org { margin-top: 6px; color: var(--brand); font-size: 12px; font-weight: 600; }
.cat .pathway-node-meta { margin-top: 6px; color: var(--mut); font-size: 12px; line-height: 1.4; }
.cat .pathway-node-remove { position: absolute; top: 8px; right: 8px; width: 24px; height: 24px; padding: 0; border: 0; border-radius: 50%; background: #f1f5f9; color: var(--mut); font-size: 16px; cursor: pointer; }
.cat .pathway-node-remove:hover { background: #fee4e2; color: #b42318; }
.cat .pathway-handle { position: absolute; width: 12px; height: 12px; border: 2px solid var(--brand); border-radius: 50%; background: #fff; cursor: crosshair; z-index: 10; }
.cat .pathway-handle:hover { background: var(--brand); }
.cat .pathway-handle.top { top: -6px; left: calc(50% - 6px); }
.cat .pathway-handle.right { top: calc(50% - 6px); right: -6px; }
.cat .pathway-handle.bottom { bottom: -6px; left: calc(50% - 6px); }
.cat .pathway-handle.left { top: calc(50% - 6px); left: -6px; }
.cat .map-empty { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; padding: 16px; text-align: center; color: var(--mut); }

/* ---------- Misc ---------- */
.cat .toast { position: fixed; left: 50%; bottom: 20px; z-index: 1000000; max-width: 90vw; padding: 10px 16px; border-radius: 8px; background: #1f2937; color: #fff; font-size: 14px; opacity: 0; transform: translate(-50%, 10px); pointer-events: none; transition: opacity .2s, transform .2s; }
.cat .toast.show { opacity: 1; transform: translate(-50%, 0); }
.cat .pathway-fab { display: none; }
.cat .cat-disclaimer { margin-top: 40px; padding: 14px 16px; border-left: 4px solid var(--deep); border-radius: 6px; background: #f8f9fb; color: var(--mut); font-size: 13px; line-height: 1.55; }
.cat .cat-disclaimer strong { color: var(--ink); }

@media (prefers-reduced-motion: reduce) { .cat * { transition: none !important; } }

/* ---------- Responsive ---------- */
@media (max-width: 1000px) {
    .cat .cat-layout, .cat .cat-layout.side-hidden { grid-template-columns: minmax(0, 1fr); }
    .cat #pathway-toggle { display: none; }
    .cat .cat-layout.side-hidden .pathway-side { display: block; }
    .cat .pathway-side {
        position: fixed; z-index: 999; left: 0; right: 0; bottom: 0; top: auto; max-height: 80vh;
        border-radius: 16px 16px 0 0; box-shadow: 0 -10px 40px rgba(31,41,55,.25);
        transform: translateY(105%); visibility: hidden; transition: transform .25s ease, visibility .25s;
    }
    .cat .pathway-side.open { transform: translateY(0); visibility: visible; }
    .cat .side-close { display: inline-flex; }
    .cat .pathway-fab {
        position: fixed; z-index: 998; right: 16px; bottom: 16px; display: inline-flex; align-items: center; gap: 8px;
        height: 46px; padding: 0 18px; border: 0; border-radius: 23px; background: var(--brand); color: #fff;
        font-size: 15px; font-weight: 700; box-shadow: 0 6px 20px rgba(148,5,148,.4); cursor: pointer;
    }
    .cat .pathway-fab.hide { display: none; }
}
@media (max-width: 720px) {
    .cat .cat-hero { padding: 22px 20px; }
    .cat .cat-hero h1 { font-size: 25px; }
    .cat .hero-stats { gap: 24px; }
    .cat .row { grid-template-columns: minmax(0, 1fr) 36px; }
    .cat .row-when { grid-column: 1; grid-row: 2; flex-direction: row; flex-wrap: wrap; align-items: center; gap: 4px 10px; }
    .cat .row .add-btn { grid-column: 2; grid-row: 1 / span 2; align-self: start; }
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function () {
"use strict";

/* ============================================================
   DATA  (Jekyll _data files)
   - external-training.csv : courses (title, organisation, format, tags, dates, location, url)
   - training-topics.yml   : groups -> topics
   - training-pathways.yml : curated pathways (optional)
   ============================================================ */

const allCourses      = {{ site.data["external-training"] | jsonify }} || [];
const trainingTopics  = {{ site.data["training-topics"]   | jsonify }} || {};
const curatedPathways = {{ site.data["training-pathways"] | jsonify }} || [];

const today = new Date();
today.setHours(0, 0, 0, 0);

const MONTHS = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"];
const MONTH_RE = /\b(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\b/gi;

/* Last day of a free-text date ("12-14 March 2026"). null = keep the course. */
function parseEndDate(text) {

    const dates = String(text || "").trim();

    if (!dates || /self[- ]?paced|rolling|on[- ]?demand/i.test(dates)) { return null; }

    const years = dates.match(/\b20\d{2}\b/g);
    if (!years) { return null; }

    const year = parseInt(years[years.length - 1], 10);

    let last = null, match;
    MONTH_RE.lastIndex = 0;
    while ((match = MONTH_RE.exec(dates)) !== null) { last = match; }
    if (!last) { return null; }

    const month  = MONTHS.indexOf(last[1].slice(0, 3).toLowerCase());
    const before = dates.slice(0, last.index);
    const after  = dates.slice(last.index + last[0].length);

    let day = null;
    const b = before.match(/\b(\d{1,2})(?:st|nd|rd|th)?\s*(?:of\s+)?$/i);

    if (b) { day = parseInt(b[1], 10); }
    else {
        const a = after.match(/^\s*(\d{1,2})(?!\d)(?:\s*(?:-|–|—|to|&|,|and)\s*(\d{1,2})(?!\d))*/i);
        if (a) { day = parseInt(a[2] || a[1], 10); }
    }

    return day ? new Date(year, month, day) : new Date(year, month + 1, 0);

}

/* Trim stray whitespace from the CSV, then drop finished courses */
const courses = allCourses
    .map(c => {
        const clean = {};
        Object.keys(c).forEach(k => { clean[k] = typeof c[k] === "string" ? c[k].trim() : c[k]; });
        return clean;
    })
    .filter(course => {
        const end = parseEndDate(course.dates);
        return !end || end >= today;
    });

const topicGroups = {};

Object.entries(trainingTopics).forEach(([groupName, topics]) => {
    const parts = groupName.trim().split(/\s+/);
    const icon  = parts.length > 1 ? parts.pop() : "📚";
    topicGroups[parts.join(" ")] = { icon: icon, topics: Array.isArray(topics) ? topics : [] };
});


/* ============================================================
   ELEMENTS
   ============================================================ */

const $ = id => document.getElementById(id);

const layout        = $("cat-layout");
const board         = $("board");
const boardStatus   = $("board-status");
const boardEmpty    = $("board-empty");
const searchInput   = $("cat-search");
const groupChips    = $("group-chips");
const formatChips   = $("format-chips");
const filterRows    = $("filter-rows");
const side          = $("pathway-side");
const sideToggle    = $("pathway-toggle");
const fab           = $("pathway-fab");
const pathwayList   = $("pathway-list");
const pathwayEmpty  = $("pathway-empty");
const pathwayContent = $("pathway-content");
const undoButton    = $("undo-pathway");
const curatedGrid   = $("curated-grid");
const mapHost       = $("pathway-map");
const zoomIndicator = $("pathway-zoom-indicator");
const toastEl       = $("toast");

const TABS = {
    catalogue: { tab: $("tab-catalogue"), view: $("view-catalogue") },
    curated:   { tab: $("tab-curated"),   view: $("view-curated") },
    map:       { tab: $("tab-map"),       view: $("view-map") }
};

const isMobile = () => window.matchMedia("(max-width: 1000px)").matches;


/* ============================================================
   STORAGE
   ============================================================ */

const KEYS = {
    pathway: "shareing-training-pathway",
    layout:  "shareing-training-pathway-layout",
    tab:     "shareing-training-tab",
    side:    "shareing-training-side"
};

function readStorage(key) { try { return localStorage.getItem(key); } catch (e) { return null; } }
function writeStorage(key, value) { try { localStorage.setItem(key, value); } catch (e) { /* ignore */ } }
function readJSON(key, fallback) {
    try { const raw = readStorage(key); return raw ? JSON.parse(raw) : fallback; }
    catch (e) { return fallback; }
}

/* "solid" = required, "dashed" = optional. Old layouts used type:"spinoff" for optional. */
function connectionStyle(c) {
    if (c.style === "solid" || c.style === "dashed") { return c.style; }
    return c.type === "spinoff" ? "dashed" : "solid";
}

function normaliseLayout(value) {
    const l = value && typeof value === "object" ? value : {};
    const connections = Array.isArray(l.connections) ? l.connections : [];
    connections.forEach(c => { c.style = connectionStyle(c); });
    return {
        positions:   l.positions && typeof l.positions === "object" ? l.positions : {},
        connections: connections,
        notes:       l.notes && typeof l.notes === "object" ? l.notes : {}
    };
}

let pathwayIds = readJSON(KEYS.pathway, []);
if (!Array.isArray(pathwayIds)) { pathwayIds = []; }
let pathwayLayout = normaliseLayout(readJSON(KEYS.layout, null));

let draggedPathwayId = null;

function savePathway() {
    writeStorage(KEYS.pathway, JSON.stringify(pathwayIds));
    writeStorage(KEYS.layout, JSON.stringify(pathwayLayout));
}

let toastTimer = null;
function toast(message) {
    toastEl.textContent = message;
    toastEl.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toastEl.classList.remove("show"), 2200);
}


/* ============================================================
   UNDO HISTORY
   ============================================================ */

const HISTORY_LIMIT = 50;
let history = [];

function snapshotState() { return JSON.stringify({ ids: pathwayIds, layout: pathwayLayout }); }

function pushHistory(snapshot) {
    history.push(snapshot || snapshotState());
    if (history.length > HISTORY_LIMIT) { history.shift(); }
    updateUndoUI();
}

function updateUndoUI() {
    undoButton.disabled = !history.length;
    undoButton.title = history.length ? "Undo the most recent change (Ctrl/⌘ + Z)" : "Nothing to undo";
}

function undoLastChange() {
    if (!history.length) { return; }
    const previous = JSON.parse(history.pop());
    pathwayIds = Array.isArray(previous.ids) ? previous.ids : [];
    pathwayLayout = normaliseLayout(previous.layout);
    savePathway();
    refreshPathwayViews();
    updateUndoUI();
}

undoButton.addEventListener("click", undoLastChange);


/* ============================================================
   COURSE LOOKUPS + HELPERS
   ============================================================ */

const coursesByTopic = {};
const courseLookup = {};

function slugify(value) {
    return String(value).toLowerCase().trim().replace(/\s+/g, "-").replace(/[^\w-]/g, "");
}
function courseIndex(course) { return slugify(course.url || course.title || "course"); }
function splitTags(course) {
    return course.tags ? String(course.tags).split(",").map(t => t.trim()).filter(Boolean) : [];
}

courses.forEach(course => {
    courseLookup[courseIndex(course)] = course;
    splitTags(course).forEach(topic => { (coursesByTopic[topic] = coursesByTopic[topic] || []).push(course); });
});

/* Drop anything that no longer exists (expired / removed courses) */
pathwayIds = pathwayIds.filter(id => courseLookup[id]);
pathwayLayout.connections = pathwayLayout.connections.filter(c => courseLookup[c.from] && courseLookup[c.to]);
Object.keys(pathwayLayout.notes).forEach(id => { if (!pathwayIds.includes(id)) { delete pathwayLayout.notes[id]; } });
savePathway();

function escapeHtml(value) {
    if (value === null || value === undefined) { return ""; }
    return String(value).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;");
}

const FORMATS = {
    "Online (self-service)": { label: "On-demand",           cls: "b-demand" },
    "Scheduled (online)":    { label: "Live online",         cls: "b-online" },
    "Scheduled (hybrid)":    { label: "Hybrid",              cls: "b-person" },
    "Scheduled (in-person)": { label: "In person",           cls: "b-person" },
    "Scheduled (in person)": { label: "In person",           cls: "b-person" },
    "Upcoming":              { label: "Upcoming",            cls: "b-other" },
    "Other":                 { label: "Other",               cls: "b-other" }
};

const formatLabel = f => (FORMATS[f] || {}).label || f;
const formatClass = f => (FORMATS[f] || {}).cls || "b-other";
const getPrimaryTopic = course => splitTags(course)[0] || "Training";
const courseTitle = course => course.title || "Untitled course";
const isCourseInPathway = course => pathwayIds.includes(courseIndex(course));
const showDates = course => course.dates && course.format !== "Online (self-service)";
const showLocation = course => course.location && !/^online$/i.test(course.location);

function plainMeta(course) {
    const parts = [];
    if (course.format) { parts.push(formatLabel(course.format)); }
    if (showDates(course)) { parts.push(course.dates); }
    return parts.join(" · ");
}

function titleHtml(course, className) {
    return course.url
        ? `<a class="${className}" href="${escapeHtml(course.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(courseTitle(course))}</a>`
        : `<span class="${className}">${escapeHtml(courseTitle(course))}</span>`;
}


/* ============================================================
   PATHWAY STATE
   ============================================================ */

function refreshPathwayViews() {
    updatePathwayUI();
    updateCourseStates();
}

function addToPathway(course, note, parentId) {

    const id = courseIndex(course);
    if (pathwayIds.includes(id)) { return; }

    pushHistory();
    pathwayIds.push(id);
    if (note) { pathwayLayout.notes[id] = note; }

    if (parentId && pathwayIds.includes(parentId)) {
        pathwayLayout.connections.push({ from: parentId, to: id, type: "spinoff", style: "dashed" });
    }

    savePathway();
    refreshPathwayViews();

}

function removeFromPathway(course) {

    const id = courseIndex(course);
    if (!pathwayIds.includes(id)) { return; }

    pushHistory();
    pathwayIds = pathwayIds.filter(item => item !== id);
    delete pathwayLayout.positions[id];
    delete pathwayLayout.notes[id];
    pathwayLayout.connections = pathwayLayout.connections.filter(c => c.from !== id && c.to !== id);

    savePathway();
    refreshPathwayViews();

}

function toggleCourse(course) {
    if (isCourseInPathway(course)) {
        removeFromPathway(course);
        toast("Removed from your pathway");
    }
    else {
        addToPathway(course);
        toast("Added to your pathway");
    }
}

function clearPathway() {

    if (!pathwayIds.length) { return; }
    if (!window.confirm("Clear your whole learning pathway? You can still undo this.")) { return; }

    pushHistory();
    pathwayIds = [];
    pathwayLayout = normaliseLayout(null);
    savePathway();
    refreshPathwayViews();

}


/* ============================================================
   CURATED PATHWAYS
   ============================================================ */

function resolveStep(step) {
    const url = typeof step === "string" ? step : (step && step.url);
    const id  = slugify(url || "");
    return { id: id, note: (step && step.note) || "", course: courseLookup[id] || null };
}

function resolveCurated(pathway) {

    const raw = Array.isArray(pathway.courses) ? pathway.courses : [];

    const steps = raw.map(step => {
        const resolved = resolveStep(step);
        resolved.spinoffs = (step && Array.isArray(step.spinoffs) ? step.spinoffs : [])
            .map(resolveStep)
            .filter(s => s.course);
        return resolved;
    });

    return { total: steps.length, available: steps.filter(s => s.course) };

}

function loadCuratedPathway(pathway, replace) {

    const resolved = resolveCurated(pathway);

    if (!resolved.available.length) {
        toast("None of the courses in this pathway are currently available.");
        return;
    }

    pushHistory();

    if (replace) {
        pathwayIds = [];
        pathwayLayout = normaliseLayout(null);
    }

    const ids = [];

    resolved.available.forEach(step => {
        ids.push(step.id);
        if (!pathwayIds.includes(step.id)) { pathwayIds.push(step.id); }
        if (step.note) { pathwayLayout.notes[step.id] = step.note; }
    });

    for (let i = 1; i < ids.length; i++) {
        if (!pathwayLayout.connections.some(c => c.from === ids[i - 1] && c.to === ids[i])) {
            pathwayLayout.connections.push({ from: ids[i - 1], to: ids[i], style: "solid" });
        }
    }

    resolved.available.forEach(step => {
        step.spinoffs.forEach(spinoff => {

            if (!pathwayIds.includes(spinoff.id)) { pathwayIds.push(spinoff.id); }
            if (spinoff.note) { pathwayLayout.notes[spinoff.id] = spinoff.note; }

            if (!pathwayLayout.connections.some(c => c.from === step.id && c.to === spinoff.id)) {
                pathwayLayout.connections.push({ from: step.id, to: spinoff.id, type: "spinoff", style: "dashed" });
            }

        });
    });

    savePathway();
    refreshPathwayViews();
    toast(replace ? "Curated pathway loaded" : "Curated pathway added");

    if (isMobile()) { setSide(true); }

}

function createCuratedStep(step, number) {

    const course = step.course;
    const li = document.createElement("li");
    li.className = "cur-step";
    li.dataset.courseId = step.id;

    li.innerHTML = `
        <span class="step-dot">${number}</span>
        <div class="step-body">
            ${titleHtml(course, "step-title")}
            <div class="step-sub">${escapeHtml([course.organisation, plainMeta(course)].filter(Boolean).join(" · "))}</div>
            ${step.note ? `<div class="step-note">${escapeHtml(step.note)}</div>` : ""}
        </div>
    `;

    step.spinoffs.forEach(spinoff => {

        const box = document.createElement("div");
        box.className = "step-optional";
        box.innerHTML = `
            <div class="step-optional-label">Optional</div>
            ${titleHtml(spinoff.course, "step-title")}
            <div class="step-sub">${escapeHtml([spinoff.course.organisation, plainMeta(spinoff.course)].filter(Boolean).join(" · "))}</div>
            ${spinoff.note ? `<div class="step-note">${escapeHtml(spinoff.note)}</div>` : ""}
            <button type="button" class="mini-btn" data-course-id="${escapeHtml(spinoff.id)}">+ Add</button>
        `;

        box.querySelector("button").addEventListener("click", function () {
            if (isCourseInPathway(spinoff.course)) { removeFromPathway(spinoff.course); }
            else { addToPathway(spinoff.course, spinoff.note, step.id); }
        });

        li.querySelector(".step-body").appendChild(box);

    });

    return li;

}

function renderCuratedPathways() {

    const valid = curatedPathways.filter(p => p && p.title);
    if (!valid.length) { return; }

    TABS.curated.tab.style.display = "";
    $("empty-browse-curated").style.display = "";

    valid.forEach(pathway => {

        const resolved = resolveCurated(pathway);
        const count = resolved.available.length;
        const optional = resolved.available.reduce((n, s) => n + s.spinoffs.length, 0);

        const card = document.createElement("article");
        card.className = "cur-card";
        card.dataset.ids = resolved.available.map(s => s.id).join("|");

        card.innerHTML = `
            <div class="cur-head">
                <div class="cur-icon">${escapeHtml(pathway.icon || "🧭")}</div>
                <div>
                    <h3 class="cur-title">${escapeHtml(pathway.title)}</h3>
                    ${pathway.audience ? `<div class="cur-audience">For ${escapeHtml(pathway.audience.charAt(0).toLowerCase() + pathway.audience.slice(1))}</div>` : ""}
                </div>
            </div>
            ${pathway.description ? `<p class="cur-desc">${escapeHtml(pathway.description)}</p>` : ""}
            <p class="cur-stats">
                ${count} ${count === 1 ? "step" : "steps"}${optional ? `, ${optional} optional` : ""}
                ${count < resolved.total ? ` · <span class="partial">${count} of ${resolved.total} courses currently available</span>` : ""}
                <span class="cur-loaded"> · ✓ In your pathway</span>
            </p>
            <div class="cur-actions">
                <button type="button" class="cat-btn cat-btn-primary cur-use" ${count ? "" : "disabled"}>Use pathway</button>
                <button type="button" class="cat-btn cur-add" ${count ? "" : "disabled"}>Add to mine</button>
            </div>
            <details class="cur-route">
                <summary>View the route</summary>
                <ol class="cur-steps"></ol>
            </details>
        `;

        const list = card.querySelector(".cur-steps");

        if (count) { resolved.available.forEach((step, i) => list.appendChild(createCuratedStep(step, i + 1))); }
        else { list.innerHTML = `<li class="step-sub">No courses in this pathway are currently available.</li>`; }

        card.querySelector(".cur-use").addEventListener("click", function () {
            if (pathwayIds.length && !window.confirm("This replaces your current pathway (you can undo it). Continue?")) { return; }
            loadCuratedPathway(pathway, true);
        });

        card.querySelector(".cur-add").addEventListener("click", () => loadCuratedPathway(pathway, false));

        curatedGrid.appendChild(card);

    });

}


/* ============================================================
   CATALOGUE (search + filters + topic lists)
   ============================================================ */

const groups = [];
const usedTopics = new Set();

Object.entries(topicGroups).forEach(([name, data]) => {

    const topics = data.topics
        .filter(t => coursesByTopic[t] && coursesByTopic[t].length)
        .map(t => ({ name: t, courses: coursesByTopic[t] }));

    topics.forEach(t => usedTopics.add(t.name));
    if (topics.length) { groups.push({ name: name, icon: data.icon, topics: topics }); }

});

/* Safety net: tags missing from training-topics.yml still show up */
const orphanTopics = Object.keys(coursesByTopic).filter(t => !usedTopics.has(t)).sort();

if (orphanTopics.length) {
    groups.push({ name: "More training", icon: "📚", topics: orphanTopics.map(t => ({ name: t, courses: coursesByTopic[t] })) });
}

groups.forEach(g => {
    g.courseCount = new Set(g.topics.flatMap(t => t.courses.map(courseIndex))).size;
});

/* Hero stats */
(function () {
    const providers = new Set(courses.map(c => c.organisation).filter(Boolean)).size;
    const topics = groups.reduce((n, g) => n + g.topics.length, 0);
    $("hero-stats").innerHTML = [[courses.length, "courses"], [providers, "providers"], [topics, "topics"]]
        .map(s => `<li><strong>${s[0]}</strong><span>${s[1]}</span></li>`).join("");
})();

const filters = { q: "", group: "all", format: "all" };
const expandedTopics = new Set();
const COLLAPSED_COUNT = 5;

const courseSearchText = c => [c.title, c.organisation, c.tags, c.location].join(" ").toLowerCase();

function highlight(text, q) {
    const safe = escapeHtml(text);
    if (!q) { return safe; }
    const i = String(text).toLowerCase().indexOf(q);
    if (i === -1) { return safe; }
    return escapeHtml(text.slice(0, i)) + "<mark>" + escapeHtml(text.slice(i, i + q.length)) + "</mark>" + escapeHtml(text.slice(i + q.length));
}

function createCourseRow(course, q) {

    const id = courseIndex(course);
    const inPath = pathwayIds.includes(id);

    const row = document.createElement("div");
    row.className = "row" + (inPath ? " in-pathway" : "");
    row.dataset.courseId = id;

    const sub = [course.organisation ? highlight(course.organisation, q) : "", showLocation(course) ? escapeHtml(course.location) : ""].filter(Boolean).join(" · ");

    row.innerHTML = `
        <div class="row-main">
            ${course.url
                ? `<a class="row-title" href="${escapeHtml(course.url)}" target="_blank" rel="noopener noreferrer">${highlight(courseTitle(course), q)}</a>`
                : `<span class="row-title">${highlight(courseTitle(course), q)}</span>`}
            ${sub ? `<div class="row-sub">${sub}</div>` : ""}
        </div>
        <div class="row-when">
            ${course.format ? `<span class="badge ${formatClass(course.format)}">${escapeHtml(formatLabel(course.format))}</span>` : ""}
            ${showDates(course) ? `<span>${escapeHtml(course.dates)}</span>` : ""}
        </div>
        <button type="button" class="add-btn" data-add="${escapeHtml(id)}"
            aria-pressed="${inPath}" aria-label="Add to my pathway: ${escapeHtml(courseTitle(course))}"
            title="${inPath ? "Remove from my pathway" : "Add to my pathway"}">${inPath ? "✓" : "+"}</button>
    `;

    return row;

}

function createTopic(group, topic, list, q, forceOpen) {

    const key = group.name + "::" + topic.name;
    const collapsible = list.length > COLLAPSED_COUNT + 1;
    const open = forceOpen || !collapsible || expandedTopics.has(key);
    const visible = open ? list : list.slice(0, COLLAPSED_COUNT);

    const wrap = document.createElement("div");
    wrap.className = "topic";

    const total = list.length === topic.courses.length ? `${list.length}` : `${list.length} of ${topic.courses.length}`;

    wrap.innerHTML = `
        <div class="topic-head"><h3>${highlight(topic.name, q)}</h3><span class="topic-count">${total} ${list.length === 1 ? "course" : "courses"}</span></div>
        <div class="rows"></div>
    `;

    const rows = wrap.querySelector(".rows");
    visible.forEach(course => rows.appendChild(createCourseRow(course, q)));

    if (collapsible && !forceOpen) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "more-btn";
        if (open) { btn.dataset.collapse = key; btn.textContent = "Show fewer"; }
        else { btn.dataset.expand = key; btn.textContent = `Show ${list.length - COLLAPSED_COUNT} more`; }
        rows.appendChild(btn);
    }

    return wrap;

}

function renderBoard() {

    const q = filters.q.trim().toLowerCase();
    const filtering = Boolean(q) || filters.format !== "all";
    const shown = new Set();

    board.innerHTML = "";

    groups.forEach(group => {

        if (filters.group !== "all" && filters.group !== group.name) { return; }

        const groupMatch = q && group.name.toLowerCase().includes(q);
        const topicEls = [];

        group.topics.forEach(topic => {

            const topicMatch = groupMatch || (q && topic.name.toLowerCase().includes(q));

            const list = topic.courses.filter(c =>
                (filters.format === "all" || c.format === filters.format) &&
                (!q || topicMatch || courseSearchText(c).includes(q))
            );

            if (list.length) {
                list.forEach(c => shown.add(courseIndex(c)));
                topicEls.push(createTopic(group, topic, list, q, filtering));
            }

        });

        if (!topicEls.length) { return; }

        const section = document.createElement("section");
        section.className = "group-section";
        section.innerHTML = `
            <div class="group-head">
                <div class="group-icon">${escapeHtml(group.icon)}</div>
                <div><h2>${escapeHtml(group.name)}</h2><small>${topicEls.length} ${topicEls.length === 1 ? "topic" : "topics"}</small></div>
            </div>
        `;

        topicEls.forEach(el => section.appendChild(el));
        board.appendChild(section);

    });

    const n = shown.size;
    boardEmpty.style.display = n ? "none" : "block";
    boardStatus.textContent = n ? `Showing ${n} ${n === 1 ? "course" : "courses"}` : "";

}

function renderChips() {

    const chip = (label, count, active, attr, value) =>
        `<button type="button" class="chip${active ? " active" : ""}" ${attr}="${escapeHtml(value)}" aria-pressed="${active}">${label}${count !== null ? ` <span class="chip-n">${count}</span>` : ""}</button>`;

    groupChips.innerHTML =
        chip("All groups", courses.length, filters.group === "all", "data-group", "all") +
        groups.map(g => chip(`${escapeHtml(g.icon)} ${escapeHtml(g.name)}`, g.courseCount, filters.group === g.name, "data-group", g.name)).join("");

    const formats = [...new Set(courses.map(c => c.format).filter(Boolean))];

    formatChips.innerHTML = formats.length > 1
        ? chip("Any format", null, filters.format === "all", "data-format", "all") +
          formats.map(f => chip(escapeHtml(formatLabel(f)), null, filters.format === f, "data-format", f)).join("")
        : "";

}

function updateFilters() {
    renderChips();
    renderBoard();
}

groupChips.addEventListener("click", function (event) {
    const b = event.target.closest("[data-group]");
    if (!b) { return; }
    filters.group = b.dataset.group;
    updateFilters();
});

formatChips.addEventListener("click", function (event) {
    const b = event.target.closest("[data-format]");
    if (!b) { return; }
    filters.format = b.dataset.format;
    updateFilters();
});

let searchTimer = null;
searchInput.addEventListener("input", function () {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => { filters.q = searchInput.value; renderBoard(); }, 120);
});

$("clear-filters").addEventListener("click", function () {
    filters.q = ""; filters.group = "all"; filters.format = "all";
    searchInput.value = "";
    updateFilters();
});

/* One delegated listener for add buttons and show more/fewer */
board.addEventListener("click", function (event) {

    const add = event.target.closest("[data-add]");

    if (add) {
        const course = courseLookup[add.dataset.add];
        if (course) { toggleCourse(course); }
        return;
    }

    const more = event.target.closest("[data-expand], [data-collapse]");

    if (more) {
        if (more.dataset.expand) { expandedTopics.add(more.dataset.expand); }
        else { expandedTopics.delete(more.dataset.collapse); }
        renderBoard();
    }

});

function updateCourseStates() {

    board.querySelectorAll(".row").forEach(row => {

        const inPath = pathwayIds.includes(row.dataset.courseId);
        const btn = row.querySelector(".add-btn");

        row.classList.toggle("in-pathway", inPath);
        btn.textContent = inPath ? "✓" : "+";
        btn.setAttribute("aria-pressed", String(inPath));
        btn.title = inPath ? "Remove from my pathway" : "Add to my pathway";

    });

    curatedGrid.querySelectorAll(".cur-step").forEach(step => {
        step.classList.toggle("in-pathway", pathwayIds.includes(step.dataset.courseId));
    });

    curatedGrid.querySelectorAll(".step-optional .mini-btn").forEach(button => {
        const added = pathwayIds.includes(button.dataset.courseId);
        button.classList.toggle("added", added);
        button.textContent = added ? "✓ In pathway" : "+ Add";
    });

    curatedGrid.querySelectorAll(".cur-card").forEach(card => {
        const ids = card.dataset.ids ? card.dataset.ids.split("|") : [];
        card.classList.toggle("is-loaded", ids.length > 0 && ids.every(id => pathwayIds.includes(id)));
    });

}


/* ============================================================
   SIDEBAR (docked on desktop, bottom sheet on mobile)
   ============================================================ */

let sideOpen = isMobile() ? false : readStorage(KEYS.side) !== "closed";

function applySideState() {

    if (isMobile()) {
        side.classList.toggle("open", sideOpen);
        layout.classList.remove("side-hidden");
    }
    else {
        side.classList.remove("open");
        layout.classList.toggle("side-hidden", !sideOpen);
    }

    sideToggle.setAttribute("aria-expanded", String(sideOpen));
    fab.classList.toggle("hide", isMobile() && sideOpen);

}

function setSide(open) {
    sideOpen = open;
    if (!isMobile()) { writeStorage(KEYS.side, open ? "open" : "closed"); }
    applySideState();
}

sideToggle.addEventListener("click", () => setSide(!sideOpen));
fab.addEventListener("click", () => setSide(true));
$("close-side").addEventListener("click", () => setSide(false));
$("empty-browse-curated").addEventListener("click", function () {
    if (isMobile()) { setSide(false); }
    setTab("curated");
    $("cat").scrollIntoView({ behavior: "smooth", block: "start" });
});

window.addEventListener("resize", applySideState);


/* ============================================================
   PATHWAY LIST (sidebar)
   ============================================================ */

function updatePathwayUI() {

    const count = pathwayIds.length;

    $("pathway-count").textContent = count;
    $("pathway-fab-count").textContent = count;
    $("pathway-summary-count").textContent = `${count} ${count === 1 ? "course" : "courses"}`;

    pathwayEmpty.hidden = count > 0;
    pathwayContent.hidden = count === 0;

    renderPathwayList();
    if (currentTab === "map") { renderMap(); }

}

function renderPathwayList() {

    pathwayList.innerHTML = "";

    pathwayIds.forEach((id, index) => {
        const course = courseLookup[id];
        if (course) { pathwayList.appendChild(createPathwayListItem(course, id, index)); }
    });

}

function createPathwayListItem(course, id, index) {

    const item = document.createElement("div");
    item.className = "pathway-item";
    item.draggable = true;
    item.dataset.courseId = id;

    const note = pathwayLayout.notes[id];

    item.innerHTML = `
        <div class="pathway-number">${index + 1}</div>
        <div class="pathway-item-body">
            ${titleHtml(course, "pathway-item-title")}
            <div class="pathway-item-sub">${escapeHtml([course.organisation, plainMeta(course)].filter(Boolean).join(" · "))}</div>
            ${note ? `<div class="pathway-item-note">${escapeHtml(note)}</div>` : ""}
            <div class="pathway-item-actions">
                <button type="button" class="mini-btn" data-dir="up" aria-label="Move up" ${index === 0 ? "disabled" : ""}>↑</button>
                <button type="button" class="mini-btn" data-dir="down" aria-label="Move down" ${index === pathwayIds.length - 1 ? "disabled" : ""}>↓</button>
                <button type="button" class="mini-btn remove">Remove</button>
            </div>
        </div>
    `;

    item.querySelectorAll("[data-dir]").forEach(b => b.addEventListener("click", () => movePathwayItem(id, b.dataset.dir)));
    item.querySelector(".remove").addEventListener("click", () => removeFromPathway(course));

    item.addEventListener("dragstart", function (event) {
        draggedPathwayId = id;
        item.classList.add("dragging");
        try { event.dataTransfer.effectAllowed = "move"; event.dataTransfer.setData("text/plain", id); } catch (e) { /* ignore */ }
    });

    item.addEventListener("dragend", function () {
        draggedPathwayId = null;
        item.classList.remove("dragging");
        pathwayList.querySelectorAll(".drag-over").forEach(el => el.classList.remove("drag-over"));
    });

    item.addEventListener("dragover", function (event) {
        if (!draggedPathwayId || draggedPathwayId === id) { return; }
        event.preventDefault();
        item.classList.add("drag-over");
    });

    item.addEventListener("dragleave", () => item.classList.remove("drag-over"));

    item.addEventListener("drop", function (event) {
        event.preventDefault();
        item.classList.remove("drag-over");
        if (!draggedPathwayId || draggedPathwayId === id) { return; }
        const rect = item.getBoundingClientRect();
        reorderPathway(draggedPathwayId, id, (event.clientY - rect.top) < rect.height / 2);
        draggedPathwayId = null;
    });

    return item;

}

function movePathwayItem(id, direction) {

    const index = pathwayIds.indexOf(id);
    const target = direction === "up" ? index - 1 : index + 1;
    if (index === -1 || target < 0 || target >= pathwayIds.length) { return; }

    pushHistory();
    [pathwayIds[index], pathwayIds[target]] = [pathwayIds[target], pathwayIds[index]];
    savePathway();
    refreshPathwayViews();

}

function reorderPathway(draggedId, targetId, insertBefore) {

    const from = pathwayIds.indexOf(draggedId);
    if (from === -1) { return; }

    pushHistory();
    pathwayIds.splice(from, 1);

    let to = pathwayIds.indexOf(targetId);
    if (to === -1) { to = pathwayIds.length; }
    else if (!insertBefore) { to += 1; }

    pathwayIds.splice(to, 0, draggedId);
    savePathway();
    refreshPathwayViews();

}

$("clear-pathway").addEventListener("click", clearPathway);


/* ============================================================
   TABS  (Catalogue / Curated pathways / Pathway map)
   ============================================================ */

let currentTab = "catalogue";

function setTab(name) {

    if (!TABS[name] || (name === "curated" && !curatedGrid.children.length)) { name = "catalogue"; }

    currentTab = name;
    writeStorage(KEYS.tab, name);

    Object.keys(TABS).forEach(key => {
        const active = key === name;
        TABS[key].tab.classList.toggle("active", active);
        TABS[key].tab.setAttribute("aria-selected", String(active));
        TABS[key].view.hidden = !active;
    });

    filterRows.hidden = name !== "catalogue";

    if (name === "map") { mapNeedsFit = true; renderMap(); }

}

Object.keys(TABS).forEach(key => TABS[key].tab.addEventListener("click", () => setTab(key)));


/* ============================================================
   PATHWAY MAP (canvas)
   ============================================================ */

const SVG_NS = "http://www.w3.org/2000/svg";
const SVG_EXTENT = 16000;
const NODE_W = 230, NODE_H = 120;

const ARROW_DEFS = `
    <defs>
        <marker id="pathway-arrow" viewBox="0 0 0 0" refX="9" refY="5" markerWidth="0" markerHeight="0" orient="auto-start-reverse">
            <path d="M0 0 L10 5 L0 10 z" fill="#940594"></path>
        </marker>
    </defs>`;

let pViewport = null, pWorld = null, pNodes = null, pSvg = null;
let pZoom = 1, pPanX = 0, pPanY = 0;
const P_MIN = 0.3, P_MAX = 2.5, P_STEP = 1.2;
let panning = false, panSX = 0, panSY = 0, panOX = 0, panOY = 0;
let mapNeedsFit = true;

function createCanvas() {

    mapHost.innerHTML = "";

    pViewport = document.createElement("div");
    pViewport.className = "pathway-viewport";

    pWorld = document.createElement("div");
    pWorld.className = "pathway-world";

    pSvg = document.createElementNS(SVG_NS, "svg");
    pSvg.classList.add("pathway-svg");
    pSvg.setAttribute("width", SVG_EXTENT);
    pSvg.setAttribute("height", SVG_EXTENT);
    pSvg.setAttribute("viewBox", `${-SVG_EXTENT / 2} ${-SVG_EXTENT / 2} ${SVG_EXTENT} ${SVG_EXTENT}`);
    pSvg.innerHTML = ARROW_DEFS;

    pNodes = document.createElement("div");
    pNodes.className = "pathway-nodes";

    pWorld.appendChild(pSvg);
    pWorld.appendChild(pNodes);
    pViewport.appendChild(pWorld);
    mapHost.appendChild(pViewport);

    pViewport.addEventListener("pointerdown", startPan);
    pViewport.addEventListener("pointermove", movePan);
    pViewport.addEventListener("pointerup", stopPan);
    pViewport.addEventListener("pointercancel", stopPan);
    pViewport.addEventListener("wheel", onWheel, { passive: false });

    applyTransform();

}

function applyTransform() {
    if (!pWorld) { return; }
    pWorld.style.transform = `translate(${pPanX}px, ${pPanY}px) scale(${pZoom})`;
    zoomIndicator.textContent = `${Math.round(pZoom * 100)}%`;
}

function toWorld(event) {
    const rect = pViewport.getBoundingClientRect();
    return { x: (event.clientX - rect.left - pPanX) / pZoom, y: (event.clientY - rect.top - pPanY) / pZoom };
}

function startPan(event) {
    if (event.target.closest(".pathway-node, button, a, .pathway-line-hit")) { return; }
    event.preventDefault();
    panning = true;
    panSX = event.clientX; panSY = event.clientY; panOX = pPanX; panOY = pPanY;
    pViewport.classList.add("is-panning");
    pViewport.setPointerCapture(event.pointerId);
}

function movePan(event) {
    if (!panning) { return; }
    pPanX = panOX + event.clientX - panSX;
    pPanY = panOY + event.clientY - panSY;
    applyTransform();
}

function stopPan(event) {
    if (!panning) { return; }
    panning = false;
    pViewport.classList.remove("is-panning");
    try { pViewport.releasePointerCapture(event.pointerId); } catch (e) { /* released */ }
}

function zoomAt(factor, cx, cy) {

    if (!pViewport) { return; }

    const rect = pViewport.getBoundingClientRect();
    const px = (cx === undefined ? rect.left + rect.width / 2 : cx) - rect.left;
    const py = (cy === undefined ? rect.top + rect.height / 2 : cy) - rect.top;

    const oldZ = pZoom;
    const newZ = Math.max(P_MIN, Math.min(P_MAX, oldZ * factor));
    if (newZ === oldZ) { return; }

    pPanX = px - (px - pPanX) * (newZ / oldZ);
    pPanY = py - (py - pPanY) * (newZ / oldZ);
    pZoom = newZ;
    applyTransform();

}

function onWheel(event) {
    event.preventDefault();
    zoomAt(event.deltaY < 0 ? P_STEP : 1 / P_STEP, event.clientX, event.clientY);
}

/* Fit all cards into view */
function fitView() {

    const ids = pathwayIds.filter(id => pathwayLayout.positions[id]);

    if (!ids.length || !pViewport) { pZoom = 1; pPanX = 40; pPanY = 40; applyTransform(); return; }

    let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;

    ids.forEach(id => {
        const r = rectOf(id);
        minX = Math.min(minX, r.x); minY = Math.min(minY, r.y);
        maxX = Math.max(maxX, r.x + r.w); maxY = Math.max(maxY, r.y + r.h);
    });

    const box = pViewport.getBoundingClientRect();
    const pad = 40;
    const z = Math.max(P_MIN, Math.min(1, (box.width - pad * 2) / (maxX - minX), (box.height - pad * 2) / (maxY - minY)));

    pZoom = z;
    pPanX = pad + (box.width - pad * 2 - (maxX - minX) * z) / 2 - minX * z;
    pPanY = pad + (box.height - pad * 2 - (maxY - minY) * z) / 2 - minY * z;
    applyTransform();

}

$("pathway-zoom-in").addEventListener("click", () => zoomAt(P_STEP));
$("pathway-zoom-out").addEventListener("click", () => zoomAt(1 / P_STEP));
$("pathway-reset-view").addEventListener("click", fitView);

$("auto-arrange").addEventListener("click", function () {
    if (!pathwayIds.length) { return; }
    pushHistory();
    pathwayLayout.positions = {};
    savePathway();
    mapNeedsFit = true;
    renderMap();
});

function defaultPosition(index) {

    const id = pathwayIds[index];
    const gapX = 45, gapY = 45;

    const spin = pathwayLayout.connections.find(c => c.type === "spinoff" && c.to === id);

    if (spin) {

        const parentIndex = pathwayIds.indexOf(spin.from);

        if (parentIndex !== -1 && parentIndex !== index) {

            const parentPos = getPosition(spin.from, parentIndex);
            const siblings = pathwayLayout.connections.filter(c => c.type === "spinoff" && c.from === spin.from && pathwayIds.includes(c.to));
            const sIndex = Math.max(0, siblings.findIndex(c => c.to === id));
            const side = sIndex % 2 === 0 ? 1 : -1;
            const level = Math.floor(sIndex / 2) + 1;

            return { x: parentPos.x, y: parentPos.y + side * level * (NODE_H + 30 + gapY) };

        }

    }

    return { x: index * (NODE_W + gapX), y: 0 };

}

function getPosition(id, index) {
    if (!pathwayLayout.positions[id]) { pathwayLayout.positions[id] = defaultPosition(index); }
    return pathwayLayout.positions[id];
}

function nodeEl(id) {
    return pNodes ? pNodes.querySelector(`[data-course-id="${CSS.escape(id)}"]`) : null;
}

/* Geometry works with or without the DOM (so downloads work from any tab) */
function rectOf(id) {
    const el = nodeEl(id);
    const p = pathwayLayout.positions[id] || { x: 0, y: 0 };
    return { x: p.x, y: p.y, w: el ? el.offsetWidth : NODE_W, h: el ? el.offsetHeight : NODE_H };
}

function anchor(r, side) {
    switch (side) {
        case "top":    return { x: r.x + r.w / 2, y: r.y };
        case "right":  return { x: r.x + r.w,     y: r.y + r.h / 2 };
        case "bottom": return { x: r.x + r.w / 2, y: r.y + r.h };
        default:       return { x: r.x,           y: r.y + r.h / 2 };
    }
}

function connectionPoints(a, b) {

    const dx = (b.x + b.w / 2) - (a.x + a.w / 2);
    const dy = (b.y + b.h / 2) - (a.y + a.h / 2);
    let s, t;

    if (Math.abs(dx) > Math.abs(dy)) { s = dx > 0 ? "right" : "left"; t = dx > 0 ? "left" : "right"; }
    else { s = dy > 0 ? "bottom" : "top"; t = dy > 0 ? "top" : "bottom"; }

    return { start: anchor(a, s), end: anchor(b, t) };

}

function bezier(x1, y1, x2, y2) {

    const dx = x2 - x1, dy = y2 - y1;

    if (Math.abs(dy) > Math.abs(dx)) {
        const d = Math.max(40, Math.abs(dy) * 0.5) * (dy >= 0 ? 1 : -1);
        return `M ${x1} ${y1} C ${x1} ${y1 + d}, ${x2} ${y2 - d}, ${x2} ${y2}`;
    }

    const d = Math.max(50, Math.abs(dx) * 0.5) * (dx >= 0 ? 1 : -1);
    return `M ${x1} ${y1} C ${x1 + d} ${y1}, ${x2 - d} ${y2}, ${x2} ${y2}`;

}

function renderMap() {

    createCanvas();

    if (!pathwayIds.length) {
        mapHost.insertAdjacentHTML("beforeend", `<div class="map-empty"><div><p class="empty-title">Your pathway is empty</p><p>Go to the catalogue and press + on the courses you want to add.</p></div></div>`);
        return;
    }

    pathwayIds.forEach((id, index) => { if (courseLookup[id]) { createNode(courseLookup[id], index); } });
    savePathway();

    requestAnimationFrame(function () {
        drawConnections();
        if (mapNeedsFit) { fitView(); mapNeedsFit = false; }
    });

}

function createNode(course, index) {

    const id = courseIndex(course);
    const node = document.createElement("div");
    node.className = "pathway-node";
    node.dataset.courseId = id;

    const pos = getPosition(id, index);
    node.style.left = pos.x + "px";
    node.style.top = pos.y + "px";

    node.innerHTML = `
        <button type="button" class="pathway-node-remove" title="Remove" aria-label="Remove from pathway">×</button>
        <div class="pathway-handle top" data-side="top"></div>
        <div class="pathway-handle right" data-side="right"></div>
        <div class="pathway-handle bottom" data-side="bottom"></div>
        <div class="pathway-handle left" data-side="left"></div>
        <div class="pathway-node-title">${titleHtml(course, "node-link")}</div>
        ${course.organisation ? `<div class="pathway-node-org">${escapeHtml(course.organisation)}</div>` : ""}
        <div class="pathway-node-meta">${escapeHtml(getPrimaryTopic(course))}${course.format ? `<br>${escapeHtml(formatLabel(course.format))}` : ""}</div>
    `;

    pNodes.appendChild(node);

    node.querySelector(".pathway-node-remove").addEventListener("click", function (event) {
        event.stopPropagation();
        removeFromPathway(course);
    });

    node.querySelectorAll(".pathway-handle").forEach(handle => {
        handle.addEventListener("pointerdown", function (event) {
            event.preventDefault();
            event.stopPropagation();
            startConnection(event, id, handle.dataset.side);
        });
    });

    node.addEventListener("pointerdown", function (event) {
        if (event.target.closest(".pathway-handle, .pathway-node-remove")) { return; }
        startNodeDrag(event, node);
    });

}

function startNodeDrag(event, node) {

    event.preventDefault();
    event.stopPropagation();

    const id = node.dataset.courseId;
    const pos = pathwayLayout.positions[id] || { x: 0, y: 0 };
    const sw = toWorld(event);
    const ox = sw.x - pos.x, oy = sw.y - pos.y;
    const sx = event.clientX, sy = event.clientY;
    const before = snapshotState();
    let moved = false;

    node.classList.add("dragging");

    function move(e) {

        if (!moved && Math.hypot(e.clientX - sx, e.clientY - sy) < 4) { return; }
        moved = true;

        const w = toWorld(e);
        const x = w.x - ox, y = w.y - oy;

        node.style.left = x + "px";
        node.style.top = y + "px";
        pathwayLayout.positions[id] = { x: x, y: y };
        drawConnections();

    }

    function stop() {

        node.classList.remove("dragging");
        document.removeEventListener("pointermove", move);
        document.removeEventListener("pointerup", stop);
        document.removeEventListener("pointercancel", stop);

        if (moved) {
            pushHistory(before);
            const suppress = e => { e.preventDefault(); e.stopPropagation(); };
            node.addEventListener("click", suppress, true);
            setTimeout(() => node.removeEventListener("click", suppress, true), 0);
        }

        savePathway();

    }

    document.addEventListener("pointermove", move);
    document.addEventListener("pointerup", stop);
    document.addEventListener("pointercancel", stop);

}

let activeConnection = null;

function startConnection(event, sourceId, side) {

    const temp = document.createElementNS(SVG_NS, "path");
    temp.classList.add("pathway-temp-line");
    pSvg.appendChild(temp);

    activeConnection = { source: sourceId, start: anchor(rectOf(sourceId), side), temp: temp };

    document.addEventListener("pointermove", moveConnection);
    document.addEventListener("pointerup", finishConnection, { once: true });
    document.addEventListener("pointercancel", finishConnection, { once: true });

    moveConnection(event);

}

function moveConnection(event) {
    if (!activeConnection) { return; }
    const p = toWorld(event);
    activeConnection.temp.setAttribute("d", bezier(activeConnection.start.x, activeConnection.start.y, p.x, p.y));
}

function finishConnection(event) {

    document.removeEventListener("pointermove", moveConnection);
    if (!activeConnection) { return; }

    const el = event.type === "pointerup" ? document.elementFromPoint(event.clientX, event.clientY) : null;
    const target = el ? el.closest(".pathway-node") : null;

    if (target && target.dataset.courseId && target.dataset.courseId !== activeConnection.source) {

        const from = activeConnection.source, to = target.dataset.courseId;

        if (!pathwayLayout.connections.some(c => c.from === from && c.to === to)) {
            pushHistory();
            pathwayLayout.connections.push({ from: from, to: to, style: "solid" });
        }

    }

    activeConnection.temp.remove();
    activeConnection = null;
    savePathway();
    drawConnections();

}

/* Click a connector: solid -> dashed -> removed */
function cycleConnection(conn) {

    pushHistory();

    if (connectionStyle(conn) === "solid") { conn.style = "dashed"; }
    else { pathwayLayout.connections = pathwayLayout.connections.filter(c => c !== conn); }

    savePathway();
    drawConnections();

}

function drawConnections() {

    if (!pSvg) { return; }

    pSvg.innerHTML = ARROW_DEFS;

    pathwayLayout.connections = pathwayLayout.connections.filter(c => pathwayIds.includes(c.from) && pathwayIds.includes(c.to));

    pathwayLayout.connections.forEach(conn => {

        if (!nodeEl(conn.from) || !nodeEl(conn.to)) { return; }

        const p = connectionPoints(rectOf(conn.from), rectOf(conn.to));
        const d = bezier(p.start.x, p.start.y, p.end.x, p.end.y);
        const dashed = connectionStyle(conn) === "dashed";

        const hit = document.createElementNS(SVG_NS, "path");
        hit.classList.add("pathway-line-hit");
        hit.setAttribute("d", d);
        hit.innerHTML = dashed
            ? "<title>Optional (dashed). Click to remove this connection</title>"
            : "<title>Required (solid). Click to make it optional (dashed)</title>";

        hit.addEventListener("click", function (event) {
            event.preventDefault();
            event.stopPropagation();
            cycleConnection(conn);
        });

        const line = document.createElementNS(SVG_NS, "path");
        line.classList.add("pathway-line");
        if (dashed) { line.classList.add("pathway-line-dashed"); }
        line.setAttribute("d", d);
        line.setAttribute("marker-end", "url(#pathway-arrow)");

        pSvg.appendChild(hit);
        pSvg.appendChild(line);

    });

}


/* ============================================================
   KEYBOARD
   ============================================================ */

document.addEventListener("keydown", function (event) {

    if (event.key === "Escape" && isMobile() && sideOpen) {
        setSide(false);
        return;
    }

    if ((event.ctrlKey || event.metaKey) && !event.shiftKey && event.key.toLowerCase() === "z") {
        const tag = (event.target && event.target.tagName) || "";
        if (!/^(INPUT|TEXTAREA)$/.test(tag) && history.length) {
            event.preventDefault();
            undoLastChange();
        }
    }

});


/* ============================================================
   DOWNLOAD
   ============================================================ */

function triggerHtmlDownload(html, filename) {

    const blob = new Blob([html], { type: "text/html;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");

    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);

}

function buildListDownloadHtml() {

    const rows = pathwayIds
        .filter(id => courseLookup[id])
        .map((id, index) => {

            const course = courseLookup[id];
            const note = pathwayLayout.notes[id];

            return `
                <article class="course">
                    <div class="number">${index + 1}</div>
                    <div>
                        <h2>${course.url ? `<a href="${escapeHtml(course.url)}">${escapeHtml(courseTitle(course))}</a>` : escapeHtml(courseTitle(course))}</h2>
                        ${course.organisation ? `<p>${escapeHtml(course.organisation)}</p>` : ""}
                        <small>${escapeHtml(plainMeta(course))}</small>
                        ${showLocation(course) ? `<br><small>${escapeHtml(course.location)}</small>` : ""}
                        ${note ? `<div class="note">${escapeHtml(note)}</div>` : ""}
                    </div>
                </article>`;

        })
        .join("");

    return `<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>My SHAREing Learning Pathway</title>
<style>
body{font-family:Arial,sans-serif;max-width:900px;margin:40px auto;padding:20px;color:#1f2937}
h1{color:#421456}.course{display:flex;gap:20px;margin-bottom:15px;padding:20px;border:1px solid #e5e7eb;border-radius:10px}
.number{font-weight:bold;color:#940594}h2{margin:0 0 5px;font-size:1.1rem}a{color:#1f2937;text-decoration:none}
p{margin:0 0 4px;color:#940594;font-size:.85rem}small{color:#5b6472}.note{margin-top:6px;font-size:.85rem;font-style:italic;color:#475569}
</style></head><body><h1>My Learning Pathway</h1>${rows}</body></html>`;

}

function buildMapDownloadHtml() {

    const ids = pathwayIds.filter(id => courseLookup[id]);
    ids.forEach(id => getPosition(id, pathwayIds.indexOf(id)));

    const rects = ids.map(id => Object.assign({ id: id }, rectOf(id)));

    const minX = Math.min(...rects.map(r => r.x)), minY = Math.min(...rects.map(r => r.y));
    const maxX = Math.max(...rects.map(r => r.x + r.w)), maxY = Math.max(...rects.map(r => r.y + r.h));

    const pad = 40, ox = pad - minX, oy = pad - minY;
    const W = (maxX - minX) + pad * 2, H = (maxY - minY) + pad * 2;
    const byId = {};
    rects.forEach(r => { byId[r.id] = r; });

    const paths = pathwayLayout.connections
        .filter(c => byId[c.from] && byId[c.to])
        .map(c => {
            const p = connectionPoints(byId[c.from], byId[c.to]);
            const d = bezier(p.start.x + ox, p.start.y + oy, p.end.x + ox, p.end.y + oy);
            const dash = connectionStyle(c) === "dashed" ? `stroke-dasharray="8 6"` : "";
            return `<path d="${d}" fill="none" stroke="#940594" stroke-width="2.5" opacity="0.75" ${dash} marker-end="url(#pathway-arrow)"/>`;
        }).join("");

    const cards = rects.map(r => {
        const course = courseLookup[r.id];
        return `<div class="card" style="left:${r.x + ox}px;top:${r.y + oy}px;width:${r.w}px">
            <div class="t">${course.url ? `<a href="${escapeHtml(course.url)}">${escapeHtml(courseTitle(course))}</a>` : escapeHtml(courseTitle(course))}</div>
            ${course.organisation ? `<div class="o">${escapeHtml(course.organisation)}</div>` : ""}
            <div class="m">${escapeHtml(plainMeta(course))}</div>
        </div>`;
    }).join("");

    return `<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>My SHAREing Learning Pathway – Map</title>
<style>
body{font-family:Arial,sans-serif;margin:40px;color:#1f2937;background:#f8f9fb}h1{color:#421456}
.legend{display:flex;gap:24px;align-items:center;font-size:.85rem;color:#475569}.legend span{display:inline-flex;align-items:center;gap:8px}
.wrap{position:relative;width:${W}px;height:${H}px;margin-top:20px}.wrap svg{position:absolute;left:0;top:0;overflow:visible;pointer-events:none}
.card{position:absolute;box-sizing:border-box;padding:14px 16px;border:1px solid #d8dee6;border-radius:12px;background:#fff;box-shadow:0 4px 12px rgba(31,41,55,.08)}
.t{font-weight:700;font-size:.9rem;color:#1f2937;line-height:1.35}.t a{color:inherit;text-decoration:none}.t a:hover{text-decoration:underline}
.o{margin-top:6px;font-size:.75rem;font-weight:700;color:#940594}.m{margin-top:6px;font-size:.75rem;color:#5b6472}
</style></head><body>
<h1>My Learning Pathway – Map</h1>
<div class="legend">
<span><svg width="40" height="10"><line x1="1" y1="5" x2="39" y2="5" stroke="#940594" stroke-width="2.5" stroke-linecap="round"/></svg> Required</span>
<span><svg width="40" height="10"><line x1="1" y1="5" x2="39" y2="5" stroke="#940594" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="7 5"/></svg> Optional</span>
</div>
<div class="wrap"><svg width="${W}" height="${H}">${ARROW_DEFS}${paths}</svg>${cards}</div>
</body></html>`;

}

$("download-list").addEventListener("click", function () {
    if (!pathwayIds.length) { return; }
    triggerHtmlDownload(buildListDownloadHtml(), "my-shareing-learning-pathway.html");
});

$("download-map").addEventListener("click", function () {
    if (!pathwayIds.length) { return; }
    savePathway();
    triggerHtmlDownload(buildMapDownloadHtml(), "my-shareing-learning-pathway-map.html");
});


/* ============================================================
   INITIALISE
   ============================================================ */

renderCuratedPathways();
renderChips();
renderBoard();
applySideState();
updatePathwayUI();
updateCourseStates();
updateUndoUI();
setTab(readStorage(KEYS.tab) || "catalogue");

});
</script>