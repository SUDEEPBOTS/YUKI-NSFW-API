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
PORT = int(os.environ.get("NSFW_PORT", 7860))
HOST = os.environ.get("NSFW_HOST", "0.0.0.0")
WORKERS = int(os.environ.get("NSFW_WORKERS", 2))

# NudeNet Configuration
NSFW_THRESHOLD = float(os.environ.get("NSFW_THRESHOLD", 0.01))

# Labels to consider as strict NSFW
STRICT_NSFW = {
    "ANUS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
    "MALE_BREAST_EXPOSED",
}

# Labels that are explicit but maybe not strictly blocked
EXPLICIT_LABELS = STRICT_NSFW.union({
    "ARMPITS_EXPOSED",
    "BELLY_EXPOSED",
    "FACE_FEMALE",
    "FACE_MALE",
})
