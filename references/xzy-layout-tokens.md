# Zeelin 微信公号视觉 Tokens

Use these defaults when creating Word/DOCX and WeChat HTML outputs.

## Page And Body

- Page: A4 portrait for Word.
- Margins: top/bottom 0.66-0.75 in, left/right 0.70-0.78 in.
- Body font: Microsoft YaHei.
- Body size: 11-12.5 pt.
- Body line spacing: 1.28-1.35.
- Body color: `#1F2933`.
- WeChat HTML body paragraphs should use `text-indent:2em` when the user asks for首行缩进.
- WeChat HTML body prose font size: `16px` exactly. Captions, metadata, footnotes, source notes, and small UI labels may be smaller.

## File Naming

- Default output folder: when no explicit folder is provided, create `C:\Users\<current-user>\Desktop\YYYY-MM-DD公众号` using the current local date.
- Batch articles and same-day follow-up articles share the same dated Desktop folder; support assets may live in article subfolders.
- Do not create multiple same-date Desktop folders for different topics or batches unless the user explicitly asks for separate folders.
- Main publishable files must use the final H1 title as the filename stem.
- Required pattern: `文章标题.md`, `文章标题.docx`, and `文章标题.html`.
- Sanitize only Windows-illegal characters (`<>:"/\|?*`) and trailing spaces or periods.
- Do not deliver main files named `article.md`, `article.docx`, `draft.docx`, `output.docx`, or other generic names.


## High-Spread Title Cues

- Front-load one recognizable entity, product, person, or number.
- Prefer concrete verbs such as 发布, 推出, 接入, 付费, 融资, 上市, 登顶, 跑通, 曝光, 实测, 改写.
- One title should usually answer: who moved, what changed, why it matters.
- Do not use house-style labels from other accounts.

## Title Engineering

- Target final title length: 28-38 visible characters; 32 is the ideal center for AI tech news.
- Strong title rhythm usually uses one separator such as Chinese exclamation, comma, colon, or question mark; prefer colon or comma when the event has a clear collision.
- Prefer a verified number when available, but never fabricate one.
- Preserve canonical English model/company/product names when they carry recognition or search value.
- Default structure: `entity / number / fresh timing` + `action/conflict` + `consequence/ranking/concrete affected group`.
- Avoid vague public labels; use concrete people or roles instead.

## Title Block

- Metadata: 9.5-10 pt, muted gray or brand green.
- Title: 22-28 pt, bold, `#0B1220`.
- Subtitle: 12.5-14 pt, `#52606D`.
- First image must be light or light-framed, never a dark full-screen image.

## Official Source Visual

Every article needs at least one official/source visual.

Acceptable:

- official webpage screenshot;
- company blog product image;
- regulator or research report screenshot;
- product page visual;
- official press asset;
- source document excerpt.

Implementation:

- Save as `images/official_source.png` where possible.
- Markdown alt text should include `官方配图` or `官方来源截图`.
- Preserve enough page/source identity to make the image traceable.
- Do not use full article screenshots or large copyrighted reproductions.
- If the official page is dark, place it after the light hero or wrap it in a light frame.

## Lead Box
- Lead block must immediately follow the H1 title in Markdown; no subtitle, metadata, image, or body text may sit between title and lead.

- Fill: near-black `#111827`.
- Text: white, 11-12.5 pt.
- Content: 2-3 lines only.
- No process wording.

## Section Headings

- Format: `01 标题`.
- Number/title: dark blue or black, bold.
- Heading must name a concrete event, actor, product, conflict, or consequence.
- Do not use generic scaffolding headings.

## Data Cards

- Use 3 cards in one row for verified facts or contrasts.
- Fill: `#F2F7FF`, `#FFFFFF`, or a light theme color.
- Border: `#D9E2EC`.
- Card text must be sourced and short.
- Do not use card labels such as `素材卡`, `影响卡`, or `配图建议`.

## Research Cards

Use `research-card-visual-standard.md` for studies, education, reports, scores, distributions, before/after data, or user-provided high-performing research-card examples.

- Canvas: 1080 px wide; prefer 1350-1700 px high for long cards.
- Style: warm paper background, large black thesis title, muted rose/sage/blue data colors, visible source line.
- Content: one evidence chart, distribution, before/after comparison, or key-number block; not a generic workflow.
- Text and charts must be deterministic, not generated as bitmap text.
- Mobile QA: readable at 375 px wide, no right-edge clipping, no long URLs inside the public body.

## Diagrams

- Use separate cards/columns for timelines and mechanism maps.
- Arrows must stay in gutters or lanes and must not overlap text.
- If text is dense, remove arrows or use numbered steps instead.
- Public image captions may be omitted. Do not caption images with diagram-role labels, production notes, QA wording, or audience labels such as `链路图`, `判断图`, `原创信息图`, `核心事实`, or `读者`.

## Images

- Total visuals: at least 5 per publishable article.
- Use official/source visual + deterministic data card + timeline/mechanism card + reader/workflow card + hero/context image.
- For research/report/education/data articles, the deterministic data card should become a research card unless another sourced chart is stronger.
- Do not use irrelevant decorative images.
- Do not ask image generation to render dense Chinese text.

## Source Section

- Heading: `事实来源`.
- No numbering before source heading.
- Source entries include source name, date, and URL when available.

## Public Text Bans

Do not output these in final article, captions, images, or source notes:

- 素材卡
- 配图建议
- 建议位置
- image2提示词
- 画面内容
- 用户提供
- Digg公开索引
- 后台
- 原稿
- 核查
- 时间线：节点分开排布
- 影响卡：
- 箭头不要挡住字体
- 这句话能火
- 别误会
- 这件事不能写成
- 这意味着，读者上手前
- 读者上手前先别急着
- 这段说明很重要
- 最后记住一个原则
- 真正复用时
- 现在能确认的是
- 两个数字最抓眼
- 这个数字要谨慎读
- 这个数字要谨慎读。
- 这件事的另一半
- 这两天的信息流很吵
- 信息流很吵
- 每一条都能写成冲突很强的科技新闻
- 对公众号作者、品牌运营和知识工作者来说
- 还有一条更贴身的变化
- AI 正在改变网络文字的平均口气
- AI正在改变网络文字的平均口气
- 这个案例最容易被讲成
- 案例已经给出边界
- 给出边界
- 把收入结构拆开
- 先把账拆开
- 故事就没那么简单
- 才有长期价值
- 最容易被讲成

- 链路图：
- 判断图：
- 原创信息图：
- 核心事实
- 这条新闻
- 这条硅谷新闻
- 落到中国读者

- 读者
