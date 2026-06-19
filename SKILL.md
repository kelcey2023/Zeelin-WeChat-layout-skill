---
name: Zeelin-WeChat-layout-skill
description: Use when creating Zeelin-style Chinese WeChat public-account articles from AI, technology, business, policy, product, workplace, or internet news topics, screenshots, PDFs, DOCX drafts, folders of images, or brief topic notes; especially when the user asks for 选题, 爆款公众号, 配图, 官方配图, xiaohu 排版, Word, HTML, or 发公众号.
---

# Zeelin WeChat Layout Skill

## Core Job

Produce ready-to-publish Chinese WeChat public-account articles for「清新研究」style output. This skill covers the full chain:

- topic selection and angle refinement;
- source search and fact ledger;
- article writing around 2000 Chinese characters;
- official/source visuals plus generated or deterministic support visuals;
- Word/DOCX output and xiaohu WeChat HTML layout;
- final QA for facts, data, cases, AI tone, banned phrases, image relevance, and copy-ready formatting.

Use this skill together with `wechat-article-proofreader`, `writing-humanizer`, `xiaohu-wechat-format`, `documents`, and `imagegen` when relevant.

## Non-Negotiable Rules

1. Browse before writing any current news article. Use official pages, company blogs, filings, regulator pages, research reports, and primary posts first; use reputable media second.
2. Build an internal fact ledger before drafting. Every date, number, valuation, lawsuit, policy, product claim, quote, executive change, release date, view count, ranking, and benchmark must have a source URL and date, or be softened/removed.
3. Every final article must include at least 5 visuals. At least 1 visual must be an official/source visual: official webpage screenshot, company blog image, regulator/research report screenshot, product page image, official press image, or source document excerpt.
4. Do not make all visuals text cards. Text cards may support facts, timelines, and logic, but each article needs a real official/source image that anchors the story.
5. First image must not be dark. Prefer a clean official/source image or light editorial hero. If the official page is dark, wrap it in a light frame or use it after the first image.
6. Do not put process notes into public text or images. Never output phrases like `素材卡`, `配图建议`, `时间线：节点分开排布`, `影响卡：`, `箭头不要挡住字体`, `把新闻落到用户和职场人的具体判断`, `image2提示词`, `Digg公开索引`, `原稿主线`, `核查中`, `后台`, or `用户提供`.
7. Do not write generic scaffolding headings: `事件先摆出`, `这场争议看三件事`, `普通人该看懂什么`, `普通人该怎么判断`, `盯三个结果就够了`, `这说明了什么`, `真正值得关注的是`, `说白了`, `一句话总结`.
8. Do not inflate uncertain claims. Viral screenshots, comments, social posts, and anonymous reports are not confirmed facts unless backed by official or reputable sources.
9. Do not add irrelevant images or decorative filler. Every visual must support the exact section where it appears.
10. The final `事实来源` section must be unnumbered. Do not output `05 事实来源` or similar.

## Topic Selection

When the user provides multiple topics, rank them by:

- event freshness and concrete trigger;
- named company/person/product/policy;
- verifiable data or official document;
- reader impact on tools, jobs, money, workflow, compliance, creators, or product choice;
- conflict that can be explained without exaggeration.

Reject or soften topics that rely mainly on rumors, unsourced valuations, fake IPO/acquisition claims, unverifiable view counts, or screenshots without source links.

A good Zeelin angle should answer:

- What exactly happened?
- Who is affected?
- Which workflow, cost, product, job, or decision changes?
- What should a user, creator, manager, developer, or buyer do differently?

Do not announce these questions as section titles. Use concrete titles tied to the event.

## Required Workflow

### 1. Extract Inputs

- For pasted text, screenshots, PDFs, DOCX, folders, or images, identify the event, date, company/person, key claim, source hints, and user audience.
- Remove placeholder text, prompt text, material cards, irrelevant comments, and source-scoring notes from public prose.
- If using user screenshots, treat them as clues, not final visuals, when they contain watermarks, app UI overlays, or cropped unreadable text.

### 2. Search And Fact Ledger

Before writing, collect sources:

- at least 2 high-quality sources for ordinary articles;
- at least 1 official/primary source whenever a product, policy, report, lawsuit, funding, acquisition, or release is discussed;
- source dates for every item in `事实来源`.

Create an internal ledger with four columns:

- claim;
- source URL and date;
- confidence: official / reputable media / reported / uncertain;
- action: keep / soften / remove.

