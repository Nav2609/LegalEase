# 02 - System Documentation

## Overview

LegalEase follows a modular architecture in which the frontend, backend, AI generation module, and document export functionality work together to provide the complete application workflow.

## System Architecture

```text
+----------------------+
|   Streamlit Frontend |
+----------+-----------+
           |
           | HTTP Request
           ↓
+----------------------+
|    FastAPI Backend   |
+----------+-----------+
           |
           ↓
+----------------------+
|   Gemini Generator   |
+----------+-----------+
           |
           ↓
+----------------------+
|    Google Gemini     |
+----------+-----------+
           |
           ↓
   Generated Document
           |
           ↓
+----------------------+
|   Export Functions   |
+----------+-----------+
           |
     +-----+-----+
     ↓     ↓     ↓
    TXT   DOCX   PDF