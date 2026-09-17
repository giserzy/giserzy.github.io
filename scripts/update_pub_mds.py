# -*- coding: utf-8 -*-
"""Add teaser front matter and localize paperurl for existing publications."""
import os, re

FOLDER = r"C:\Users\yan\OneDrive\yemanzhongting.github.io\_publications"

PDF_URLS = {
    "2021-paper-1":  "/files/papers/2021-JHydrology-Extracting-flooding-events-social-sensing.pdf",
    "2021-paper-2":  "/files/papers/2021-BuildEnviron-Urban-habitat-resident-health-sensing.pdf",
    "2021-paper-3":  "/files/papers/2021-CEUS-KE-CNN-social-sensing.pdf",
    "2022-paper-3":  "/files/papers/2022-SCS-City2vec-urban-knowledge.pdf",
    "2022-paper-4":  "/files/papers/2022-IJAEOG-Migratable-street-scene-sensing.pdf",
    "2023-paper-2":  "/files/papers/2023-UFUG-Restorative-effects-campus-spaces.pdf",
    "2023-paper-4":  "/files/papers/2023-IJAEOG-Inferring-socioeconomic-environment.pdf",
    "2023-paper-9":  "/files/papers/2023-JEM-Carbon-trading-spatial-inequality.pdf",
    "2024-paper-2":  "/files/papers/2024-ApplGeog-Noise-exposure-inequality.pdf",
    "2024-paper-6":  "/files/papers/2024-JCP-SAGE-GSAN-taxi-CO-emissions.pdf",
    "2024-paper-7":  "/files/papers/2024-ISPRS-Multi-level-street-representation.pdf",
    "2025-paper-3":  "/files/papers/2025-SciData-LLM-crime-dataset.pdf",
    "2025-paper-8":  "/files/papers/2025-IJDE-CrossGraphNet-traffic-speed.pdf",
    "2025-paper-9":  "/files/papers/2025-GSIS-Drivers-depth-perception-traffic-speed.pdf",
    "2026-paper-1":  "/files/papers/2026-CEUS-Multi-frequency-noise-mapping.pdf",
    "2026-paper-2":  "/files/papers/2026-LUP-Mobility-exposure-inequality.pdf",
    "2026-paper-3":  "/files/papers/2026-UrbanClimate-Seasonal-heat-exposure-NEAP.pdf",
    "2026-paper-5":  "/files/papers/2026-TRD-AlphaEarth-traffic-noise.pdf",
    "2026-paper-10": "/files/papers/2026-SSM-Noise-complaint-multi-LLM.pdf",
}

# pubs that get a teaser but keep their external paperurl
TEASER_ONLY = ["2022-paper-1", "2026-paper-9", "2025-paper-6"]

targets = dict(PDF_URLS)
for pid in TEASER_ONLY:
    targets.setdefault(pid, None)

changed = 0
for pid, url in targets.items():
    f = os.path.join(FOLDER, pid + ".md")
    if not os.path.exists(f):
        print(f"SKIP (no file): {pid}")
        continue
    with open(f, encoding="utf-8") as fh:
        txt = fh.read()

    orig = txt

    if url:
        txt = re.sub(r"^paperurl:.*$", f"paperurl: '{url}'", txt, count=1, flags=re.M)

    if "teaser" not in txt:
        teaser_block = f'---\nheader:\n  teaser: "/images/pub-teasers/{pid}.jpg"\n'
        txt = re.sub(r"^(---\s*\n)", teaser_block.replace("\\", "\\\\"), txt, count=1)

    if txt != orig:
        with open(f, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(txt)
        changed += 1
        print(f"updated: {pid}")
    else:
        print(f"unchanged: {pid}")

print(f"\n{changed} files updated")
