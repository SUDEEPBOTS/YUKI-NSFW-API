# Copyright (c) 2025 @SUDEEPBOTS <HellfireDevs>
# Location: delhi,noida
#
# All rights reserved.
#
# This code is the intellectual property of SUDEEPBOTS.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.

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

from config import STRICT_NSFW, WEAK_NSFW, EXPLICIT_LABELS, NSFW_THRESHOLD, WEAK_THRESHOLD, HOST, PORT, WORKERS, VIT_API_URL, VIT_FALLBACK, VIT_THRESHOLD


# ── FastAPI app ───────────────────────────────────────────────────────────────
app = FastAPI(title="Yuki NSFW API", version="1.0")

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("nsfw_server")


@app.get("/")
async def root():
    return {"status": "ok", "true": "me", "ready": detector is not None}


@app.get("/health")
async def health():
    return {"status": "ok", "detector": detector is not None}


@app.post("/check")
async def check_nsfw(file: UploadFile = File(...)):
    """
    Image bhejo → NSFW hai ya nahi batata.

    Pipeline: ViT (primary) → NudeNet (fallback)
    """
    # Read image bytes
    try:
        contents = await file.read()
        if len(contents) < 100:
            raise HTTPException(400, "File too small / empty")

        img = Image.open(io.BytesIO(contents))
        img.verify()
        img = Image.open(io.BytesIO(contents)).convert("RGB")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(400, f"Invalid image: {e}")

    nsfw_found   = []
    highest_score = 0.0

    # ── 1. ViT Check (Primary) ────────────────────────────────────────────
    # 96.5% accuracy — photos, stickers, drawings sab pe kaam karta hai
    if VIT_FALLBACK:
        try:
            img_bytes_io = io.BytesIO()
            img.save(img_bytes_io, "JPEG", quality=85)
            img_bytes = img_bytes_io.getvalue()

            import httpx
            async with httpx.AsyncClient(timeout=15.0) as client:
                vit_resp = await client.post(
                    VIT_API_URL,
                    files={"file": ("image.jpg", img_bytes, "image/jpeg")}
                )
                if vit_resp.status_code == 200:
                    vit_data = vit_resp.json()
                    vit_nsfw = vit_data.get("nsfw", False)
                    vit_score = vit_data.get("nsfw_score", 0)

                    if vit_nsfw and vit_score >= VIT_THRESHOLD:
                        nsfw_found.append({
                            "label": "VIT_NSFW",
                            "score": round(vit_score, 3),
                            "model": "vit"
                        })
                        highest_score = max(highest_score, vit_score)
                        log.info(f"[vit] nsfw=True score={vit_score:.3f}")
                    else:
                        log.info(f"[vit] nsfw=False score={vit_score:.3f}")
                else:
                    log.warning(f"[vit] API error: {vit_resp.status_code}")
        except ImportError:
            log.warning("[vit] httpx not installed — skipping")
        except Exception as e:
            log.warning(f"[vit] Failed: {e}")

    # ── 2. NudeNet Check (Fallback — ViT miss kare toh) ─────────────────
    if detector is not None and not nsfw_found:
        tmp_path = f"/tmp/nsfw_check_{os.getpid()}.jpg"
        try:
            img.save(tmp_path, "JPEG", quality=85)
            results = detector.detect(tmp_path)

            for detection in results:
                label = detection.get("class", "")
                score = float(detection.get("score", 0))

                if label in STRICT_NSFW and score >= NSFW_THRESHOLD:
                    nsfw_found.append({"label": label, "score": round(score, 3), "model": "nudenet"})
                    highest_score = max(highest_score, score)

                elif label in WEAK_NSFW and score >= WEAK_THRESHOLD:
                    nsfw_found.append({"label": label, "score": round(score, 3), "model": "nudenet"})
                    highest_score = max(highest_score, score)

            if nsfw_found:
                log.info(f"[nudenet] nsfw=True labels={[x['label'] for x in nsfw_found]}")
            else:
                log.info(f"[nudenet] nsfw=False — safe image")
        except Exception as e:
            log.error(f"[nudenet] Detection error: {e}")
        finally:
            try:
                os.remove(tmp_path)
            except Exception:
                pass

    is_nsfw = len(nsfw_found) > 0
    log.info(f"[check] nsfw={is_nsfw} score={highest_score:.2f} models={[x.get('model','?') for x in nsfw_found]}")

    return JSONResponse({
        "nsfw":           is_nsfw,
        "score":          round(highest_score, 3),
        "labels":         [{"label": x["label"], "model": x.get("model", "?")} for x in nsfw_found],
        "models_used":    "vit" + ("+nudenet" if not is_nsfw and detector else ""),
    })


# ── GIF / Video frame check ───────────────────────────────────────────────────
@app.post("/check_frame")
async def check_frame(file: UploadFile = File(...)):
    """
    GIF ya video ka thumbnail check karo.
    Same response as /check.
    """
    return await check_nsfw(file)


if __name__ == "__main__":
    log.info(f"Starting YUKI NSFW Server on {HOST}:{PORT} with {WORKERS} workers...")
    uvicorn.run(
        "nsfw_server:app",
        host=HOST,
        port=PORT,
        log_level="info",
        workers=WORKERS,
    )
