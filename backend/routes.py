from fastapi import APIRouter, HTTPException

from .ai_core.gemini_generator import GeminiDocumentGenerator
from .schemas import DocumentRequest, DocumentResponse

router = APIRouter()
_generator = None


def get_generator() -> GeminiDocumentGenerator:
    global _generator
    if _generator is None:
        _generator = GeminiDocumentGenerator()
    return _generator


@router.get("/")
def root():
    return {
        "name": "LegalEase API",
        "status": "running",
        "message": "AI-powered legal document generation API",
    }


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/generate", response_model=DocumentResponse)
def generate_document(request: DocumentRequest):
    try:
        generator = get_generator()
        content = generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            effective_date=request.effective_date,
        )
        return DocumentResponse(
            document_type=request.document_type,
            content=content,
            model=generator.model,
        )
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"AI generation failed: {exc}",
        ) from exc
