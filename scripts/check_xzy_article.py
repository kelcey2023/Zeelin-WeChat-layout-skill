#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

BANNED_SCAFFOLD = [
    "报道核对", "反常识", "本文分享自微信公众号", "公众号QbitAI", "量子位 | 公众号 QbitAI", "发自凹非寺", "新智元报道", "新智元导读",
    "\u4e8b\u4ef6\u5148\u6446\u51fa", "\u4e8b\u4ef6\u5148\u6446\u51fa\u6765", "\u8fd9\u573a\u4e89\u8bae\u770b\u4e09\u4ef6\u4e8b",
    "\u666e\u901a\u4eba\u8be5\u770b\u61c2\u4ec0\u4e48", "\u666e\u901a\u4eba\u8be5\u600e\u4e48\u770b", "\u666e\u901a\u4eba\u8be5\u600e\u4e48\u5224\u65ad",
    "\u666e\u901a\u4eba\u6709\u4ec0\u4e48\u5173\u7cfb", "\u76ef\u4e09\u4e2a\u7ed3\u679c\u5c31\u591f\u4e86", "\u63a5\u4e0b\u6765\u600e\u4e48\u770b",
    "\u771f\u6b63\u503c\u5f97\u5173\u6ce8\u7684\u662f", "\u8fd9\u8bf4\u660e\u4e86\u4ec0\u4e48", "\u8bf4\u767d\u4e86", "\u4e00\u53e5\u8bdd\u603b\u7ed3", "\u503c\u5f97\u4e00\u63d0\u7684\u662f",
    "这意味着，读者上手前", "读者上手前先别急着", "这段说明很重要", "最后记住一个原则", "真正复用时",
    "现在能确认的是", "两个数字最抓眼", "这个数字要谨慎读", "这个数字要谨慎读。", "这件事的另一半", "这两天的信息流很吵", "信息流很吵",
    "每一条都能写成冲突很强的科技新闻", "对公众号作者、品牌运营和知识工作者来说",
    "还有一条更贴身的变化", "AI 正在改变网络文字的平均口气", "AI正在改变网络文字的平均口气",
    "这个案例最容易被讲成", "案例已经给出边界", "给出边界", "把收入结构拆开", "先把账拆开", "故事就没那么简单", "才有长期价值", "最容易被讲成",
    '链路图：', '判断图：', '原创信息图：', '核心事实', '这条新闻', '这条硅谷新闻', '落到中国读者', '读者']
AI_FLAVOR = [
    "\u6807\u5fd7\u7740", "\u51f8\u663e", "\u91cd\u5927\u8f6c\u6298", "\u6df1\u523b\u63ed\u793a", "\u63a5\u4e0b\u6765\u6211\u4eec\u6765\u770b\u770b",
    "\u6211\u4eec\u5148\u8bf4\u7ed3\u8bba", "\u771f\u6b63\u7684\u95ee\u9898\u662f", "\u5e95\u5c42\u903b\u8f91\u662f", "\u6838\u5fc3\u672c\u8d28\u662f",
    "\u672a\u6765\u503c\u5f97\u671f\u5f85", "\u666e\u901a\u4eba\u9700\u8981\u4fdd\u6301\u5173\u6ce8", "\u65f6\u4ee3\u5df2\u7ecf\u53d8\u4e86"
]
VAGUE_AUTHORITY = ["\u4e1a\u5185\u4eba\u58eb", "\u4e13\u5bb6\u8ba4\u4e3a", "\u6709\u89c2\u70b9\u6307\u51fa", "\u5e02\u573a\u4eba\u58eb\u8ba4\u4e3a", "\u5916\u754c\u8ba4\u4e3a", "\u4e0d\u5c11\u4eba\u8ba4\u4e3a"]
OFFICIAL_IMAGE_HINTS = ["\u5b98\u65b9\u914d\u56fe", "\u5b98\u65b9\u6765\u6e90", "\u5b98\u7f51\u622a\u56fe", "\u539f\u59cb\u6765\u6e90", "official", "source", "official_source", "apple", "google", "meta", "gallup", "challenger", "wired", "sec", "ftc", "gov", "businessinsider", "deepmind"]
SOURCE_NUMBERED_RE = re.compile(r"(?m)^\s*(?:#{1,6}\s*)?(?:0?\d+|[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]+)[\.\u3001\s_-]*\u4e8b\u5b9e\u6765\u6e90\s*$")
WINDOWS_ILLEGAL = str.maketrans({
    "<": "＜", ">": "＞", ":": "：", '"': "＂", "/": "／",
    "\\": "＼", "|": "｜", "?": "？", "*": "＊",
})

