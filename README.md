# 📧 AI Email Assistant & Intelligent NLP Auto-Responder

<div align="center">

[![CI](https://github.com/amirthn6533/ai-email-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/amirthn6533/ai-email-assistant/actions)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**An intelligent, offline-capable email analyzer and reply generator powered by Natural Language Processing (NLP) and modern transformer models.**

[Overview](#-overview) • [Key Features](#-key-features) • [Architecture](#-architecture) • [Quick Start](#-quick-start) • [Usage](#-usage) • [License](#-license)

</div>

---

## 📌 Overview

Managing high-volume inboxes is time-consuming. **AI Email Assistant** automatically parses incoming emails, evaluates sender intent and urgency, extracts core action points, generates concise summaries, and crafts context-aware response drafts—all wrapped in an intuitive **Streamlit** dashboard.

---

## 🚀 Key Features

- 🧠 **Intent & Priority Scoring:** Automatically ranks incoming messages into High, Normal, and Low priority tiers based on semantic urgency.
- 📝 **Abstractive Summarization:** Condenses long communication threads into clear bullet points using HuggingFace Transformers.
- ✍️ **Contextual Reply Generation:** Drafts professional, courteous responses tailored to the tone of the sender.
- 📬 **Gmail API Integration:** Seamlessly fetches unread emails and synchronizes status updates.
- 💾 **Local SQLite Storage:** Securely indexes emails and generated drafts locally without third-party cloud exposure.
- 🔒 **Privacy First:** Supports local offline models for zero data leakage.

---

## 🏗️ Architecture

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│   Gmail API /   │ ───►  │  NLP Pipeline   │ ───►  │ Streamlit Web   │
│   Email Input   │       │  (Transformers) │       │   Dashboard     │
└─────────────────┘       └────────┬────────┘       └─────────────────┘
                                   │
                                   ▼
                          ┌─────────────────┐
                          │ SQLite Database │
                          │  (emails.db)    │
                          └─────────────────┘
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- Virtual environment (recommended)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/amirthn6533/ai-email-assistant.git
cd ai-email-assistant

# 2. Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Launch the Streamlit application
streamlit run app.py
```

---

## 💻 Tech Stack

- **Core:** Python 3.10+
- **Machine Learning & NLP:** HuggingFace `transformers`, `torch`, `nltk`
- **UI Framework:** Streamlit
- **Persistence:** SQLite3
- **Integrations:** Google API Client / Gmail API

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
