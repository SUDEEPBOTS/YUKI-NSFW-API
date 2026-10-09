<div align="center">

<img src="assets/banner.png" alt="Yuki NSFW API Banner" width="100%">

# 🔞 𝗬𝗨𝗞𝗜 𝗡𝗦𝗙𝗪 𝗔𝗣𝗜 𝗦𝗘𝗥𝗩𝗘𝗥

### ⚡ 𝗛𝗶𝗴𝗵-𝗦𝗽𝗲𝗲𝗱 𝗔𝗜 𝗜𝗺𝗮𝗴𝗲 𝗠𝗼𝗱𝗲𝗿𝗮𝘁𝗶𝗼𝗻 & 𝗡𝘂𝗱𝗲𝗡𝗲𝘁 𝗗𝗲𝘁𝗲𝗰𝘁𝗶𝗼𝗻 𝗘𝗻𝗴𝗶𝗻𝗲

<p>
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=FF3366&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=60&lines=FastAPI+NSFW+Detector;AI+Powered+Image+Moderation;Strict+NudeNet+Filtering+🛡️;Built+by+SUDEEPBOTS+⚡" alt="Typing SVG" />
</p>

<p>
  <a href="https://github.com/SUDEEPBOTS/YUKI-NSFW-API/stargazers"><img src="https://img.shields.io/github/stars/SUDEEPBOTS/YUKI-NSFW-API?style=for-the-badge&logo=github&color=FF3366&logoColor=white" alt="Stars"></a>
  <a href="https://github.com/SUDEEPBOTS/YUKI-NSFW-API/network/members"><img src="https://img.shields.io/github/forks/SUDEEPBOTS/YUKI-NSFW-API?style=for-the-badge&logo=git&color=FF6B6B&logoColor=white" alt="Forks"></a>
  <a href="https://github.com/SUDEEPBOTS/YUKI-NSFW-API/issues"><img src="https://img.shields.io/github/issues/SUDEEPBOTS/YUKI-NSFW-API?style=for-the-badge&logo=github&color=FFC93C&logoColor=white" alt="Issues"></a>
  <a href="https://github.com/SUDEEPBOTS/YUKI-NSFW-API/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/SUDEEPBOTS/YUKI-NSFW-API/ci.yml?branch=main&style=for-the-badge&logo=githubactions&logoColor=white&label=CI+Pipeline" alt="CI"></a>
</p>

<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NudeNet-ONNX-FF0000?style=flat-square&logo=ai&logoColor=white" alt="NudeNet">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Security-Hardened-success?style=flat-square&logo=shield" alt="Security">
</p>

---

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%">

</div>

## 🎯 𝗪𝗵𝗮𝘁 𝗶𝘀 𝗬𝗨𝗞𝗜 𝗡𝗦𝗙𝗪 𝗔𝗣𝗜?

**𝗬𝗨𝗞𝗜 𝗡𝗦𝗙𝗪 𝗔𝗣𝗜** is an enterprise-grade, privacy-first local AI computer vision microservice engineered for real-time explicit content detection and image moderation. Powered by **FastAPI**, **Uvicorn**, and **NudeNet ONNX Runtime**, it delivers millisecond-level inference on both CPU and GPU environments without relying on third-party cloud moderation APIs.

Designed specifically for automated Telegram moderation bots, web platforms, and community group security filters.

🔒 **Zero Third-Party Dependency** &bull; **Zero Data Logging** &bull; **Instant In-Memory Purging**

<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">
</div>

## 🏗️ 𝗦𝘆𝘀𝘁𝗲𝗺 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲

```mermaid
flowchart LR
    Client["Client / Telegram Bot / Web UI"] -->|HTTP POST /check-nsfw| APIGateway["FastAPI Engine (Port 7860)"]
    APIGateway -->|Multipart Stream| Validator["MIME & Magic Byte Validator"]
    Validator -->|Temp Buffer| VisionEngine["NudeNet 320n ONNX Classifier"]
    VisionEngine -->|Detection Matrix| RuleEngine["Strict / Soft Label Evaluator"]
    RuleEngine -->|Auto Wipe| MemoryCleaner["Secure File Shredder"]
    RuleEngine -->|JSON Verdict| Response["{'is_nsfw': bool, 'predictions': [...]}"]
    Response --> Client
```

<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">
</div>

## ✨ 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀

<table>
<tr>
<td>

### 🧠 𝗔𝗜 𝗗𝗲𝘁𝗲𝗰𝘁𝗶𝗼𝗻 𝗠𝗮𝘁𝗿𝗶𝘅
- NudeNet 320n ONNX CPU-optimized inference
- Detects exposed body parts, explicit nudity, and suggestive poses
- Granular confidence thresholds (`NSFW_THRESHOLD`)
- Distinguishes strict violations vs warning soft-labels

</td>
<td>

### 🛡️ 𝗣𝗿𝗶𝘃𝗮𝗰𝘆 & 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆
- Automatic instant unlinking of inspected media
- Zero persistence: images never saved to permanent disk or database
- Sanitized environment variable configuration
- Rate-limiting and production WSGI worker clustering

</td>
</tr>
<tr>
<td>

