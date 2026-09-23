# 06 - Security Documentation

## Overview

Security is an important part of LegalEase because the application processes user-provided legal information and communicates with an external AI service.

The project follows basic security practices to protect credentials, configuration, and application data.

## API Key Protection

The Gemini API key is stored in the `.env` file.

Example:

```env
GEMINI_API_KEY=your_api_key_here