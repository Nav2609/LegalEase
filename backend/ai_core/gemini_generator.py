import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env", override=True)
import os
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


class GeminiDocumentGenerator:
    """Generate legal-document drafts using Google's current GenAI SDK."""

    def __init__(self, model: Optional[str] = None):
        self.api_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.model = model or os.getenv("GEMINI_MODEL", "gemini-3.6-flash").strip()

        if not self.api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured. Copy .env.example to .env "
                "and add your Gemini API key."
            )

        self.client = genai.Client(api_key=self.api_key)

    def build_prompt(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str,
    ) -> str:
        return f"""
You are LegalEase, an AI assistant that drafts structured legal-document templates.

Create a professional DRAFT of the requested document using only the facts supplied below.

DOCUMENT TYPE:
{document_type}

PARTIES:
{parties}

TERMS / CONDITIONS:
{terms}

EFFECTIVE DATE:
{effective_date}

Requirements:
1. Produce a complete, editable document draft.
2. Use clear legal-document structure: title, parties, recitals/background when useful,
   definitions when useful, numbered sections, obligations, payment/term/termination
   provisions when applicable, confidentiality when applicable, governing-law placeholder
   when jurisdiction was not supplied, and signature blocks.
3. Preserve every material user-supplied fact.
4. Do not invent names, dates, addresses, monetary amounts, statutes, regulations,
   case citations, or jurisdiction-specific legal requirements.
5. If a necessary legal detail was not supplied, use a neutral placeholder such as
   [GOVERNING LAW] rather than inventing it.
6. Do not include Markdown code fences.
7. Return plain text with readable headings and numbered clauses.
8. This is a drafting aid, not legal advice. Do not claim that the document is legally
   valid or enforceable in a particular jurisdiction.
""".strip()

    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str,
    ) -> str:
        prompt = self.build_prompt(document_type, parties, terms, effective_date)

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.35,
                max_output_tokens=7000,
            ),
        )

        text = (response.text or "").strip()
        if not text:
            raise RuntimeError("Gemini returned an empty response.")

        return text
