#!/usr/bin/env python3
"""
For each _publications/*.md:
1. Identify the real DOI/URL using title + venue
2. Update paperurl field
3. Try to download open-access PDF to images/papers/
"""

import os, re, time, requests, json, urllib.parse, shutil, sys
from pathlib import Path

# Force UTF-8 output so Chinese titles don't crash on Windows
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PUBS_DIR = Path("C:/Users/yan/OneDrive/yemanzhongting.github.io/_publications")
PAPERS_DIR = Path("C:/Users/yan/OneDrive/yemanzhongting.github.io/images/papers")
PAPERS_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (research tool; mailto:yanzhang@cuhk.edu.hk)"
}

# Known real URLs already in files (keep these as-is if they look real)
PLACEHOLDER_PATTERNS = [
    r'academicpages\.github\.io/files/',
    r'^$',
]

def is_placeholder(url: str) -> bool:
    if not url:
        return True
    for p in PLACEHOLDER_PATTERNS:
        if re.search(p, url):
            return True
    return False

def search_crossref(title: str) -> str | None:
    """Search CrossRef for DOI by title."""
    try:
        q = urllib.parse.quote(title)
        url = f"https://api.crossref.org/works?query.title={q}&rows=3&select=DOI,title"
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            items = r.json().get("message", {}).get("items", [])
            if items:
                doi = items[0].get("DOI")
                if doi:
                    return f"https://doi.org/{doi}"
    except Exception as e:
        print(f"  CrossRef error: {e}")
    return None

def try_download_pdf(doi_url: str, paper_id: str) -> str | None:
    """Try to download open-access PDF via Unpaywall or direct DOI."""
    if not doi_url or "doi.org" not in doi_url:
        return None
    
    doi = doi_url.replace("https://doi.org/", "").replace("http://doi.org/", "")
    pdf_path = PAPERS_DIR / f"{paper_id}.pdf"
    
    if pdf_path.exists():
        print(f"  PDF already exists: {pdf_path.name}")
        return f"/images/papers/{paper_id}.pdf"
    
    # Try Unpaywall
    try:
        email = "yanzhang@cuhk.edu.hk"
        uw_url = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={email}"
        r = requests.get(uw_url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            oa_loc = data.get("best_oa_location")
            if oa_loc:
                pdf_url = oa_loc.get("url_for_pdf") or oa_loc.get("url")
                if pdf_url and pdf_url.endswith(".pdf"):
                    print(f"  Unpaywall PDF: {pdf_url}")
                    pr = requests.get(pdf_url, headers=HEADERS, timeout=30, stream=True)
                    if pr.status_code == 200 and "pdf" in pr.headers.get("content-type", ""):
                        with open(pdf_path, "wb") as f:
                            shutil.copyfileobj(pr.raw, f)
                        print(f"  Downloaded: {pdf_path.name} ({pdf_path.stat().st_size // 1024}KB)")
                        return f"/images/papers/{paper_id}.pdf"
    except Exception as e:
        print(f"  Unpaywall error: {e}")
    
    return None

def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """Parse YAML frontmatter. Returns (fields, raw_fm, body)."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)', text, re.DOTALL)
    if not m:
        return {}, "", text
    raw_fm = m.group(1)
    body = m.group(2)
    fields = {}
    for line in raw_fm.splitlines():
        kv = re.match(r'^(\w+)\s*:\s*(.*)', line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip().strip("'\"")
    return fields, raw_fm, body

def update_paperurl_in_file(filepath: Path, new_url: str) -> bool:
    """Update paperurl field in frontmatter."""
    text = filepath.read_text(encoding="utf-8")
    # Replace existing paperurl line
    new_text = re.sub(
        r"^(paperurl\s*:\s*).*$",
        f"paperurl: '{new_url}'",
        text, flags=re.MULTILINE
    )
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        return True
    return False

# ── Main ──────────────────────────────────────────────────────────────────────
results = []
md_files = sorted(PUBS_DIR.glob("*.md"))
print(f"Found {len(md_files)} publication files\n")

for md_file in md_files:
    paper_id = md_file.stem  # e.g. "2024-paper-3"
    text = md_file.read_text(encoding="utf-8")
    fields, raw_fm, body = parse_frontmatter(text)
    
    title = fields.get("title", "").strip().strip('"').strip("'")
    current_url = fields.get("paperurl", "").strip().strip("'\"")
    
    print(f"[{paper_id}] {title[:60]}")
    
    # If URL already looks real, keep it but still try PDF
    if not is_placeholder(current_url):
        print(f"  URL already real: {current_url}")
        real_url = current_url
    else:
        # Search CrossRef
        real_url = search_crossref(title)
        if real_url:
            print(f"  Found DOI: {real_url}")
            update_paperurl_in_file(md_file, real_url)
        else:
            print(f"  Could not find DOI")
            real_url = current_url
    
    # Try to download PDF
    pdf_local = try_download_pdf(real_url, paper_id)
    
    results.append({
        "id": paper_id,
        "title": title[:60],
        "url": real_url,
        "pdf": pdf_local or "not available"
    })
    
    time.sleep(0.5)  # Be polite to APIs

# Print summary
print("\n\n══ SUMMARY ══")
print(f"{'ID':<20} {'URL set':<8} {'PDF':<30}")
for r in results:
    has_url = "✓" if r["url"] and "academicpages" not in r["url"] and r["url"] else "✗"
    print(f"{r['id']:<20} {has_url:<8} {r['pdf']:<30}")

# Save JSON summary
summary_path = Path("C:/Users/yan/OneDrive/yemanzhongting.github.io/scripts/publication_update_results.json")
with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nResults saved to {summary_path}")
