# LegalEase — AI-Powered Legal Document Generator

LegalEase is a complete FastAPI + Streamlit application for generating editable legal-document drafts with Google Gemini and exporting them to TXT, DOCX, and PDF.

## Important model update
The supplied project document selected `gemini-1.5-pro`. Google retired the Gemini 1.5 models on September 29, 2025, so this implementation keeps the model configurable but defaults to the current `gemini-3.8-flash` model. This avoids building against a retired model. See Google's current Gemini model/deprecation documentation.

## Features
- Streamlit frontend
- FastAPI backend
- Google Gemini integration through the current `google-genai` SDK
- Employment contracts, NDAs, lease agreements, contracts, and custom document types
- Editable preview
- TXT, DOCX, and PDF exports
- Optional logo upload for DOCX/PDF
- Terms table in DOCX
- Header/footer branding
- Input validation and error handling
- Health endpoint
- Automated tests
- Docker support

## Project structure

```text
LegalEase/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   └── ai_core/
│       ├── __init__.py
│       └── gemini_generator.py
├── frontend/
│   ├── __init__.py
│   ├── app.py
│   └── exporters.py
├── assets/
│   └── logo.svg
├── tests/
│   ├── test_api.py
│   └── test_exporters.py
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── Procfile
├── requirements.txt
└── README.md
```

## 1. Requirements

- Python 3.10+
- VS Code
- A Gemini API key
- Internet connection for Gemini generation

## 2. Windows setup in VS Code

Open the LegalEase folder in VS Code and open Terminal.

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Gemini key:

```env
GEMINI_API_KEY=your_real_key_here
GEMINI_MODEL=gemini-3.8-flash
BACKEND_URL=http://127.0.0.1:8000
```

Never commit `.env`.

## 3. Start the backend

Terminal 1:

```powershell
.venv\Scripts\activate
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```

Check:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs

## 4. Start the Streamlit frontend

Terminal 2:

```powershell
.venv\Scripts\activate
streamlit run frontend/app.py
```

Open the URL Streamlit prints, normally:

```text
http://localhost:8501
```

## 5. How to test

### Automated tests

With the virtual environment active:

```powershell
pytest -q
```

The tests do not call Gemini. They validate the API contract and document exporters.

### Manual end-to-end test

1. Start FastAPI.
2. Start Streamlit.
3. Choose a document type.
4. Enter parties.
5. Enter terms separated by semicolons.
6. Enter an effective date.
7. Optionally upload a logo.
8. Click **Generate Document**.
9. Review the preview.
10. Edit the generated text if needed.
11. Download TXT, DOCX, or PDF.

## 6. Example input

Document type:

```text
Freelance Work Contract
```

Parties:

```text
Jane Doe (Service Provider), TechNova Inc. (Client)
```

Terms:

```text
Payment within 30 days of invoice; Provider will deliver work by the agreed deadline; Confidentiality must be maintained; Either party may terminate with 15 days notice
```

Effective date:

```text
April 15, 2026
```

## Legal-use note

LegalEase generates drafts and general legal-language content. It is not a law firm and does not replace review by a qualified lawyer. The application prompt explicitly asks the model not to invent statutes, citations, or jurisdiction-specific legal claims when they are not supplied by the user.

## Deployment

### Docker

```powershell
docker compose up --build
```

Backend: `http://localhost:8000`

The Streamlit service is available at `http://localhost:8501`.

For production, set secrets through your hosting provider rather than committing `.env`.

## Architecture

```text
Streamlit
   |
   | POST /generate
   v
FastAPI
   |
   v
GeminiDocumentGenerator
   |
   v
Google Gemini API

Generated text
   |
   +--> Editable Streamlit preview
   +--> TXT
   +--> DOCX
   +--> PDF
```
