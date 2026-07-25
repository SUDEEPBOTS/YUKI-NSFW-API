# Copyright (c) 2025 @SUDEEPBOTS <HellfireDevs>
# Location: delhi,noida
#
# All rights reserved.
#
# This code is the intellectual property of SUDEEPBOTS.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.

import os

# Server Configuration
PORT = int(os.environ.get("PORT", os.environ.get("NSFW_PORT", 7860)))
HOST = os.environ.get("NSFW_HOST", "0.0.0.0")
WORKERS = int(os.environ.get("NSFW_WORKERS", 2))

# NudeNet Configuration
NSFW_THRESHOLD = float(os.environ.get("NSFW_THRESHOLD", 0.001))
WEAK_THRESHOLD = float(os.environ.get("WEAK_THRESHOLD", 0.080))

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

# Labels that are explicit but need higher threshold
EXPLICIT_LABELS = STRICT_NSFW.union({
    "FACE_FEMALE",
    "FACE_MALE",
})

# Weak NSFW — sirf high threshold pe trigger karein
WEAK_NSFW = {
    "FACE_FEMALE",
    "FACE_MALE",
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
