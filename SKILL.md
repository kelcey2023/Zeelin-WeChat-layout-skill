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
- optional WeChat operating loops that learn from metrics, comments, topic ledgers, and user feedback without auto-publishing.

Use this skill together with `wechat-article-proofreader`, `writing-humanizer`, `xiaohu-wechat-format`, `documents`, and `imagegen` when relevant.

When the user asks for 爆款、公号风格、学习新智元/量子位, or higher-flow AI tech writing, read `references/xzy-qbitai-high-traffic-patterns.md` before drafting and apply its structure rules.

When the user provides a high-performing article/card example, says previous graphics were poor, or the topic is based on research, education, reports, scores, distributions, before/after data, or "study finds" claims, read `references/research-card-visual-standard.md` before title writing and visual planning.

## Non-Negotiable Rules

1. Browse before writing any current news article. Use official pages, company blogs, filings, regulator pages, research reports, and primary posts first; use reputable media second.
2. Build an internal fact ledger before drafting. Every date, number, valuation, lawsuit, policy, product claim, quote, executive change, release date, view count, ranking, and benchmark must have a source URL and date, or be softened/removed.
3. Every final article must include at least 5 visuals. At least 1 visual must be an official/source visual: official webpage screenshot, company blog image, regulator/research report screenshot, product page image, official press image, or source document excerpt.
4. Do not make all visuals text cards. Text cards may support facts, timelines, and logic, but each article needs a real official/source image that anchors the story.
5. First image must not be dark. Prefer a clean official/source image or light editorial hero. If the official page is dark, wrap it in a light frame or use it after the first image.
6. Do not put process notes, diagram labels, audience labels, or workflow reminders into public text or images. Never output phrases like `素材卡`, `配图建议`, `时间线：节点分开排布`, `链路图：`, `判断图：`, `影响卡：`, `原创信息图：`, `核心事实`, `箭头不要挡住字体`, `把新闻落到用户和职场人的具体判断`, `image2提示词`, `Digg公开索引`, `原稿主线`, `核查中`, `后台`, `用户提供`, `这条新闻`, `这条硅谷新闻`, `落到中国读者`, or `读者`.
7. Do not write generic scaffolding headings: `事件先摆出`, `这场争议看三件事`, `普通人该看懂什么`, `普通人该怎么判断`, `盯三个结果就够了`, `这说明了什么`, `真正值得关注的是`, `说白了`, `一句话总结`.
8. Do not inflate uncertain claims. Viral screenshots, comments, social posts, and anonymous reports are not confirmed facts unless backed by official or reputable sources.
9. Do not add irrelevant images or decorative filler. Every visual must support the exact section where it appears.
10. The final `事实来源` section must be unnumbered. Do not output `05 事实来源` or similar.
11. Delete narrator padding that does not add facts or instructions. Do not publish phrases like `这意味着，读者上手前`, `读者上手前先别急着`, `这段说明很重要`, `最后记住一个原则`, `真正复用时`, `现在能确认的是`, `两个数字最抓眼`, `这个数字要谨慎读`, `这件事的另一半`, `这两天的信息流很吵`, `每一条都能写成冲突很强的科技新闻`, `对公众号作者、品牌运营和知识工作者来说`, `还有一条更贴身的变化`, `AI 正在改变网络文字的平均口气`, `这个案例最容易被讲成`, `案例已经给出边界`, `把收入结构拆开`, `先把账拆开`, `故事就没那么简单`, `才有长期价值`, or similar throat-clearing.
12. WeChat HTML body prose must use `font-size:16px`. This is a hard publishing rule for all正文段落; only captions, metadata, footnotes, source notes, and small UI labels may be smaller.
13. Final deliverable files must be named by the article title. Use the sanitized H1 title as the filename stem for Markdown, Word/DOCX, and standalone HTML exports; do not deliver main files named `article.md`, `article.docx`, `draft.docx`, or generic batch names.
14. If the user asks to write a WeChat public-account article and does not name an output folder, create a Desktop folder named with the current local date plus `公众号`, such as `2026-06-25公众号`, and put all article outputs there. All WeChat articles written on the same local date must reuse that one dated folder; do not create separate date folders per article, topic, or batch.
15. WeChat operating loops are read/analyze/draft by default. Never publish, delete drafts, change account settings, mass-message, pay, or perform irreversible account actions without explicit user approval.
16. Do not invent backend metrics. If WeChat analytics exports, screenshots, or article URLs are unavailable, run a qualitative review and mark metric conclusions as unavailable.
17. For research, education, report, score, distribution, before/after, and study-based articles, the main deterministic support visual must be a research card: 1080 px wide, mobile-safe, evidence-led, with a strong thesis headline, chart/key-number block, and source line. Do not use a generic flow chart as the main evidence image.


