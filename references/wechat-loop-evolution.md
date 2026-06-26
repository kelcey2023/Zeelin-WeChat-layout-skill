# WeChat Loop Evolution Reference

Use this reference when the user wants the public-account workflow to learn from past articles, backend data, screenshots, exported spreadsheets, comments, or recurring topic production.

## Operating Principle

Loop engineering for WeChat is not automatic publishing. It is a controlled cycle that reads evidence, proposes changes, verifies quality, records what happened, and asks for approval before any public or account-impacting action.

The loop has five moves:

1. Intent: define the narrow operating goal for this run.
2. Context: read sources, prior outputs, WeChat backend exports, screenshots, comments, topic ledgers, and existing skill rules.
3. Action: produce analysis, hypotheses, titles, covers, drafts, or revised skill suggestions inside the workspace.
4. Observation: evaluate against metrics, QA checks, source confidence, visual checks, and human feedback.
5. Adjustment: update the state file, experiment ledger, and only then suggest a small skill/process change.

## Minimum State Files

Create or reuse these files when the user asks for continuous learning or account operations:

- `ops/WECHAT_LOOP_STATE.md`: current goal, latest run, unresolved questions, next action, stop conditions.
- `ops/article_metrics.csv`: article title, publish date, topic, title pattern, cover type, reads, read rate, shares, saves, follows, comments, 24h/48h performance when available.
- `ops/topic_ledger.csv`: topic source, freshness, category, evidence strength, duplication status, final decision.
- `ops/experiment_log.md`: hypothesis, changed variable, baseline, result, decision, whether to keep or revert.
- `ops/skill_change_log.md`: every proposed skill update with evidence and approval status.

Do not invent WeChat backend metrics. If the user has not provided exports, screenshots, or accessible backend data, ask for the data or run only a qualitative review.

## Data Inputs

Acceptable inputs:

- WeChat backend screenshots or exported spreadsheets;
- article URL/title/date and visible public numbers;
- comment screenshots and selected user feedback;
- folder of previously published DOCX/HTML/Markdown;
- topic lists and source links;
- manual notes from the user.

Not allowed:

- bypassing WeChat login, scraping private backend pages without explicit user direction, auto-publishing, deleting drafts, changing account settings, mass messaging, payments, or any irreversible external action.

## Metrics To Learn From

Track only metrics that are actually available:

- exposure, reads, read rate, completion signal if provided;
- share count, save/favorite count, comment count, new follows;
- first 2h, 24h, and 48h growth when available;
- title pattern, first-image style, topic category, source type, article length, publish time;
- qualitative signals: high-quality comments, repeated objections, confusing sections, screenshot feedback.

Always compare like with like: AI policy vs AI product, tutorial vs news analysis, hot event vs evergreen guide. Do not compare one viral breaking story against a niche tutorial as proof of title quality.

## Experiment Rules

- Change one main variable per experiment: title, cover, first screen, topic angle, publish time, article length, visual density, or CTA.
- Keep a baseline for each topic category.
- Require at least 3 comparable cases before treating a pattern as a rule.
- If data is sparse, record a hypothesis instead of modifying the skill.
- Never optimize only for clicks if saves, shares, follows, or trust signals decline.

## Maker Checker Loop

Use separate roles inside the workflow:

- Maker: searches, writes, creates visuals, formats Word/HTML.
- Checker: audits facts, duplicate topics, title quality, visual relevance, public-text bans, and metric interpretation.
- Operator: summarizes backend performance and proposes one small next experiment.
- Human: approves publishing, account actions, external messages, irreversible changes, and skill updates.

## Self Evolution Gate

A workflow rule may be added to the skill only when at least one is true:

- the same failure appears in 3 or more articles;
- a metric pattern repeats across 3 or more comparable articles;
- the user explicitly gives a stable preference;
- a fact/format QA check catches a recurring production defect.

Every skill update must include:

- evidence: article links, file paths, metrics, screenshots, or user instruction;
- scope: what future articles it affects;
- rollback: what to undo if the rule hurts quality;
- approval: explicit user request or direct instruction.

## Safety And Stop Conditions

Stop and ask for human approval when:

- source facts conflict or cannot be verified;
- backend data is missing but the requested decision depends on it;
- a proposed action would publish, delete, message, change account settings, pay, or expose private data;
- the loop repeats the same failure twice;
- metrics are too sparse for a confident conclusion;
- generated content would add unverified claims, fake screenshots, or irrelevant images.

## Weekly Operating Loop

1. Import the past 7 days of article metrics and comments if available.
2. Group articles by topic type and title pattern.
3. Identify the top 3 wins and bottom 3 misses with evidence.
4. Extract one reusable lesson for topic choice, title, cover, opening, or visual strategy.
5. Propose one experiment for the next batch.
6. Update `WECHAT_LOOP_STATE.md` and `experiment_log.md`.
7. Only update the skill when the Self Evolution Gate is satisfied.

## Source Patterns Distilled

- Top GitHub loop-engineering references emphasize moving from single prompts to systems that schedule, spawn helpers, verify work, keep state, and decide when to stop.
- Practical loop kits highlight readiness checks, cost checks, run logs, state files, safety boundaries, and tool-aware patterns.
- OpenLoop-style workflows add observable state: heartbeat, progress, logs, baseline, deterministic verification, circuit breakers, and auditable reports.
- For WeChat operations, translate these into topic ledgers, article metrics, experiment logs, QA gates, and human approval for publishing.