def strip_sources(text: str) -> str:
    m = re.search(r"(?m)^\s*(?:#{1,6}\s*)?\u4e8b\u5b9e\u6765\u6e90\s*$", text)
    if m: return text[:m.start()]
    m = SOURCE_NUMBERED_RE.search(text)
    return text[:m.start()] if m else text

def chinese_char_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))

def read_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as zf: xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    return "\n".join([n.text or "" for n in root.findall(".//w:t", ns)])

def count_docx_images(path: Path) -> int:
    with zipfile.ZipFile(path) as zf:
        return len([n for n in zf.namelist() if n.startswith("word/media/")])

def count_markdown_images(text: str) -> int:
    return len(re.findall(r"!\[[^\]]*\]\([^)]+\)", text)) + len(re.findall(r"!\[\[[^\]]+\]\]", text)) + len(re.findall(r"<img\b", text, flags=re.I))

def has_official_image(text: str, path: Path) -> bool:
    if path.suffix.lower() == ".docx": return True
    refs = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", text)
    refs += [("", x) for x in re.findall(r"!\[\[([^\]]+)\]\]", text)]
    refs += [("", x) for x in re.findall(r"<img[^>]+src=[\"']([^\"']+)[\"']", text, flags=re.I)]
    blob = "\n".join([a + " " + s for a, s in refs]).lower()
    return any(h.lower() in blob for h in OFFICIAL_IMAGE_HINTS)



def lead_immediately_after_title(text: str) -> tuple[bool, int, str]:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.lstrip("\ufeff").startswith("# "):
            for j in range(i + 1, len(lines)):
                stripped = lines[j].strip()
                if not stripped:
                    continue
                ok = (
                    stripped.startswith("> [!important]")
                    or stripped.startswith(":::intro")
                    or stripped.startswith("> [!tip] ??")
                )
                return ok, j + 1, stripped[:80]
            return False, i + 1, "missing lead block after title"
    return True, 1, "no h1 title found"

def read_text(path: Path) -> str:
    return read_docx(path) if path.suffix.lower() == ".docx" else path.read_text(encoding="utf-8", errors="replace")

def extract_title(text: str, path: Path) -> str:
    if path.suffix.lower() == ".docx":
        for line in text.splitlines():
            stripped = line.strip()
            if stripped:
                return stripped
        return ""
    m = re.search(r"(?m)^\ufeff?\s*#\s+(.+?)\s*$", text)
    return m.group(1).strip() if m else ""

def sanitize_filename_stem(title: str) -> str:
    stem = re.sub(r"\s+", " ", title).strip().translate(WINDOWS_ILLEGAL)
    stem = stem.rstrip(" .")
    return stem[:120].rstrip(" .")

TITLE_MIN_LEN = 24
TITLE_MAX_LEN = 45
TITLE_RHYTHM_RE = re.compile(r"[\uff01\uff0c\uff1a\uff1f]")
TITLE_ANCHOR_WORDS = [
    "\u521a\u521a", "\u7a81\u53d1", "\u9996\u4e2a", "\u9996\u6b21", "\u6700\u5927", "\u4e07", "\u4ebf", "\u7f8e\u5143",
    "\u878d\u8d44", "\u4e0a\u5e02", "\u53d1\u5e03", "\u5f00\u6e90", "\u53ec\u56de", "\u7981\u7528", "\u5b9e\u540d", "\u5237\u8138",
    "\u88c1\u5458", "\u6da8", "\u8dcc",
]
TITLE_ACTION_WORDS = [
    "\u53d1\u5e03", "\u63a8\u51fa", "\u4e0a\u7ebf", "\u66f4\u65b0", "\u5f00\u6e90", "\u6536\u8d2d", "\u878d\u8d44", "\u4e0a\u5e02",
    "\u4e0b\u67b6", "\u7981\u7528", "\u53ec\u56de", "\u8c03\u67e5", "\u8d77\u8bc9", "\u52a0\u5165", "\u79bb\u5f00", "\u8df3\u69fd",
    "\u84b8\u53d1", "\u66b4\u6da8", "\u66b4\u8dcc", "\u88c1\u5458", "\u6539\u5199", "\u4e89\u593a", "\u76ef\u4e0a", "\u6682\u505c",
    "\u5f00\u653e", "\u63a5\u5165", "\u5356\u7ed9", "\u4e0a\u4f4d", "\u51fa\u5c40",
]
TITLE_ANCHOR_RE = re.compile(r"(?:\d|[A-Za-z][A-Za-z0-9.-]{2,}|" + "|".join(re.escape(w) for w in TITLE_ANCHOR_WORDS) + r")")
TITLE_ACTION_RE = re.compile(r"(?:" + "|".join(re.escape(w) for w in TITLE_ACTION_WORDS) + r")")

