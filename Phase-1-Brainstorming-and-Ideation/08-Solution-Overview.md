# 08 - Solution Overview

## Proposed Solution

LegalEase is an AI-powered web application designed to assist users in creating structured legal-document drafts.

The system allows users to provide basic document information through a simple interface. This information is processed by the backend and sent to Google's Gemini AI for document generation.

## System Workflow

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Gemini AI
  ↓
Generated Legal Document
  ↓
Frontend Preview
  ↓
TXT / DOCX / PDF Export