## High-Spread Reference Layer

Use `references/xzy-qbitai-high-traffic-patterns.md` as the style calibration layer for AI/tech public-account work. Apply the patterns as structure, not imitation:

- Borrow New智元's high-stakes collision, named actors, fast first-screen tension, and screenshot density.
- Borrow 量子位's concrete scene, test/payment/order/data entry point, and business/workflow consequence.
- Do not copy their identity markers, author labels, house slogans, or unsupported heat words.
- Keep Zeelin's fact ledger stricter than the reference outlets: every title number, product claim, ranking, and quote needs a source or must be softened.
- Public text must never expose this calibration process or mention that it is learning from another account.

A publishable Zeelin article should pass this shape check:

1. Title: recognizable entity + sourced number or role shift + visible action/conflict.
2. First 120 Chinese characters: actor, event, tension, changed decision.
3. Body: scene -> mechanism -> consequence -> boundary.
4. Visuals: source proof first, then data/mechanism/workflow cards.
5. Ending: cost, workflow, job, buying, learning, compliance, or product-choice implication.

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
- If the user references an external workflow, thread, X Article, tweet, newsletter, or long post, first extract the actual text or screenshot. If the page is inaccessible, say so and ask for pasted text or screenshots instead of inventing the workflow.

### 1.5 Production Loop

Use this loop for every article:

1. `Source`: collect official/reputable sources and note dates before drafting.
2. `Angle`: compress the article into one concrete sentence: event + affected reader + changed decision.
3. `Title`: generate 5-10 titles using the Title Engineering rules below. Include three lanes internally: Collision lane, Utility lane, and Decision lane. Pick one with a real subject, a sourced anchor, a visible conflict, and no exaggerated claim.
4. `Skeleton`: draft around event, mechanism, user/workflow consequence, and action/checklist.
5. `Visuals`: assign at least 5 visuals to specific sections before creating Word/HTML.
   - For research/data/education/report topics, assign one `research_card` visual before ordinary data cards or mechanism cards.
6. `Anti-fluff pass`: delete narrator padding, editor notes, vague transition sentences, and any line that can be removed without losing facts or instructions.
7. `QA`: run source, banned phrase, image count, official image, and layout checks.


### 1.6 WeChat Operating Evolution Loop

Use `references/wechat-loop-evolution.md` whenever the user asks for self-learning, self-evolution, operations, account data analysis, article review, title/cover experiments, follower growth, or recurring public-account production.

Default loop:

1. Import evidence: WeChat backend exports/screenshots, article files, comments, topic lists, source links, and prior outputs.
2. Update state: record goal, last run, unresolved questions, next action, and stop conditions in `ops/WECHAT_LOOP_STATE.md` when the user wants ongoing operation.
3. Analyze performance: group comparable articles by topic type, title pattern, cover style, first-screen structure, publish time, and available metrics.
4. Propose one experiment: change only one main variable per batch, such as title, cover, opening, topic angle, publish time, article length, or visual density.
5. Produce drafts: apply the normal Zeelin article workflow and QA gates.
6. Observe results: after data arrives, compare against a like-for-like baseline and record the result in `ops/experiment_log.md`.
7. Evolve cautiously: update this skill only after repeated evidence, explicit user preference, or recurring QA failure. Do not change rules from one isolated article.

