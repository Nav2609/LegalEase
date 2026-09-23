# 02 - Database Design

## Overview

The current version of LegalEase does not require a traditional database for its core document-generation workflow.

User-provided information is processed during the document-generation request and is not dependent on a persistent application database.

## Current Design

The current application follows this flow:

```text
User Input
    ↓
Frontend
    ↓
Backend
    ↓
Gemini API
    ↓
Generated Document
    ↓
Export