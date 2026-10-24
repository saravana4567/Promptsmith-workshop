#!/usr/bin/env python3
"""Store and auto-tag prompts in prompt_library.csv.
Usage:
  python prompt_tagger.py add "Title" "Tool" "prompt text"
  python prompt_tagger.py list
  python prompt_tagger.py search keyword
Warns if the prompt looks like it contains private data.
"""
import csv, sys, re, os
from datetime import date

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "09_prompt_library.csv")
FIELDS = ["id", "date", "title", "tool", "tags", "prompt", "verified", "notes"]
RULES = {
    "code": ["code", "python", "java", "function", "bug", "error"],
    "writing": ["email", "write", "summarize", "resume", "readme", "post"],
    "study": ["explain", "quiz", "study", "exam", "concept"],
    "few-shot": ["example:", "examples", "for example"],
    "chain-of-thought": ["step by step", "step-by-step", "think"],
    "react": ["search", "look up", "sources", "cite"],
    "role": ["you are"],
    "format": ["table", "bullets", "json", "words"],
}
PRIVATE = [r"\b\d{12}\b", r"password\s*[:=]", r"api[_-]?key", r"\b[\w.]+@[\w.]+\.\w+\b"]

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def tag(text):
    t = text.lower()
    return ";".join(k for k, words in RULES.items() if any(w in t for w in words)) or "general"

def add(title, tool, prompt):
    for p in PRIVATE:
        if re.search(p, prompt, re.I):
            print("WARNING: possible private data detected. Remove it before saving.")
            return
    rows = load()
    rows.append({"id": len(rows) + 1, "date": date.today().isoformat(), "title": title,
                 "tool": tool, "tags": tag(prompt), "prompt": prompt, "verified": "no", "notes": ""})
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    print("Saved with tags:", rows[-1]["tags"])

def main():
    a = sys.argv[1:]
    if a[:1] == ["add"] and len(a) == 4: add(a[1], a[2], a[3])
    elif a[:1] == ["list"]:
        for r in load(): print(r["id"], r["title"], "|", r["tool"], "|", r["tags"])
    elif a[:1] == ["search"] and len(a) == 2:
        for r in load():
            if a[1].lower() in (r["title"] + r["tags"] + r["prompt"]).lower(): print(r["id"], r["title"], "|", r["tags"])
    else: print(__doc__)

if __name__ == "__main__":
    main()
