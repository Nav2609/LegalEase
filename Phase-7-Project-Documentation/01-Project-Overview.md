# 01 - Project Overview

## Project Name

LegalEase

## Overview

LegalEase is an AI-powered legal document drafting application designed to help users create initial drafts of common legal documents.

The application combines a Streamlit frontend, FastAPI backend, and Google Gemini AI to provide an end-to-end document-generation workflow.

## Problem

Preparing legal documents manually can require significant time and effort.

Users may need to structure information, organize clauses, and format documents before they can review a draft.

LegalEase aims to simplify the initial drafting process through AI-assisted document generation.

## Proposed Solution

LegalEase allows users to provide information about the required document and its terms.

The application sends the information to the backend, which uses Gemini AI to generate a structured legal-document draft.

The generated document can then be reviewed and exported.

## Main Features

The application provides:

- Document type selection
- Party information input
- Terms and conditions input
- Effective date input
- AI-assisted document generation
- Generated document preview
- TXT export
- DOCX export
- PDF export
- Error handling

## Technology Stack

The main technologies used are:

- Python
- Streamlit
- FastAPI
- Google Gemini API
- `google-genai`
- `python-docx`
- ReportLab

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
Preview
  ↓
TXT / DOCX / PDF