# 01 - System Architecture

## Overview

LegalEase follows a simple layered architecture consisting of a frontend, backend, AI generation module, and document export functionality.

## Architecture

```text
+----------------------+
|        User          |
+----------+-----------+
           |
           v
+----------------------+
| Streamlit Frontend   |
|      app.py          |
+----------+-----------+
           |
           v
+----------------------+
|   FastAPI Backend    |
|   Request Handling   |
+----------+-----------+
           |
           v
+----------------------+
|   AI Generation      |
| Gemini Integration   |
+----------+-----------+
           |
           v
+----------------------+
|     Gemini API       |
+----------+-----------+
           |
           v
+----------------------+
| Generated Document   |
+----------+-----------+
           |
           v
+----------------------+
|    Export Module     |
| TXT / DOCX / PDF     |
+----------------------+