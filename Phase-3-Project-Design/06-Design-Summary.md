# 06 - Design Summary

## Phase Overview

Phase 3 defines the technical and functional design of the LegalEase application.

The design describes the system architecture, user interface, API structure, database considerations, and internal modules.

## System Architecture

LegalEase follows a layered architecture:

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
AI Generation Module
  ↓
Gemini API
  ↓
Generated Document
  ↓
Export Module
  ↓
TXT / DOCX / PDF