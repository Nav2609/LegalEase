# 07 - Frontend and Backend Integration

## Overview

The LegalEase frontend and backend work together to provide the complete document-generation workflow.

The Streamlit frontend collects user information, while the FastAPI backend processes the request and communicates with the Gemini AI service.

## Integration Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
HTTP Request
  ↓
FastAPI Backend
  ↓
AI Generation Module
  ↓
Gemini API
  ↓
Generated Document
  ↓
FastAPI Response
  ↓
Streamlit Frontend
  ↓
Preview / Export