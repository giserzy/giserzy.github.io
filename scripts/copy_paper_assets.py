# -*- coding: utf-8 -*-
"""Copy paper PDFs and compress first-page teasers into the Jekyll site."""
import os, shutil
from PIL import Image

SRC = r"C:\Users\yan\OneDrive\26论文\文献"
SITE = r"C:\Users\yan\OneDrive\yemanzhongting.github.io"
PDF_DST = os.path.join(SITE, "files", "papers")
TEASER_DST = os.path.join(SITE, "images", "pub-teasers")
os.makedirs(PDF_DST, exist_ok=True)
os.makedirs(TEASER_DST, exist_ok=True)

# publication id -> (source pdf, target pdf name)
PDF_MAP = {
    "2021-paper-1":  ("1-s2.0-S0022169421011033-main.pdf", "2021-JHydrology-Extracting-flooding-events-social-sensing.pdf"),
    "2021-paper-2":  ("1-s2.0-S0360132321002894-main.pdf", "2021-BuildEnviron-Urban-habitat-resident-health-sensing.pdf"),
    "2021-paper-3":  ("1-s2.0-S0198971521000363-main.pdf", "2021-CEUS-KE-CNN-social-sensing.pdf"),
    "2022-paper-3":  ("1-s2.0-S2210670722003201-main.pdf", "2022-SCS-City2vec-urban-knowledge.pdf"),
    "2022-paper-4":  ("1-s2.0-S1569843222001807-main.pdf", "2022-IJAEOG-Migratable-street-scene-sensing.pdf"),
    "2023-paper-2":  ("1-s2.0-S1618866723002583-main.pdf", "2023-UFUG-Restorative-effects-campus-spaces.pdf"),
    "2023-paper-4":  ("1-s2.0-S1569843223002820-main.pdf", "2023-IJAEOG-Inferring-socioeconomic-environment.pdf"),
    "2023-paper-9":  ("1-s2.0-S0301479722019752-main.pdf", "2023-JEM-Carbon-trading-spatial-inequality.pdf"),
    "2024-paper-2":  ("1-s2.0-S0143622824001747-main.pdf", "2024-ApplGeog-Noise-exposure-inequality.pdf"),
    "2024-paper-6":  ("1-s2.0-S0959652624029925-main.pdf", "2024-JCP-SAGE-GSAN-taxi-CO-emissions.pdf"),
    "2024-paper-7":  ("1-s2.0-S0924271624003708-main.pdf", "2024-ISPRS-Multi-level-street-representation.pdf"),
    "2025-paper-3":  ("s41597-025-04757-8.pdf",            "2025-SciData-LLM-crime-dataset.pdf"),
    "2025-paper-8":  ("CrossGraphNet  a cross-spatiotemporal graph-based method for traffic speed reconstruction using remote sensing vehicle detection.pdf", "2025-IJDE-CrossGraphNet-traffic-speed.pdf"),
    "2025-paper-9":  ("How drivers  depth perception of environmental features influences traffic speed.pdf", "2025-GSIS-Drivers-depth-perception-traffic-speed.pdf"),
    "2025-paper-11": ("1-s2.0-S2095927325007364-main.pdf", "2025-SciBull-Mobility-environmental-exposure.pdf"),
    "2026-paper-1":  ("1-s2.0-S0198971526000037-main.pdf", "2026-CEUS-Multi-frequency-noise-mapping.pdf"),
    "2026-paper-2":  ("1-s2.0-S0169204626000241-main.pdf", "2026-LUP-Mobility-exposure-inequality.pdf"),
    "2026-paper-3":  ("1-s2.0-S2212095526000593-main.pdf", "2026-UrbanClimate-Seasonal-heat-exposure-NEAP.pdf"),
    "2026-paper-5":  ("s44284-025-00372-1.pdf",            "2026-TRD-AlphaEarth-traffic-noise.pdf"),
    "2026-paper-10": ("1-s2.0-S0277953626005927-main.pdf", "2026-SSM-Noise-complaint-multi-LLM.pdf"),
}

# teaser image number -> publication id
TEASER_MAP = {
    "01": "2025-paper-9",  "02": "2026-paper-5",  "03": "2026-paper-10",
    "04": "2026-paper-2",  "05": "2026-paper-1",  "06": "2026-paper-3",
    "07": "2025-paper-8",  "08": "2025-paper-11", "09": "2025-paper-3",
    "10": "2024-paper-9",  "11": "2024-paper-7",  "12": "2024-paper-2",
    "13": "2023-paper-4",  "14": "2023-paper-7",  "15": "2023-paper-9",
    "16": "2022-paper-3",  "17": "2022-paper-4",  "18": "2021-paper-1",
    "19": "2021-paper-2",  "23": "2022-paper-1",  "24": "2021-paper-3",
    "25": "2024-paper-6",  "26": "2023-paper-2",  "27": "2026-paper-9",
    "29": "2025-paper-6",
}

print("=== PDFs ===")
ok, fail = 0, 0
for pid, (src, dst) in PDF_MAP.items():
    s = os.path.join(SRC, src)
    d = os.path.join(PDF_DST, dst)
    if not os.path.exists(s):
        print(f"MISSING SRC: {src}")
        fail += 1
        continue
    shutil.copy2(s, d)
    ok += 1
print(f"copied {ok} pdfs, {fail} missing")

print("=== Teasers ===")
ok, fail = 0, 0
for num, pid in TEASER_MAP.items():
    candidates = [f for f in os.listdir(os.path.join(SRC, "first_page_images"))
                  if f.startswith(num + " ")]
    if not candidates:
        print(f"MISSING teaser #{num}")
        fail += 1
        continue
    s = os.path.join(SRC, "first_page_images", candidates[0])
    d = os.path.join(TEASER_DST, f"{pid}.jpg")
    try:
        im = Image.open(s).convert("RGB")
        w = 340
        h = int(im.height * w / im.width)
        im = im.resize((w, h), Image.LANCZOS)
        im.save(d, "JPEG", quality=82, optimize=True)
        ok += 1
    except Exception as e:
        print(f"ERROR {num}: {e}")
        fail += 1
print(f"teasers {ok} ok, {fail} failed")

total_pdf = sum(os.path.getsize(os.path.join(PDF_DST, f)) for f in os.listdir(PDF_DST))
total_te = sum(os.path.getsize(os.path.join(TEASER_DST, f)) for f in os.listdir(TEASER_DST))
print(f"PDF total: {total_pdf/1e6:.1f} MB | Teasers total: {total_te/1e6:.2f} MB")
