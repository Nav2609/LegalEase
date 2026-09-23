# 05 - Export Testing

## Overview

Export testing verifies that LegalEase can successfully convert generated legal-document content into the supported download formats.

The supported formats are:

- TXT
- DOCX
- PDF

## Export Testing Objectives

The main objectives are:

- Verify that each export format is generated correctly.
- Verify that generated files can be downloaded.
- Verify that the document content is preserved.
- Verify that exported files can be opened successfully.
- Identify export-related errors.

## TXT Export Testing

The TXT export should be tested to verify that:

- A `.txt` file is created.
- The generated document text is preserved.
- The file can be downloaded.
- The file can be opened using a text editor.

## DOCX Export Testing

The DOCX export should be tested to verify that:

- A `.docx` file is created.
- The generated document content is included.
- The file can be downloaded.
- The document opens correctly in a compatible word processor.

## PDF Export Testing

The PDF export should be tested to verify that:

- A `.pdf` file is created.
- The generated content is included.
- The file can be downloaded.
- The PDF opens correctly in a compatible PDF viewer.

## Export Test Cases

| Test ID | Format | Test Case | Expected Result |
|---|---|---|---|
| EX-01 | TXT | Export generated document as TXT | TXT file created successfully |
| EX-02 | TXT | Open downloaded TXT file | Content is readable |
| EX-03 | DOCX | Export generated document as DOCX | DOCX file created successfully |
| EX-04 | DOCX | Open downloaded DOCX file | Content is displayed correctly |
| EX-05 | PDF | Export generated document as PDF | PDF file created successfully |
| EX-06 | PDF | Open downloaded PDF file | Content is displayed correctly |

## Content Verification

The exported files should contain the generated document content.

The following should be checked:

- Document title
- Party information
- Terms and conditions
- Effective date
- Generated clauses
- Overall document text

## File Validation

Each exported file should be checked for:

- Correct file extension
- Successful download
- Correct file format
- Successful opening
- Preserved content

## Export Testing Goal

The goal is to verify that LegalEase reliably converts generated legal-document drafts into usable TXT, DOCX, and PDF files.