Self-evolution guardrail:

- The loop may propose skill changes, but the user approves them.
- Use Maker / Checker / Operator roles: Maker drafts, Checker audits, Operator interprets performance data, Human approves publishing and skill changes.
- Keep external account actions manual unless the user explicitly approves the exact action.

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

- Put the event first, with a date or source when available. The first 120 Chinese characters should include actor, event, tension, and changed decision.
- First screen should show conflict and reader relevance.
- Avoid long throat-clearing and avoid explaining why the article is worth reading.


Title Engineering:

- For AI/technology news, aim the final title at 28-38 visible characters, with roughly 32 as the center. Avoid titles under 24 characters unless the event itself is already famous.
- Use one natural rhythm separator. Chinese exclamation, comma, colon, and question marks are the common separators; do not stack punctuation or force clickbait.
- Prefer one verified number when available: date, price, valuation, token count, users, percentage, ranking, model version, round size, or affected scale. Never invent numbers just to satisfy the pattern.
- Keep canonical English names for AI models, companies, products, or labs when they are the recognition hook, such as `OpenAI`, `Claude`, `Gemini`, `Cursor`, `xAI`, `SpaceX`, `Meta`, or `DeepMind`. Do not translate them away if the English name carries search value.
- Default title formula: `entity / number / fresh timing` + `action or conflict` + `consequence / ranking / concrete affected group`. Use concrete groups such as users, developers, parents, workers, creators, founders, teachers, doctors, or teams; do not use vague audience labels in public copy.
- Generate titles in three lanes before choosing: fact-forward, conflict-forward, and utility-forward. Pick the one with the clearest subject, a sourced anchor, and a consequence that the article actually explains.
- Use urgent timing words only for truly fresh events or source posts within the current news window. If timing is uncertain, use the date or remove the urgency word.

Structure:

- Title: concrete event plus tension. For tutorial articles, use benefit-first titles such as "you do X once, the tool can do Y next time"; do not promise full automation when the source only supports assisted execution.
- Lead box: 2-3 concise lines and must appear immediately after the H1 title in Markdown.
- Do not put subtitle, metadata, author line, image, blank prose, or any ordinary text between the title and the lead box. This preserves xiaohu callout spacing and prevents the lead from becoming normal body text.
- Subtitle or metadata, if needed, should be folded into the lead box or placed after the lead box.
- Sections: numbered `01`, `02`, `03` with event-specific headings.
- Closing: return to concrete user/workplace/product decisions.
- Final heading: `事实来源`.

Style:

- Use compact mobile-friendly paragraphs.
- Prefer concrete nouns, dates, products, companies, and scenarios.
- Lower the fire on risky claims: use `据媒体报道`, `公开信息显示`, `可能`, `更像是`, `尚未确认` where appropriate.
- Do not overuse colons, slogans, one-sentence paragraphs, or forced rule-of-three structures.
- Replace empty transitions with direct instructions or facts. Bad: `这意味着，读者上手前先别急着找按钮。` Better: `先确认 Mac 版应用、版本和 Computer Use 权限。`
- For uncertain numbers, do not write generic warnings like `这个数字要谨慎读`; state the exact source, scope, denominator, time window, or remove the number.
- If a paragraph starts with `这意味着`, `这说明`, `真正`, `最后记住`, or `值得注意`, rewrite it so the sentence starts with the actor, product, date, or action.
- Do not open with generic media-environment chatter, trend-summary throat-clearing, or topic-shopping prose. Start from the exact article subject: company, product, policy, paper, report, release, lawsuit, price, date, user action, or workflow change.
- Do not explain the writing angle from outside the story. Avoid editor-like case commentary such as `这个案例最容易被讲成...`, `把收入结构拆开...`, `案例已经给出边界...`, or `先把账拆开`. State the verified event, the source, the numbers, and the concrete risk directly.

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
- Public captions may be omitted. If a caption is needed, make it content-specific; never expose diagram-role labels, QA wording, production notes, or audience labels such as `链路图`, `判断图`, `原创信息图`, `核心事实`, or `读者`.

