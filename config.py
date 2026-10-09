# --------------------------------------------------------------------------
# Copyright (c) 2026 SUDEEPBOTS. All Rights Reserved.
# Yuki NSFW API — High-Performance Computer Vision Content Moderation Engine
# Licensed under the MIT License. See LICENSE in the project root for details.
# --------------------------------------------------------------------------

import os

# Server Configuration
PORT = int(os.environ.get("PORT", os.environ.get("NSFW_PORT", 7860)))
HOST = os.environ.get("NSFW_HOST", "0.0.0.0")
WORKERS = int(os.environ.get("NSFW_WORKERS", 2))

# NudeNet Configuration
NSFW_THRESHOLD = float(os.environ.get("NSFW_THRESHOLD", 0.01))
WEAK_THRESHOLD = float(os.environ.get("WEAK_THRESHOLD", 0.01))

# Labels to consider as strict NSFW (exposed + covered)
STRICT_NSFW = {
    "ANUS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
    "MALE_BREAST_EXPOSED",
    "FEMALE_BREAST_COVERED",
    "BUTTOCKS_COVERED",
    "FEMALE_GENITALIA_COVERED",
    "MALE_GENITALIA_COVERED",
    "ANUS_COVERED",
    "BELLY_EXPOSED",
    "ARMPITS_EXPOSED",
}

# Labels that are explicit
EXPLICIT_LABELS = STRICT_NSFW.union({})

# Weak NSFW detection categories
WEAK_NSFW = {
    "BELLY_COVERED",
    "ARMPITS_COVERED",
    "BREAST_EXPOSED",
    "BREAST_COVERED",
    "NIPPLE_EXPOSED",
    "COVERED_BREAST",
    "COVERED_GENITALIA",
    "COVERED_BUTTOCKS",
    "EXPOSED_BELLY",
    "EXPOSED_BREAST",
}

# ViT API Config (fallback when NudeNet finds nothing)
VIT_API_URL = os.environ.get("VIT_API_URL", "https://yuki-nsfw-vit-production.up.railway.app/check")
VIT_FALLBACK = os.environ.get("VIT_FALLBACK", "true").lower() in ("true", "1", "yes")
VIT_THRESHOLD = float(os.environ.get("VIT_THRESHOLD", 0.01))
