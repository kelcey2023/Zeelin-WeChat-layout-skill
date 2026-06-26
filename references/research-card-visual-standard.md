# Zeelin Research Card Visual Standard

Use this when the user provides a successful article/image example, says previous graphics are poor, or the topic is driven by studies, education, reports, scores, distributions, before/after changes, AI usage effects, or measurable public consequences.

## Benchmark

The target is a shareable WeChat research card, not a decorative illustration.

The quality bar is like the user-provided example:

- Thesis title: `AI正在制造一种“假优秀”学生`, not `AI学习影响分析`.
- Scene hook: `AI帮你写作业，谁帮你考试？`, not a paper-summary opening.
- Evidence image: trend chart, distribution chart, before/after comparison, grouped metrics, source line.
- Visual mood: warm paper background, large black Chinese headline, restrained rose/sage/blue data colors, serif-like editorial feeling, readable charts.

Do not copy the exact image, brand mark, chart, or wording. Learn the structure and standard.

## Title Formula

Research/data articles need scene + reversal + consequence:

1. Scene: homework, exam, phone call,副业,求职,家长,打工人,创作者.
2. Reversal: 表面变轻松，实际丢能力；表面能赚钱，实际先交钱；表面更高效，实际更不可信.
3. Consequence: 家长误判, 学生能力空心化, 普通人被课程收割, 白领被流程重估.

Use formulas like:

- `AI帮你[轻松完成X]，谁帮你[真正过Y]？`
- `AI正在制造一种“[表面好处]”的人`
- `[人群]看起来赢了，真正丢掉的是[能力/信任/判断力]`
- `不是不能用AI，而是不能把[核心能力]外包`
- `[数字/研究]之后，最该紧张的不是[表面对象]`

Reject topic-name titles, report headings, and broad summaries.

## Article Rhythm

1. Scene hook: everyday moment readers recognize.
2. Research punch: sample size, time span, metric, headline result.
3. Mechanism: daily behavior that explains the result.
4. Split groups: who is harmed, who benefits, and what behavior separates them.
5. Local consequence: why Chinese parents, workers, creators, or managers should care.
6. Practical boundary: what to do differently without moral panic.
7. Comment hook: one discussable question.

## Card Layout

- Canvas: 1080 px wide.
- Height: 1350-1700 px for a long card; 1080x1080 only for one simple chart.
- Safe margin: 64-88 px.
- Chinese body text: at least 30 px.
- Chart labels: at least 24 px.
- Bottom source area: 80-120 px.
- Phone test: readable at 375 px wide.

Order:

1. Big editorial thesis title.
2. Short subtitle saying what the chart shows.
3. Main evidence chart.
4. Secondary comparison, distribution, or key-number row.
5. Source line.

Never place a five-step horizontal workflow inside a narrow WeChat body. Use vertical steps or two rows.

## Palette

- Paper: `#fbf7ef`, `#f7f1e8`, warm white.
- Ink: `#171514`, `#2a2724`.
- Rose/risk/after: `#b25b63`, `#c98d93`.
- Sage/baseline/before: `#758b6a`, `#9aae90`.
- Blue/control: `#315d7d`.
- Grid/border: `#e8dfd2`.

Avoid dark tech backgrounds, neon gradients, robot heads, random 3D icons, one-note purple-blue palettes, and stock-like office scenes.

## Chart Rules

Preferred charts:

- Line chart with shaded band.
- Distribution/KDE small multiples.
- Before/after dumbbell or bar chart.
- 2-3 small multiples with one visual language.
- Evidence card with sample size, period, subjects, result, and source.

Rules:

- Never invent numeric chart data.
- If exact data is unavailable, create a qualitative mechanism diagram and label it as such.
- If only headline numbers are available, make a key-number card instead of fake axes.
- Rebuild source charts into simplified Chinese cards when rights and data allow; cite the source.
- Every chart needs a source or note.

## Generation Rule

Do not ask image generation to spell Chinese labels or draw accurate axes. Use deterministic layout tools for all Chinese text, charts, source lines, and labels. Image generation may supply only a subtle background or non-text visual texture.

Useful prompt for background only:

```text
Chinese WeChat research-card background, 1080x1500, warm off-white editorial paper, clean chart spaces, muted rose and sage accents, no logos, no real faces, no fake screenshots, no readable text, leave blank safe areas for Chinese title and source text added later.
```

## QA

Before publishing:

- No right-edge clipping.
- No text overlap.
- No tiny axes on mobile.
- No long URLs in public body.
- First inline visual carries evidence or thesis.
- Source line is factual and bounded.
- Readable at 375 px wide.

If any item fails, redraw the image. Do not call it acceptable.

## Failure Fixes

| Failure | Fix |
| --- | --- |
| Generic flow boxes for a research topic | Replace with evidence chart, distribution, or key-number card |
| Wide landscape diagram clipped in WeChat | Convert to vertical 1080-wide card or two-row layout |
| Source list breaks with full URLs | Move URLs to appendix; use short source names in body |
| Title names topic but has no tension | Rewrite with scene + reversal + consequence |
| Chart has fake precision | Use qualitative mechanism diagram or cite exact data |
| Pretty image but weak evidence | Add data/source card or remove it |
