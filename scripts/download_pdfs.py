#!/usr/bin/env python3
"""
Second pass: try to download PDFs for papers that don't have them yet.
Uses multiple open-access sources: Unpaywall, OpenDOAR, PubMed Central, Semantic Scholar.
"""
import sys, re, time, requests, json, shutil, urllib.parse
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PUBS_DIR = Path("C:/Users/yan/OneDrive/yemanzhongting.github.io/_publications")
PAPERS_DIR = Path("C:/Users/yan/OneDrive/yemanzhongting.github.io/images/papers")
PAPERS_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; academic research tool; mailto:yanzhang@cuhk.edu.hk)"
}
EMAIL = "yanzhang@cuhk.edu.hk"

def get_doi_from_file(md_path):
    text = md_path.read_text(encoding='utf-8')
    m = re.search(r"paperurl:\s*['\"]?(https?://(?:doi\.org|dx\.doi\.org)/[^\s'\"]+)", text)
    if m:
        url = m.group(1).rstrip("'\"")
        doi = re.sub(r"https?://(?:dx\.)?doi\.org/", "", url)
        return doi, url
    # Try to extract non-DOI URLs
    m2 = re.search(r"paperurl:\s*['\"]?(https?://[^\s'\"]+)", text)
    if m2:
        return None, m2.group(1).rstrip("'\"")
    return None, None

def try_unpaywall(doi):
    """Return PDF url if open access via Unpaywall."""
    try:
        enc_doi = urllib.parse.quote(doi, safe='')
        url = f"https://api.unpaywall.org/v2/{enc_doi}?email={EMAIL}"
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            loc = data.get("best_oa_location")
            if loc:
                pdf_url = loc.get("url_for_pdf") or loc.get("url")
                return pdf_url
    except:
        pass
    return None

def try_semantic_scholar(doi):
    """Get PDF URL from Semantic Scholar."""
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(doi)}?fields=openAccessPdf"
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            oa = data.get("openAccessPdf")
            if oa and oa.get("url"):
                return oa["url"]
    except:
        pass
    return None

def download_pdf(pdf_url, dest_path, min_size=10000):
    """Download and verify PDF."""
    try:
        r = requests.get(pdf_url, headers={**HEADERS, "Accept": "application/pdf"},
                         timeout=60, stream=True, allow_redirects=True)
        if r.status_code == 200:
            ct = r.headers.get("content-type", "")
            if "pdf" in ct or pdf_url.endswith(".pdf"):
                content = r.content
                if len(content) > min_size and content[:4] == b'%PDF':
                    dest_path.write_bytes(content)
                    return True
    except Exception as e:
        print(f"    Download error: {e}")
    return False

def update_paperurl_field(md_path, new_url):
    text = md_path.read_text(encoding='utf-8')
    new_text = re.sub(r'^(paperurl\s*:\s*).*$', f"paperurl: '{new_url}'", text, flags=re.MULTILINE)
    if new_text != text:
        md_path.write_text(new_text, encoding='utf-8')

downloaded = []
skipped = []
failed = []

md_files = sorted(PUBS_DIR.glob("*.md"))
print(f"Processing {len(md_files)} files...\n")

for md_path in md_files:
    paper_id = md_path.stem
    pdf_dest = PAPERS_DIR / f"{paper_id}.pdf"

    if pdf_dest.exists() and pdf_dest.stat().st_size > 10000:
        print(f"[{paper_id}] Already have PDF ({pdf_dest.stat().st_size//1024}KB)")
        # Update paperurl to point to local PDF
        update_paperurl_field(md_path, f"/images/papers/{paper_id}.pdf")
        downloaded.append(paper_id)
        continue

    doi, current_url = get_doi_from_file(md_path)
    if not doi:
        print(f"[{paper_id}] No DOI, skipping (URL: {current_url})")
        skipped.append(paper_id)
        continue

    print(f"[{paper_id}] DOI: {doi}")

    # Try Unpaywall first
    pdf_url = try_unpaywall(doi)
    source = "unpaywall"
    
    if not pdf_url or not pdf_url.endswith(".pdf"):
        # Try Semantic Scholar
        pdf_url = try_semantic_scholar(doi)
        source = "semanticscholar"
    
    if pdf_url:
        print(f"  Trying {source}: {pdf_url[:80]}")
        if download_pdf(pdf_url, pdf_dest):
            size_kb = pdf_dest.stat().st_size // 1024
            print(f"  Downloaded: {paper_id}.pdf ({size_kb}KB)")
            update_paperurl_field(md_path, f"/images/papers/{paper_id}.pdf")
            downloaded.append(paper_id)
            time.sleep(0.3)
            continue
        else:
            print(f"  Download failed or not PDF")
    else:
        print(f"  No open-access PDF found")
    
    failed.append(paper_id)
    time.sleep(0.5)

print(f"\n=== DONE ===")
print(f"Downloaded ({len(downloaded)}): {', '.join(downloaded)}")
print(f"No DOI/skipped ({len(skipped)}): {', '.join(skipped)}")
print(f"Not open-access ({len(failed)}): {', '.join(failed)}")
