# GCSE Lessons — Site Improvement Brief (for AI agent)

**Site live:** https://scottrix.github.io/gcselessons
**Canonical repo:** `/home/scott/src/gcselessons`
**Mirror repo (must apply same edits):** `/home/scott/src/github/gcselessons`
**Date of audit:** 2026-09-28
**Goal:** Best UK GCSE homeschool lesson resource. LESSONS not revision: teach from scratch in 50 minutes. Parent (non-teacher) must be able to deliver with zero prep beyond reading the page. Every lesson needs filled teaching script, plenty of worked examples with full steps, guided + independent practice, checks for understanding, misconceptions, support/stretch differentiation, materials, timings, homework, assessment. Compare against Oak Academy / BBC Bitesize lessons / Seneca / savemyexams smart lessons — but structured as parent-delivered 50-min plans.

---

## 1. Current state (verified)

- `subjects.json`: 37 subjects, boards metadata only (`{id, name, category, boards[], papers?, practical?}`). **No `topics[]`, no `topicDirs`.** Filesystem is source of truth.
- `topics/`: **1,712 files in 273 unit dirs**, organised by TEACHING UNIT not board (e.g. `topics/cell-biology/B1…B5`, `topics/number/N1…`, `topics/infection/…`, `topics/engineering-general/…`). Board-agnostic by design — no board subdirs (contrast gcserevise `topics/{subject}/{board}/…`).
- Homepage claims "37 Subjects / 5 Exam Boards / 50 min Per Lesson". No topic count claimed (good — avoids the gcserevise/alevelrevise count problem).
- Page size ~1,000–2,300 words incl. boilerplate → roughly **700–1,500 real words** per lesson. Estimated total ~3.1M words. Thinner than gcserevise topics (~2,000) — expected for lessons, but placeholders eat much of it (see P0-1).
- Lesson template (verified `topics/cell-biology/B2-cell-division.html`): Lesson Overview → Learning Objectives → Prerequisites → Materials & Equipment → Lesson 1 Intro → Lesson 2 Core Concepts → Lesson 3 Application → Lesson 4 Exam Practice (each "50 minutes" — actually 4 lessons per file, not 1; homepage "50 min per lesson" refers to each sub-lesson) → Homework & Consolidation → Recommended Resources → Smart Lesson container. Each sub-lesson: starter (5 min), main with parent/teacher guide + timed teaching script, plenary. Template elements (objectives/prereqs/stretch/plenary/homework) present in 8/8 sample.
- `smart-lessons/`: **1,722 JSON** ≈ 1:1 with topics — good interactive coverage.
- Subject pages link well statically (`biology.html` 54, `mathematics.html` 123, `french.html` 43 topic links). Zero broken internal hrefs in root sample. No generic-revision placeholders.
- `images/` contains only 3 affiliate assets (FM banner, dynadot, amazon). All 1,712 topic `<img>` hits are affiliate banners. **Zero inline SVG diagrams.**

## 2. Defects to fix (prioritised)

### P0-1. Unfilled teaching-script placeholders in ~799 files (the big one)
- `grep -rl "\[specific outcome\]\|\[prior topic\]\|\[bolded terms\]\|See Troubleshooting below" topics | wc -l` → **799**.
- Examples from live pages: `Teaching Script: Mins 0-5 - Hook: "Today: Cell Division. Goal: [specific outcome]. Connects to [prior topic] because [link]."` / `Pre-teach key vocab: [bolded terms]. If stuck: See Troubleshooting below.` / `Real example: "Like [everyday example]..."` / `Key principle: "Most important:..."`.
- A parent cannot teach from brackets. This fails the site's core promise.
- **Task:** Fill EVERY bracket sitewide with topic-specific text. Hook: concrete everyday anchor. Goal: measurable outcome ("By the end you can…"). Prior-topic link: named topic + why it matters. Vocab: 4–8 bolded terms defined in-line. Troubleshooting: 2–3 stuck-points with recovery steps. Everyday example: real, age-appropriate. Acceptance: `grep -rn "\[specific outcome\]\|\[prior topic\]\|\[bolded terms\]\|\[everyday example\]\|Most important:\.\.\." topics` → 0 hits; spot-check 20 files read as deliverable scripts.

### P0-2. No diagrams — "Draw diagram, label live" with nothing to copy
- Lessons tell the parent to draw/label live but provide no reference figure, steps, or labels. 0 SVG, 0 content images sitewide.
- **Task:** For every lesson needing a visual (all sciences, geography, maths geometry/graphs, D&T, engineering, music, PE anatomy): add stepped draw-along box (numbered strokes + labels to add at each step) AND/OR inline SVG reference figure the parent can display. Acceptance: every science/maths/geography lesson has ≥1 figure or draw-along; validator-clean SVG.

### P0-3. Weak examiner layer (sampled 300 files)
- `misconception` 142/300 (half missing), `mark scheme` 46/300, `examiner` 23/300, `common mistake` 6/300, `required practical` 2/300, `working scientifically` 0, `success criteria` 0. `key vocab` 300/300 (good).
- B2 sample: 29× "example" but 0 misconception/examiner/mark-scheme strings; "grade 8" ×4 with no grade-5 floor; tier mentioned once.
- **Task:** Every lesson gets: 2–4 named misconceptions with correction script ("If pupil says X, respond…"), examiner tips (command words, AO1/AO2/AO3, timing, tier notes Foundation vs Higher), success criteria checklist, mark-scheme-referenced answers for Exam Practice. Sciences: required-practical box where spec demands (numbers per board) + working-scientifically skills. Acceptance: 300-file resample → misconception ≥270, mark scheme ≥270, examiner ≥200, required-practical present on all science practical lessons.

