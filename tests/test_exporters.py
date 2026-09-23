from docx import Document

from frontend.exporters import (
    format_docx,
    format_html_preview,
    format_pdf,
    sanitize_text,
    terms_from_input,
)


def test_sanitize_text():
    assert sanitize_text("“Hello”—world") == '"Hello"-world'


def test_terms_from_input():
    assert terms_from_input("A; B; ; C") == ["A", "B", "C"]


def test_html_preview():
    result = format_html_preview("TITLE:\nThis is a paragraph.")
    assert "<h4>TITLE:</h4>" in result
    assert "<p>This is a paragraph.</p>" in result


def test_docx_export_is_readable():
    data = format_docx(
        "1. Parties\nA and B agree.",
        "Test Agreement",
        terms=["Payment within 30 days"],
    )
    document = Document(__import__("io").BytesIO(data))
    full_text = "\n".join(p.text for p in document.paragraphs)
    assert "Test Agreement" in full_text
    assert "1. Parties" in full_text


def test_pdf_export_has_pdf_signature():
    data = format_pdf("1. Parties\nA and B agree.", "Test Agreement")
    assert data.startswith(b"%PDF")
