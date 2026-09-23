# 01 - Demo Plan

## Overview

The LegalEase demonstration presents the main features and workflow of the completed application.

The goal is to demonstrate how a user can provide information and generate an AI-assisted legal document.

## Demo Objectives

The demonstration will show:

- Application startup
- Streamlit frontend
- Backend API
- Document type selection
- User input
- AI-powered document generation
- Generated document review
- Document export

## Demo Environment

The demonstration requires:

- Python environment
- Project dependencies
- Gemini API key configured in `.env`
- FastAPI backend running
- Streamlit frontend running
- Internet connection for Gemini API access

## Demonstration Sequence

### Step 1 - Start Backend

Start the FastAPI backend and verify that the API is running.

### Step 2 - Start Frontend

Launch the Streamlit application and open it in the browser.

### Step 3 - Select Document Type

Choose a supported legal document type.

### Step 4 - Enter Information

Enter the required parties, terms, dates, and other relevant information.

### Step 5 - Generate Document

Submit the information and allow the Gemini-powered backend to generate the document.

### Step 6 - Review Document

Review the generated legal-document content in the application.

### Step 7 - Export Document

Demonstrate the available export options, such as:

- TXT
- DOCX
- PDF

## Demonstration Example

A suitable demonstration can use an Employment Contract with sample information such as:

- Employee: John Doe
- Employer: TechNova Inc.
- Salary: INR 60,000/month
- Working days: Monday-Friday
- Working hours: 9 AM-6 PM
- Confidentiality requirement
- Paid leave
- Termination notice
- Effective date

All demonstration information should be fictional or appropriately anonymized.

## Expected Result

The demonstration should show that LegalEase can:

1. Accept structured user input.
2. Send the request to the backend.
3. Generate a legal-document draft using Gemini.
4. Display the generated content.
5. Export the document into supported formats.

## Demo Duration

A short demonstration can be completed in approximately:

**5-10 minutes**

## Demo Preparation

Before the demonstration:

- Verify the backend starts successfully.
- Verify the frontend starts successfully.
- Confirm the Gemini API configuration.
- Test document generation.
- Test at least one export format.
- Keep sample input ready.
- Close unnecessary applications and windows.

## Demo Conclusion

The demonstration should conclude by showing the complete workflow from user input to generated and exported legal document.