### 🚀 𝗛𝗶𝗴𝗵 𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲
- Asynchronous FastAPI non-blocking endpoints
- Multi-worker Uvicorn process manager
- Sub-second classification for standard image payloads
- Native support for JPEG, PNG, WEBP, and GIF frames

</td>
<td>

### 💻 𝗜𝗻𝘁𝗲𝗿𝗮𝗰𝘁𝗶𝘃𝗲 𝗪𝗲𝗯 𝗦𝘁𝘂𝗱𝗶𝗼
- Modern Cyberpunk inspection console (`index.html`)
- Live drag-and-drop image scanning laser simulation
- Bounding box telemetry and raw JSON inspector
- Built-in REST API interactive testing sandbox

</td>
</tr>
</table>

<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">
</div>

## 📡 𝗔𝗣𝗜 𝗘𝗻𝗱𝗽𝗼𝗶𝗻𝘁𝘀

| Method | Endpoint | Description | Auth |
| :--- | :--- | :--- | :--- |
| `POST` | `/check-nsfw` | Upload an image file for full explicit content detection | Optional Token |
| `GET` | `/health` | Server health check and uptime probe | Public |
| `GET` | `/metrics` | Prometheus metrics and worker status | Public |
| `GET` | `/docs` | Interactive Swagger UI API documentation | Public |

### 🔍 Example Request (`curl`)

```bash
curl -X POST "http://localhost:7860/check-nsfw" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@test_image.jpg"
```

### 📋 Example Response

```json
{
  "is_nsfw": true,
  "status": "DETECTED",
  "score": 0.9824,
  "labels": [
    {
      "class": "FEMALE_BREAST_EXPOSED",
      "score": 0.9824,
      "box": [124, 210, 340, 480]
    }
  ],
  "processing_time_ms": 32.4
}
```

<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">
</div>

## 🚀 𝗗𝗲𝗽𝗹𝗼𝘆𝗺𝗲𝗻𝘁

### ☁️ 𝗢𝗻𝗲-𝗖𝗹𝗶𝗰𝗸 𝗗𝗲𝗽𝗹𝗼𝘆

<p align="left">
  <a href="https://heroku.com/deploy?template=https://github.com/SUDEEPBOTS/YUKI-NSFW-API">
    <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku">
  </a>
  &nbsp;
  <a href="https://render.com/deploy?repo=https://github.com/SUDEEPBOTS/YUKI-NSFW-API">
    <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
  </a>
  &nbsp;
  <a href="https://app.koyeb.com/deploy?type=git&repository=github.com/SUDEEPBOTS/YUKI-NSFW-API&branch=main&name=yuki-nsfw-api">
    <img src="https://www.koyeb.com/static/images/deploy/button.svg" alt="Deploy to Koyeb">
  </a>
</p>

### 🐳 𝗗𝗼𝗰𝗸𝗲𝗿 / 𝗗𝗼𝗰𝗸𝗲𝗿 𝗖𝗼𝗺𝗽𝗼𝘀𝗲

```bash
# Clone the repository
git clone https://github.com/SUDEEPBOTS/YUKI-NSFW-API.git
cd YUKI-NSFW-API

# Launch with Docker Compose
docker compose up -d --build
```

### ⚡ 𝗟𝗼𝗰𝗮𝗹 𝗩𝗣𝗦 𝗤𝘂𝗶𝗰𝗸 𝗦𝗲𝘁𝘂𝗽

```bash
# 1️⃣ Clone the repository
git clone https://github.com/SUDEEPBOTS/YUKI-NSFW-API.git
cd YUKI-NSFW-API

# 2️⃣ Configure environment
cp sample.env .env

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run with production script or python
bash nsfw_start.sh
```

<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">
</div>

## ⚙️ 𝗖𝗼𝗻𝗳𝗶𝗴𝘂𝗿𝗮𝘁𝗶𝗼𝗻

Control the strictness and server settings via `.env` or `config.py`:

```env
PORT=7860
WORKERS=2
NSFW_THRESHOLD=0.01
LOG_LEVEL=INFO
```

Strict detection labels configured out of the box:
```python
STRICT_NSFW = {
    "ANUS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
}
```

<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%">
</div>

## 📜 𝗟𝗶𝗰𝗲𝗻𝘀𝗲

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

---

<div align="center">

### ⭐ 𝗦𝘁𝗮𝗿 𝘁𝗵𝗶𝘀 𝗿𝗲𝗽𝗼 𝗶𝗳 𝘆𝗼𝘂 𝗳𝗼𝘂𝗻𝗱 𝗶𝘁 𝘂𝘀𝗲𝗳𝘂𝗹!

<p>
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=FF3366&center=true&vCenter=true&repeat=true&width=400&height=30&lines=Made+with+%E2%9D%A4%EF%B8%8F+by+SUDEEPBOTS" alt="Footer" />
</p>

<a href="https://github.com/SUDEEPBOTS">
  <img src="https://img.shields.io/badge/GitHub-SUDEEPBOTS-181717?style=for-the-badge&logo=github" alt="GitHub">
</a>
<a href="https://t.me/SUDEEPBOTS">
  <img src="https://img.shields.io/badge/Telegram-SUDEEPBOTS-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
</a>

</div>
