# ⚖️ LegalEase

### AI-Powered Legal Document Drafting and Export Platform

LegalEase is an AI-powered application designed to help users generate structured legal documents from simple inputs. It uses Google's Gemini API to transform user-provided document details, parties, terms, and effective dates into professionally structured legal-document drafts.

The application provides a simple web interface for entering document information and allows users to preview and export generated documents in multiple formats.

---

## 🚀 Features

- 🤖 AI-powered legal document generation using Google Gemini
- 📝 Simple document input interface
- 📄 Supports structured legal-document drafting
- 👥 Input fields for parties involved
- 📅 Effective-date selection
- 📋 Terms and conditions input
- 👀 Generated document preview
- 📥 Export generated documents as:
  - TXT
  - DOCX
  - PDF
- 🖼️ Optional logo upload
- 🔌 FastAPI backend
- 🎨 Streamlit frontend
- 🔐 API key configuration through environment variables

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Frontend web interface |
| FastAPI | Backend API |
| Google Gemini | AI document generation |
| python-dotenv | Environment configuration |
| python-docx | DOCX document generation |
| ReportLab | PDF generation |

---

## 📁 Project Structure

```text
LegalEase/
│
├── backend/
│   ├── ai_core/
│   │   ├── gemini_generator.py
│   │   └── __init__.py
│   │
│   ├── main.py
│   ├── routes.py
│   └── schemas.py
│
├── frontend/
│   ├── app.py
│   ├── exporters.py
│   └── __init__.py
│
├── tests/
│   ├── test_api.py
│   └── test_exporters.py
│
├── assets/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── Procfile
├── requirements.txt
└── README.md