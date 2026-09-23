# LegalEase

AI-powered legal document drafting and export application.

## Project Overview

LegalEase is an AI-assisted application that helps users generate structured legal-document drafts using Google Gemini.

The application uses:

- Streamlit for the frontend
- FastAPI for the backend
- Google Gemini for AI-powered document generation
- Python for application development
- TXT, DOCX, and PDF export functionality

## Project Architecture

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
Export Module
 ↓
TXT / DOCX / PDF