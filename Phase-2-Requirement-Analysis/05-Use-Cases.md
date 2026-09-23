# 05 - Use Cases

## Overview

Use cases describe the main interactions between users and the LegalEase system.

## Use Case 1 - Select Document Type

**Actor:** User

**Description:**  
The user selects the type of legal document they want to generate.

**Expected Result:**  
The system displays the appropriate input fields for the selected document type.

---

## Use Case 2 - Enter Document Information

**Actor:** User

**Description:**  
The user enters party information, terms and conditions, and the effective date.

**Expected Result:**  
The system accepts and prepares the provided information for document generation.

---

## Use Case 3 - Generate Legal Document

**Actor:** User

**Description:**  
The user submits the entered information to generate a legal-document draft.

**System Action:**

1. The frontend sends the request to the backend.
2. The backend processes the request.
3. The AI generation module sends the information to Gemini.
4. Gemini generates the document draft.
5. The backend returns the generated document.

**Expected Result:**  
The generated legal-document draft is displayed to the user.

---

## Use Case 4 - Review Document

**Actor:** User

**Description:**  
The user reviews the generated document before downloading it.

**Expected Result:**  
The user can inspect the generated content and decide whether to export it.

---

## Use Case 5 - Export Document

**Actor:** User

**Description:**  
The user downloads the generated document in a supported format.

**Available Formats:**

- TXT
- DOCX
- PDF

**Expected Result:**  
The selected document format is downloaded successfully.

---

## Use Case 6 - Handle Generation Error

**Actor:** User

**Description:**  
Document generation may fail because of an API error, network issue, or service unavailability.

**Expected Result:**  
The application displays an appropriate error message instead of failing silently.

---

## Use Case 7 - Legal Review

**Actor:** User / Legal Professional

**Description:**  
The generated document is reviewed before being used for an actual legal purpose.

**Expected Result:**  
The document is treated as an AI-assisted draft and reviewed by a qualified legal professional where appropriate.