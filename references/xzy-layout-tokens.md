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

## Diagrams

- Use separate cards/columns for timelines and mechanism maps.
- Arrows must stay in gutters or lanes and must not overlap text.
- If text is dense, remove arrows or use numbered steps instead.

## Images

- Total visuals: at least 5 per publishable article.
- Use official/source visual + deterministic data card + timeline/mechanism card + reader/workflow card + hero/context image.
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
