"""
YUKI NSFW API SERVER
====================
VPS pe alag chalega — port 7860 (ya koi bhi)
Bot isko call karega locally: http://localhost:7860/check

Install:
    pip install fastapi uvicorn nudenet pillow python-multipart

Run:
    python nsfw_server.py
    # ya background mein:
    nohup python nsfw_server.py &

NudeNet:
  - Pure Python, no C compile needed
  - CPU pe bhi fast (2-3 sec per image)
  - 8GB RAM mein aaram se fit
  - Detects: EXPOSED_*, COVERED_* body parts with confidence scores
"""

import io
import os
import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image

# ── NudeNet ──────────────────────────────────────────────────────────────────
try:
    from nudenet import NudeDetector
    detector = NudeDetector()
    print("[NSFW Server] ✅ NudeNet loaded!")
except Exception as e:
    detector = None
    print(f"[NSFW Server] ❌ NudeNet failed: {e}")

# ── NSFW labels jo actually explicit hain ─────────────────────────────────────
EXPLICIT_LABELS = {
    "ANUS_EXPOSED",
    "ARMPITS_EXPOSED",      # exclude karna ho toh hata do
    "BELLY_EXPOSED",        # exclude karna ho toh hata do
    "FEMALE_BREAST_EXPOSED",     # female exposed breast
    "BUTTOCKS_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
    "MALE_BREAST_EXPOSED",
    "FACE_FEMALE",               # face detection (optional)
    "FACE_MALE",
}

# Sirf inhe NSFW maano (strict mode)
STRICT_NSFW = {
    "ANUS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
    "MALE_BREAST_EXPOSED",
}

NSFW_THRESHOLD = 0.01


# ── FastAPI app ───────────────────────────────────────────────────────────────
app = FastAPI(title="Yuki NSFW API", version="1.0")

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("nsfw_server")


@app.get("/")
async def root():
    return {"status": "ok", "model": "NudeNet", "ready": detector is not None}


@app.get("/health")
async def health():
    return {"status": "ok", "detector": detector is not None}


@app.post("/check")
async def check_nsfw(file: UploadFile = File(...)):
    """
    Image bhejo → NSFW hai ya nahi batata.

    Response:
    {
        "nsfw": true/false,
        "score": 0.85,           # highest confidence among NSFW labels
        "labels": ["FEMALE_BREAST_EXPOSED"],   # detected NSFW labels
        "all_detections": [...]  # full NudeNet output
    }
    """
    if detector is None:
        raise HTTPException(503, "NudeNet not loaded")

    # Read image bytes
    try:
        contents = await file.read()
        if len(contents) < 100:
            raise HTTPException(400, "File too small / empty")

        # Validate it's actually an image
        img = Image.open(io.BytesIO(contents))
        img.verify()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(400, f"Invalid image: {e}")

    # Save to temp file (NudeNet needs file path)
    tmp_path = f"/tmp/nsfw_check_{os.getpid()}.jpg"
    try:
        # Re-open (verify() closes the file)
        img = Image.open(io.BytesIO(contents)).convert("RGB")
        img.save(tmp_path, "JPEG", quality=85)

        # Run detection
        results = detector.detect(tmp_path)

        # Analyze results
        nsfw_found   = []
        highest_score = 0.0

        for detection in results:
            label = detection.get("class", "")
            score = float(detection.get("score", 0))

            if label in STRICT_NSFW and score >= NSFW_THRESHOLD:
                nsfw_found.append({"label": label, "score": round(score, 3)})
                highest_score = max(highest_score, score)

        is_nsfw = len(nsfw_found) > 0

        log.info(f"[check] nsfw={is_nsfw} score={highest_score:.2f} labels={[x['label'] for x in nsfw_found]}")

        return JSONResponse({
            "nsfw":           is_nsfw,
            "score":          round(highest_score, 3),
            "labels":         [x["label"] for x in nsfw_found],
            "all_detections": results,
        })

    except Exception as e:
        log.error(f"[check] Detection error: {e}")
        raise HTTPException(500, f"Detection failed: {e}")
    finally:
        try:
            os.remove(tmp_path)
        except Exception:
            pass


# ── GIF / Video frame check ───────────────────────────────────────────────────
@app.post("/check_frame")
async def check_frame(file: UploadFile = File(...)):
    """
    GIF ya video ka thumbnail check karo.
    Same response as /check.
    """
    return await check_nsfw(file)


if __name__ == "__main__":
    port = int(os.environ.get("NSFW_PORT", 7860))
    log.info(f"Starting YUKI NSFW Server on port {port}...")
    uvicorn.run(
        "nsfw_server:app",
        host="0.0.0.0",
        port=port,
        log_level="info",
        workers=2,          # 2 workers = parallel checks, 8GB RAM mein fine
    )
