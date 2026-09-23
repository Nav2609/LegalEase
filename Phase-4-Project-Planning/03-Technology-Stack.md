# 03 - Technology Stack

## Overview

LegalEase uses a Python-based technology stack with Streamlit for the frontend, FastAPI for the backend, and Google's Gemini API for AI-assisted document generation.

## Programming Language

### Python

Python is used as the primary programming language for the application.

It is used for:

- Frontend development
- Backend development
- AI integration
- Document generation
- Document export

## Frontend Technology

### Streamlit

Streamlit is used to build the web-based user interface.

It provides:

- User input forms
- Document selection
- Generation controls
- Document preview
- Download buttons

## Backend Technology

### FastAPI

FastAPI is used to build the backend API.

It handles:

- Client requests
- Request validation
- Communication with the AI module
- Responses to the frontend

## Artificial Intelligence

### Google Gemini

Google Gemini is used for AI-assisted legal-document generation.

The application sends structured user information to the Gemini API and receives generated document content.

## AI SDK

### google-genai

The `google-genai` Python package is used to communicate with the Gemini API.

## Document Export

### python-docx

Used for generating DOCX documents.

### ReportLab

Used for generating PDF documents.

TXT documents are generated as plain text.

## Configuration

### python-dotenv

Used to load environment variables such as:

- Gemini API key
- Gemini model configuration
- Backend URL

## Version Control

### Git

Git is used for source-code version control.

### GitHub

GitHub is used to host and manage the project repository.

## Technology Architecture

```text
Python
  |
  +-- Streamlit
  |     |
  |     +-- User Interface
  |
  +-- FastAPI
  |     |
  |     +-- Backend API
  |
  +-- google-genai
  |     |
  |     +-- Gemini AI
  |
  +-- python-docx / ReportLab
        |
        +-- Document Export