Research-card rules:

- Use `references/research-card-visual-standard.md` for study/report/data/education pieces.
- Prefer 1080x1350 to 1080x1700 vertical cards with a warm paper background, black editorial headline, muted rose/sage/blue data colors, and clear source line.
- Build charts and Chinese text deterministically with code or vector layout. Do not rely on image generation for Chinese labels, axes, source notes, or dense text.
- The image should answer "what did the evidence prove?" at a glance. If it only decorates the article, rebuild it.
- Check at phone width: no right-edge clipping, no overlapping text, no tiny axes, no long URLs in the public body.

### 5. Output Formats

### 5.0 File Naming

Default output folder:

- If the user gives an explicit output folder, use that folder.
- If the user only says `写公众号`, `输出到桌面`, `放在桌面`, or does not specify a folder, create `C:\Users\<current-user>\Desktop\YYYY-MM-DD公众号` using the current local date.
- For batch writing, put the whole batch in that one dated folder. For same-day follow-up requests, reuse the existing `YYYY-MM-DD公众号` Desktop folder instead of creating a second folder. Each article may have its own support subfolder, but the main Word/DOCX and HTML files must still be named by the article title.
- Do not scatter outputs across Desktop, `outputs/`, and temporary folders unless a tool requires temporary files; copy the final publishable files back into the dated Desktop folder.

All main deliverables must use the final H1 title as their filename stem:

- Markdown: `文章标题.md`
- Word/DOCX: `文章标题.docx`
- Standalone HTML or xiaohu copy page: `文章标题.html`

Sanitize only characters illegal in Windows filenames (`<>:"/\|?*`) and trim trailing spaces or periods. Keep Chinese punctuation and meaningful title wording whenever possible. Support folders may be numbered for sorting, but the publishable files inside must still be title-named.

For Word/DOCX:

- Output to the requested folder or Desktop.
- Use Microsoft YaHei or another readable Chinese font.
- Body paragraphs use first-line indent when the user asks for formal WeChat-style prose.
- Include official/source image and 5+ total visuals.
- Include unnumbered `事实来源` with source names, dates, and URLs.

For xiaohu WeChat HTML:

1. Run punctuation repair first:
   `python C:/Users/76518/.codex/skills/xiaohu-wechat-format/scripts/zh_punctuation_fix.py "article.md" --write`
2. Run xiaohu formatter, usually with `--theme newspaper --font-size 16` unless user asks otherwise.
3. Post-process HTML body paragraphs to add `text-indent:2em` when the user asks for first-line indent.
4. Ensure WeChat HTML body paragraphs use `font-size:16px`; do not leave body prose at 14px, 15px, or mixed sizes unless it is captions, metadata, footnotes, source notes, or intentional small UI text.
5. Verify copied hidden HTML area also contains the same indentation and `font-size:16px` body text.

### 6. Final QA Gate

Before delivery, all of these must pass:

- `wechat-article-proofreader/scripts/check_public_article.py "article.md" --expect-sources`
- `Zeelin-WeChat-layout-skill/scripts/check_xzy_article.py "article.md"`
- Manual fact pass: data, dates, cases, sources, and official/source visuals checked.
- No banned scaffolding, process notes, visible prompts, or irrelevant images.
- At least 5 visuals and at least 1 official/source visual.
- First image is not dark.
- Logic arrows do not cover text.
- Research/data visuals are evidence-led cards, not generic workflow boxes; no chart or visual element is clipped in WeChat draft view.
- Source section unnumbered.
- Main Markdown, DOCX, and HTML filenames use the sanitized final H1 title, not generic names.
- Word and HTML outputs match the same final article.
- If a WeChat operating loop is used, metrics and conclusions are backed by provided data, screenshots, exports, or marked unavailable.
- Markdown title is followed immediately by the lead box; no subtitle, metadata, image, or plain paragraph sits between them.

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
