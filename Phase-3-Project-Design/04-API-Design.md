# 04 - API Design

## Overview

LegalEase uses a FastAPI backend to receive document-generation requests from the Streamlit frontend and return generated legal-document content.

## API Architecture

```text
Streamlit Frontend
        ↓
    FastAPI API
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