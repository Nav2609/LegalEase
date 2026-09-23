import os
from io import BytesIO

import requests
import streamlit as st
from dotenv import load_dotenv

from exporters import (
    format_docx,
    format_html_preview,
    format_pdf,
    sanitize_text,
    terms_from_input,
)

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #777;
        margin-top: 0;
        margin-bottom: 28px;
    }
    .preview-card {
        background: #111827;
        color: #f9fafb;
        padding: 24px;
        border-radius: 16px;
        max-height: 620px;
        overflow-y: auto;
        line-height: 1.65;
    }
    .preview-card h4 {
        color: #93c5fd;
        margin-top: 18px;
    }
    .preview-card p {
        margin-bottom: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">⚖️ LegalEase</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-powered legal document drafting and export</div>',
    unsafe_allow_html=True,
)

if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "document_type" not in st.session_state:
    st.session_state.document_type = ""

with st.sidebar:
    st.header("Document Inputs")

    document_type = st.selectbox(
        "Document Type",
        [
            "Employment Contract",
            "Non-Disclosure Agreement (NDA)",
            "Lease Agreement",
            "Freelance Work Contract",
            "Service Agreement",
            "Employment Offer Letter",
            "Custom Agreement",
        ],
    )

    if document_type == "Custom Agreement":
        document_type = st.text_input(
            "Custom document type",
            placeholder="e.g. Partnership Agreement",
        )

    parties = st.text_area(
        "Parties Involved",
        placeholder="Jane Doe (Service Provider), TechNova Inc. (Client)",
        height=110,
    )

    terms = st.text_area(
        "Terms & Conditions",
        placeholder=(
            "Payment within 30 days of invoice; "
            "Provider will deliver work by the deadline; "
            "Confidentiality must be maintained"
        ),
        height=170,
    )

    effective_date = st.text_input(
        "Effective Date",
        placeholder="April 15, 2026",
    )

    logo_file = st.file_uploader(
        "Optional logo",
        type=["png", "jpg", "jpeg"],
        help="Used in DOCX export.",
    )

    generate = st.button(
        "Generate Document",
        type="primary",
        use_container_width=True,
    )

if generate:
    if not all([document_type.strip(), parties.strip(), terms.strip(), effective_date.strip()]):
        st.error("Please fill in document type, parties, terms, and effective date.")
    else:
        payload = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "effective_date": effective_date,
        }

        with st.spinner("Generating your draft with Gemini..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    json=payload,
                    timeout=120,
                )
                response.raise_for_status()
                data = response.json()
                st.session_state.generated_text = data["content"]
                st.session_state.document_type = data["document_type"]
                st.session_state.model = data.get("model", "")
                st.success("Document generated successfully.")
            except requests.RequestException as exc:
                detail = ""
                if getattr(exc, "response", None) is not None:
                    try:
                        detail = exc.response.json().get("detail", "")
                    except Exception:
                        detail = exc.response.text
                st.error(
                    f"Could not reach the backend or Gemini. "
                    f"{detail or str(exc)}"
                )

if st.session_state.generated_text:
    st.subheader("Document Preview")

    preview_tab, edit_tab = st.tabs(["Preview", "Edit Document"])

    with preview_tab:
        st.markdown(
            f'<div class="preview-card">{format_html_preview(st.session_state.generated_text)}</div>',
            unsafe_allow_html=True,
        )

    with edit_tab:
        edited = st.text_area(
            "Edit generated document",
            value=st.session_state.generated_text,
            height=600,
        )
        if st.button("Save Edits", use_container_width=True):
            st.session_state.generated_text = edited
            st.success("Edits saved for this session.")

    st.divider()
    st.subheader("Download")

    current_text = sanitize_text(st.session_state.generated_text)
    doc_type = st.session_state.document_type or "Legal Document"

    logo_bytes = logo_file.getvalue() if logo_file else None
    term_items = terms_from_input(terms)

    txt_bytes = current_text.encode("utf-8")
    docx_bytes = format_docx(
        current_text,
        doc_type,
        logo_bytes=logo_bytes,
        terms=term_items,
    )
    pdf_bytes = format_pdf(current_text, doc_type)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.download_button(
            "Download TXT",
            data=txt_bytes,
            file_name="legalease_document.txt",
            mime="text/plain",
            use_container_width=True,
        )
    with c2:
        st.download_button(
            "Download DOCX",
            data=docx_bytes,
            file_name="legalease_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
        )
    with c3:
        st.download_button(
            "Download PDF",
            data=pdf_bytes,
            file_name="legalease_document.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    st.caption(
        "LegalEase creates AI-generated drafts. Review the final document with a qualified "
        "legal professional before relying on it."
    )
else:
    st.info(
        "Enter the document details in the left sidebar and click Generate Document."
    )
