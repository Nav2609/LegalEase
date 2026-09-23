# 05 - Module Design

## Overview

LegalEase is divided into separate modules so that each part of the application has a clear responsibility.

## Main Modules

### 1. Frontend Module

**Location:**
`frontend/`

**Main responsibility:**

- Display the user interface.
- Collect user input.
- Send requests to the backend.
- Display generated documents.
- Provide download options.

### 2. Backend Module

**Location:**
`backend/`

**Main responsibility:**

- Receive frontend requests.
- Validate request data.
- Process document-generation requests.
- Return generated content.

### 3. AI Generation Module

**Location:**
`backend/ai_core/`

**Main responsibility:**

- Connect to the Gemini API.
- Prepare the AI generation request.
- Generate the legal-document draft.
- Return the generated content.

### 4. Export Module

**Location:**
`frontend/exporters.py`

**Main responsibility:**

- Convert generated content into supported formats.
- Provide TXT export.
- Provide DOCX export.
- Provide PDF export.

### 5. Configuration Module

The application uses environment variables for configuration values such as the Gemini API key and model name.

Sensitive configuration should remain outside the source code.

## Module Interaction

```text
+-------------------+
| Frontend Module   |
+---------+---------+
          |
          v
+-------------------+
| Backend Module    |
+---------+---------+
          |
          v
+-------------------+
| AI Generation     |
| Module            |
+---------+---------+
          |
          v
+-------------------+
| Gemini API        |
+-------------------+

Generated Content
          |
          v
+-------------------+
| Export Module     |
+---------+---------+
          |
          v
   TXT / DOCX / PDF