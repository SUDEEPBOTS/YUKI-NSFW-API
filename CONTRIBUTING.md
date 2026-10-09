# 🤝 Contributing to Yuki NSFW API

Thank you for your interest in contributing to **Yuki NSFW API**! We welcome contributions ranging from bug reports and documentation enhancements to major feature additions.

---

## 📜 Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before interacting with the repository or submitting pull requests.

---

## 🛠️ Development Workflow

1. **Fork the Repository**:
   Click the "Fork" button on the top right of the GitHub page.

2. **Clone your fork**:
   ```bash
   git clone https://github.com/<your-username>/YUKI-NSFW-API.git
   cd YUKI-NSFW-API
   ```

3. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/my-awesome-improvement
   ```

4. **Install Dependencies & Set Up Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cp sample.env .env
   ```

5. **Make Changes and Test**:
   Ensure all Python files compile cleanly:
   ```bash
   python -m py_compile $(find . -name "*.py" -not -path "*/.*")
   ```

6. **Commit & Push**:
   ```bash
   git commit -m "feat(filter): add fine-grained confidence threshold"
   git push origin feature/my-awesome-improvement
   ```

7. **Submit a Pull Request**:
   Open a PR against the `main` branch of `SUDEEPBOTS/YUKI-NSFW-API`.

---

## 📌 Coding Standards

- Write clean, asynchronous code utilizing modern `FastAPI` best practices.
- Ensure all computer vision operations handle invalid or corrupted images gracefully.
- Do not commit sensitive tokens, sessions, or personal keys.
- Add descriptive docstrings and inline comments where necessary.