### P0-4. Board-agnostic with no board callouts
- Lessons never vary by board; subject pages have no board selector (verified `biology.html` 0 hits). Homepage still advertises 5 exam boards. Board differences (papers, practicals, equations sheet vs memorise, set texts, options) live only in gcserevise.
- **Task:** Add "Board notes" box to every lesson (which boards examine this, paper numbers, tier, anything omitted per board). Do NOT fork files per board — one lesson + callouts. Cross-link each lesson to matching gcserevise topic(s) for revision follow-up. Acceptance: every lesson has board-notes box with ≥2 boards named; cross-links resolve.

### P0-5. Search + sitemap gaps, missing robots/canonical (same family bug)
- `search-index.json`: 37 subjects, **1,150 topics** vs 1,712 files. `sitemap.xml`: **838 URLs** vs 1,712 + ~40 roots → ~900 lessons unindexed. No `robots.txt`. Canonicals point at `https://www.scottrix.co.uk/gcselessons/…`, live is `https://scottrix.github.io/gcselessons`.
- **Task:** Regen search + sitemap from filesystem; add `robots.txt` (Allow + Sitemap line); decide single canonical domain and apply to all pages/og/sitemap/JSON-LD. Acceptance: counts match filesystem; `robots.txt` present.

## 3. Lesson-quality standard (apply to every file)

Deliverable 50-min sub-lesson = hook (concrete) → direct instruction (filled script, key vocab bolded + defined) → ≥3 worked examples with FULL steps (maths/science: every line; humanities: paragraph frames + sentence starters; languages: model sentences + manipulation) → guided practice with answers → CFU checks (hinge questions with expected answers) → independent task (differentiated: support scaffold vs stretch challenge) → plenary (exit ticket) → homework (15–30 min, marked criteria). Materials list must be shoppable-from-home (paper, ruler, household items) + printables named where needed. Timings must sum to 50 per sub-lesson. Thin files first: astronomy/geology general (~980–1,010 words) then outward.

## 4. Per-area priorities
| Priority | Area | Action |
|---|---|---|
| P1 | Sciences + Maths (cell-biology, infection, bioenergetics, atomic-structure, energy, number, algebra) | Fill P0-1→P0-3; draw-alongs for cells, circuits, energy stores, graphs; required practicals; tier tags |
| P2 | English (language Paper 1/2 methods, literature set-text lessons), MFL (photo-card + 90/150-word technique + grammar drills with answers) | Worked paragraphs/translations step-by-step, not just reminders |
| P3 | Humanities/creative/technical (history sources, geography fieldwork + case studies, music set works listening guides, D&T/food practical safety, PE demos, art process photos described) | Hands-on sections a parent can supervise safely |
| P4 | Single-board specials (astronomy, geology, ancient history, law, dance, film, electronics) | State board + spec codes up front; exam-technique lessons per spec |

## 5. Sources (not just savemyexams)
Official specs + specimen mark schemes (AQA/Edexcel/OCR/Eduqas/CCEA); Oak Academy + BBC Bitesize lessons (pedagogy reference); Seneca; savemyexams smart lessons; PMT; mathsgenie/Dr Frost; tutor2u; set-text editions. Never copy — synthesise, cite spec codes.

## 6. Execution order
1. P0-1 placeholder fill (largest trust repair; script-assist then human-read 20-file spot check).
2. P0-2 figures/draw-alongs for sciences/maths/geography.
3. P0-3 examiner/misconception/practical layer.
4. P0-4 board boxes + gcserevise cross-links.
5. P0-5 search/sitemap/robots/canonical.
6. P1→P4 area passes + QA.
7. Mirror every edit to `/home/scott/src/github/gcselessons`.

## 7. Reproduce-audit commands
```
cd /home/scott/src/gcselessons
find topics -type f | wc -l; ls topics | wc -l
grep -rl "\[specific outcome\]\|\[prior topic\]\|\[bolded terms\]\|See Troubleshooting below" topics | wc -l
grep -rl "<svg" topics | wc -l; grep -rl "<img" topics | wc -l
python3 -c "import json;d=json.load(open('search-index.json'));print(len(d['subjects']),len(d['topics']))"
python3 -c "import re;print(len(re.findall(r'<loc>',open('sitemap.xml').read())))"
ls smart-lessons | wc -l; ls images -R | head
```

## 8. Acceptance criteria
- [ ] Zero bracket placeholders (`[specific outcome]` etc.) sitewide.
- [ ] Every visual lesson has figure/draw-along; 0 SVG→present where needed.
- [ ] Misconceptions + examiner + mark-scheme coverage per §2 P0-3.
- [ ] Board-notes box + gcserevise cross-links on every lesson.
- [ ] search/sitemap == filesystem; robots.txt present; single canonical domain.
- [ ] Both repo copies identical for changed files.
