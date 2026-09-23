# 04 - AI Integration

## Overview

LegalEase integrates Google's Gemini AI to generate structured legal-document drafts based on information provided by the user.

## AI Technology

The project uses:

- Google Gemini API
- `google-genai` Python package
- Gemini model configured through environment variables

## AI Integration Flow

```text
User Input
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
Gemini Generator
    ↓
Google Gemini API
    ↓
Generated Legal Draft
    ↓
Backend
    ↓
Frontend