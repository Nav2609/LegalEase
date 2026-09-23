from io import BytesIO
import html
import re
from typing import Iterable

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Inches, Pt
from fpdf import FPDF


def sanitize_text(text: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()


def terms_from_input(terms: str) -> list[str]:
    return [item.strip() for item in terms.split(";") if item.strip()]


def format_html_preview(text: str) -> str:
    safe = html.escape(sanitize_text(text))
    paragraphs = [p.strip() for p in safe.split("\n") if p.strip()]
    rendered = []
    for paragraph in paragraphs:
        if re.match(r"^(\d+[\.\)]|[A-Z][A-Z\s]{4,}:)$", paragraph):
            rendered.append(f"<h4>{paragraph}</h4>")
        else:
            rendered.append(f"<p>{paragraph}</p>")
    return "\n".join(rendered)


def format_docx(
    text: str,
    doc_type: str,
    logo_bytes: bytes | None = None,
    terms: Iterable[str] | None = None,
) -> bytes:
    document = Document()
    section = document.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

    if logo_bytes:
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture(BytesIO(logo_bytes), width=Inches(1.15))

    title = document.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = title.add_run(doc_type.upper())
    run.bold = True
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)

    for raw in sanitize_text(text).splitlines():
        line = raw.strip()
        if not line:
            continue
        p = document.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(line)
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)

    term_list = list(terms or [])
    if term_list:
        document.add_paragraph()
        heading = document.add_paragraph()
        r = heading.add_run("KEY TERMS")
        r.bold = True
        r.font.name = "Times New Roman"

        table = document.add_table(rows=1, cols=2)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.style = "Table Grid"
        table.rows[0].cells[0].text = "No."
        table.rows[0].cells[1].text = "Term / Condition"

        for index, term in enumerate(term_list, start=1):
            cells = table.add_row().cells
            cells[0].text = str(index)
            cells[1].text = term

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("LegalEase — AI-generated draft | Review before use").font.size = Pt(8)

    output = BytesIO()
    document.save(output)
    return output.getvalue()


class LegalEasePDF(FPDF):
    def __init__(self, doc_type: str, logo_bytes: bytes | None = None):
        super().__init__()
        self.doc_type = doc_type
        self.logo_bytes = logo_bytes

    def header(self):
        if self.logo_bytes:
            # FPDF needs a filename for images, so logo is intentionally omitted here.
            # The Streamlit layer can use the DOCX exporter for image embedding.
            pass
        self.set_font("Helvetica", "B", 10)
        self.cell(0, 8, self.doc_type[:70], align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "", 8)
        self.cell(0, 10, f"LegalEase | Page {self.page_no()} | AI-generated draft", align="C")


def format_pdf(text: str, doc_type: str) -> bytes:
    pdf = LegalEasePDF(doc_type)
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 15)
    pdf.multi_cell(0, 9, sanitize_text(doc_type), align="C")
    pdf.ln(4)

    pdf.set_font("Helvetica", "", 11)
    for line in sanitize_text(text).splitlines():
        line = line.strip()
        if not line:
            pdf.ln(3)
            continue
        pdf.multi_cell(0, 6, line)
        pdf.ln(1)

    return bytes(pdf.output())