def visible_title_length(title: str) -> int:
    return len(re.sub(r"\s+", "", title))

def title_quality_findings(title: str) -> list[dict[str, object]]:
    findings = []
    length = visible_title_length(title)
    if length < TITLE_MIN_LEN or length > TITLE_MAX_LEN:
        findings.append({"kind": "title_length_out_of_range", "term": f"title has {length} visible chars; target 28-38 and hard range {TITLE_MIN_LEN}-{TITLE_MAX_LEN}", "line": 1})
    if not TITLE_RHYTHM_RE.search(title):
        findings.append({"kind": "title_lacks_rhythm_punctuation", "term": "title should usually use one rhythm separator such as \uff01, \uff0c, \uff1a, or \uff1f", "line": 1})
    if not TITLE_ANCHOR_RE.search(title):
        findings.append({"kind": "title_lacks_specific_anchor", "term": "title should include a verified number, fresh timing, or canonical English model/company/product name when available", "line": 1})
    if not TITLE_ACTION_RE.search(title):
        findings.append({"kind": "title_lacks_action_or_conflict", "term": "title should include a concrete action, conflict, or consequence, not just a topic label", "line": 1})
    return findings

def line_number(text: str, start: int) -> int:
    return text.count("\n", 0, start) + 1

def find_terms(text: str, terms: list[str], kind: str) -> list[dict[str, object]]:
    findings=[]; occupied=[]
    for term in sorted(terms, key=len, reverse=True):
        for match in re.finditer(re.escape(term), text):
            span=match.span()
            if any(not (span[1] <= old[0] or span[0] >= old[1]) for old in occupied): continue
            occupied.append(span)
            findings.append({"kind":kind,"term":term,"line":line_number(text, match.start())})
    return findings

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("path"); ap.add_argument("--json", action="store_true"); args=ap.parse_args()
    path=Path(args.path); text=read_text(path)
    image_count = count_docx_images(path) if path.suffix.lower()==".docx" else count_markdown_images(text)
    findings=[]
    findings += find_terms(text, BANNED_SCAFFOLD, "banned_scaffold")
    findings += find_terms(text, AI_FLAVOR, "ai_flavor")
    findings += find_terms(text, VAGUE_AUTHORITY, "vague_authority")
    body=strip_sources(text); body_chars=chinese_char_count(body)
    if body_chars < 1800: findings.append({"kind":"article_too_short","term":f"main body has {body_chars} Chinese chars; target 1800-2300","line":1})
    if image_count < 5: findings.append({"kind":"too_few_images","term":f"found {image_count} image(s); target at least 5","line":1})
    if path.suffix.lower() != ".docx" and image_count >= 1 and not has_official_image(text, path): findings.append({"kind":"missing_official_source_image","term":"at least one image must be an official/source visual","line":1})
    if path.suffix.lower() in {".html", ".htm"} and not re.search(r"font-size\s*:\s*16px", text, flags=re.I):
        findings.append({"kind":"html_body_font_not_16px","term":"WeChat HTML body prose must include font-size:16px styling","line":1})
    for m in SOURCE_NUMBERED_RE.finditer(text): findings.append({"kind":"numbered_source_heading","term":m.group(0).strip(),"line":line_number(text,m.start())})
    if path.suffix.lower() != ".docx":
        ok, lead_line, lead_value = lead_immediately_after_title(text)
        if not ok:
            findings.append({
                "kind": "lead_not_immediately_after_title",
                "term": f"title must be followed immediately by lead block; found: {lead_value}",
                "line": lead_line,
            })
    if path.suffix.lower() in {".md", ".docx", ".html", ".htm"}:
        title = extract_title(text, path)
        if title:
            findings += title_quality_findings(title)
            expected_stem = sanitize_filename_stem(title)
            if path.stem != expected_stem:
                findings.append({
                    "kind": "filename_not_title",
                    "term": f"main file stem must match sanitized H1 title: expected '{expected_stem}', got '{path.stem}'",
                    "line": 1,
                })
    payload={"path":str(path),"findings":findings,"count":len(findings),"main_body_chinese_chars":body_chars,"image_count":image_count}
    if args.json: print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if findings:
            print(f"{path}: {len(findings)} finding(s)")
            for f in findings: print(f"- {f['kind']} line {f['line']}: {f['term']}")
        else: print(f"{path}: clean")
    return 1 if findings else 0
if __name__ == "__main__": raise SystemExit(main())