If sources conflict, name the conflict in prose only when it matters; otherwise remove the disputed claim.

### 3. Write The Article

Default target: 1800-2300 Chinese characters for main body, excluding source links and captions. Around 2000 characters is ideal.

Opening requirements:

- Put the event first, with a date or source when available.
- First screen should show conflict and reader relevance.
- Avoid long throat-clearing and avoid explaining why the article is worth reading.

Structure:

- Title: concrete event plus tension.
- Subtitle: one line explaining the impact.
- Metadata: `清新研究 | AI观察 | YYYY.MM` or similar.
- Lead box: 2-3 concise lines.
- Sections: numbered `01`, `02`, `03` with event-specific headings.
- Closing: return to concrete user/workplace/product decisions.
- Final heading: `事实来源`.

Style:

- Use compact mobile-friendly paragraphs.
- Prefer concrete nouns, dates, products, companies, and scenarios.
- Lower the fire on risky claims: use `据媒体报道`, `公开信息显示`, `可能`, `更像是`, `尚未确认` where appropriate.
- Do not overuse colons, slogans, one-sentence paragraphs, or forced rule-of-three structures.

### 4. Visual System

Each article must contain at least 5 visuals:

1. official/source visual: screenshot or asset from official page, research report, regulator page, filing, product page, or source article;
2. light hero image or official visual framed on light background;
3. fact/data card with 3 verified facts;
4. timeline or mechanism diagram;
5. reader/workflow impact card or product/context image.

Official/source visual rules:

- Save as `images/official_source.png` or another obvious official/source filename.
- In Markdown alt text, include `官方配图` or `官方来源截图`.
- Do not crop out the source identity if it helps verification.
- Do not use unreadable screenshots; if needed, frame and enlarge the relevant area.
- For copyrighted media screenshots, use only a small, contextual screenshot for commentary/reference, not a full article reproduction.

Generated image rules:

- Use `imagegen` for editorial visuals when needed, but not for exact Chinese text.
- Do not ask image generation to render dense Chinese labels. Use PIL/deterministic cards for text-heavy visuals.
- No logos unless sourced from official assets or necessary in an official screenshot.
- No irrelevant decoration.

Logic diagram rules:

- Arrows must be in gutters or separate lanes, never over text.
- Use separated cards/columns when unsure.
- Inspect output before delivery; if text overlaps or arrows block labels, regenerate or simplify.

### 5. Output Formats

For Word/DOCX:

- Output to the requested folder or Desktop.
- Use Microsoft YaHei or another readable Chinese font.
- Body paragraphs use first-line indent when the user asks for formal WeChat-style prose.
- Include official/source image and 5+ total visuals.
- Include unnumbered `事实来源` with source names, dates, and URLs.

For xiaohu WeChat HTML:

1. Run punctuation repair first:
   `python C:/Users/76518/.codex/skills/xiaohu-wechat-format/scripts/zh_punctuation_fix.py "article.md" --write`
2. Run xiaohu formatter, usually with `--theme newspaper` unless user asks otherwise.
3. Post-process HTML body paragraphs to add `text-indent:2em` when the user asks for first-line indent.
4. Verify copied hidden HTML area also contains the same indentation.

### 6. Final QA Gate

Before delivery, all of these must pass:

- `wechat-article-proofreader/scripts/check_public_article.py "article.md" --expect-sources`
- `Zeelin-WeChat-layout-skill/scripts/check_xzy_article.py "article.md"`
- Manual fact pass: data, dates, cases, sources, and official/source visuals checked.
- No banned scaffolding, process notes, visible prompts, or irrelevant images.
- At least 5 visuals and at least 1 official/source visual.
- First image is not dark.
- Logic arrows do not cover text.
- Source section unnumbered.
- Word and HTML outputs match the same final article.

If any check fails, fix and rerun. Do not call the article finished because it is “close enough”.

## GitHub Packaging

When the user asks to save or upload this Skill:

- Package the Skill folder with `SKILL.md`, `references/`, and `scripts/`.
- Do not include generated articles, desktop outputs, browser caches, screenshots, or pycache.
- Commit only Skill files.
- If a GitHub remote exists, push the branch.
- If no remote exists and `gh` is unavailable, ask the user for a repository URL or GitHub CLI login before claiming upload is complete.

## Final Response Standard

Return:

- final file/folder path;
- whether official/source visuals are included;
- QA result;
- GitHub push status or exact blocker.

Keep the response concise.
