#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

BANNED_SCAFFOLD = [
    "\u4e8b\u4ef6\u5148\u6446\u51fa", "\u4e8b\u4ef6\u5148\u6446\u51fa\u6765", "\u8fd9\u573a\u4e89\u8bae\u770b\u4e09\u4ef6\u4e8b",
    "\u666e\u901a\u4eba\u8be5\u770b\u61c2\u4ec0\u4e48", "\u666e\u901a\u4eba\u8be5\u600e\u4e48\u770b", "\u666e\u901a\u4eba\u8be5\u600e\u4e48\u5224\u65ad",
    "\u666e\u901a\u4eba\u6709\u4ec0\u4e48\u5173\u7cfb", "\u76ef\u4e09\u4e2a\u7ed3\u679c\u5c31\u591f\u4e86", "\u63a5\u4e0b\u6765\u600e\u4e48\u770b",
    "\u771f\u6b63\u503c\u5f97\u5173\u6ce8\u7684\u662f", "\u8fd9\u8bf4\u660e\u4e86\u4ec0\u4e48", "\u8bf4\u767d\u4e86", "\u4e00\u53e5\u8bdd\u603b\u7ed3", "\u503c\u5f97\u4e00\u63d0\u7684\u662f"
]
AI_FLAVOR = [
    "\u6807\u5fd7\u7740", "\u51f8\u663e", "\u91cd\u5927\u8f6c\u6298", "\u6df1\u523b\u63ed\u793a", "\u63a5\u4e0b\u6765\u6211\u4eec\u6765\u770b\u770b",
    "\u6211\u4eec\u5148\u8bf4\u7ed3\u8bba", "\u771f\u6b63\u7684\u95ee\u9898\u662f", "\u5e95\u5c42\u903b\u8f91\u662f", "\u6838\u5fc3\u672c\u8d28\u662f",
    "\u672a\u6765\u503c\u5f97\u671f\u5f85", "\u666e\u901a\u4eba\u9700\u8981\u4fdd\u6301\u5173\u6ce8", "\u65f6\u4ee3\u5df2\u7ecf\u53d8\u4e86"
]
VAGUE_AUTHORITY = ["\u4e1a\u5185\u4eba\u58eb", "\u4e13\u5bb6\u8ba4\u4e3a", "\u6709\u89c2\u70b9\u6307\u51fa", "\u5e02\u573a\u4eba\u58eb\u8ba4\u4e3a", "\u5916\u754c\u8ba4\u4e3a", "\u4e0d\u5c11\u4eba\u8ba4\u4e3a"]
OFFICIAL_IMAGE_HINTS = ["\u5b98\u65b9\u914d\u56fe", "\u5b98\u65b9\u6765\u6e90", "\u5b98\u7f51\u622a\u56fe", "\u539f\u59cb\u6765\u6e90", "official", "source", "official_source", "apple", "google", "meta", "gallup", "challenger", "wired", "sec", "ftc", "gov", "businessinsider", "deepmind"]
SOURCE_NUMBERED_RE = re.compile(r"(?m)^\s*(?:#{1,6}\s*)?(?:0?\d+|[\u4e00\u4e8c\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]+)[\.\u3001\s_-]*\u4e8b\u5b9e\u6765\u6e90\s*$")

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

def read_text(path: Path) -> str:
    return read_docx(path) if path.suffix.lower() == ".docx" else path.read_text(encoding="utf-8", errors="replace")

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
    for m in SOURCE_NUMBERED_RE.finditer(text): findings.append({"kind":"numbered_source_heading","term":m.group(0).strip(),"line":line_number(text,m.start())})
    payload={"path":str(path),"findings":findings,"count":len(findings),"main_body_chinese_chars":body_chars,"image_count":image_count}
    if args.json: print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        if findings:
            print(f"{path}: {len(findings)} finding(s)")
            for f in findings: print(f"- {f['kind']} line {f['line']}: {f['term']}")
        else: print(f"{path}: clean")
    return 1 if findings else 0
if __name__ == "__main__": raise SystemExit(main())
