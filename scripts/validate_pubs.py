# -*- coding: utf-8 -*-
"""Validate publication front matter and asset references."""
import os, re, glob, sys

SITE = r"C:\Users\yan\OneDrive\yemanzhongting.github.io"
FOLDER = os.path.join(SITE, "_publications")

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

errors = []
files = sorted(glob.glob(os.path.join(FOLDER, "*.md")))
for f in files:
    name = os.path.basename(f)
    txt = open(f, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.S)
    if not m:
        errors.append(f"{name}: no front matter block")
        continue
    fm = m.group(1)
    if HAS_YAML:
        try:
            data = yaml.safe_load(fm)
        except Exception as e:
            errors.append(f"{name}: YAML error: {e}")
            continue
        teaser = (data.get("header") or {}).get("teaser", "")
        if teaser:
            p = os.path.join(SITE, teaser.lstrip("/"))
            if not os.path.exists(p):
                errors.append(f"{name}: teaser missing {teaser}")
        pu = data.get("paperurl", "")
        if pu.startswith("/files/"):
            p = os.path.join(SITE, pu.lstrip("/"))
            if not os.path.exists(p):
                errors.append(f"{name}: paperurl missing {pu}")
        for k in ("title", "permalink", "date", "venue", "citation", "category"):
            if k not in data:
                errors.append(f"{name}: missing key {k}")

if errors:
    print("ERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"All {len(files)} publication files OK (yaml={HAS_YAML})")
