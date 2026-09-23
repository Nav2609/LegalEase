# 04 - User Guide

## Overview

This guide explains how to use the LegalEase application to generate an AI-assisted legal-document draft.

## Starting the Application

Make sure both the FastAPI backend and Streamlit frontend are running.

Open the Streamlit application in a web browser using the local URL displayed in the terminal.

## Step 1 - Select Document Type

Select the type of legal document that you want to generate.

For example:

- Employment Contract
- Other supported document types

## Step 2 - Enter Party Information

Enter the information about the parties involved in the document.

For an employment contract, this may include:

- Employee name
- Employer name

## Step 3 - Enter Terms and Conditions

Provide the important terms that should be included in the document.

Examples include:

- Salary
- Working days
- Working hours
- Confidentiality requirements
- Leave information
- Termination notice

## Step 4 - Enter Effective Date

Enter the date on which the document should become effective.

## Step 5 - Generate Document

Select the **Generate Document** option.

LegalEase sends the provided information to the backend, which uses Gemini AI to generate the document draft.

## Step 6 - Review the Generated Document

After successful generation, the document is displayed in the application.

Review the generated content carefully.

Check:

- Party information
- Dates
- Terms
- Clauses
- Other important details

## Step 7 - Download the Document

LegalEase provides download options for:

- TXT
- DOCX
- PDF

Select the required format and download the generated document.

## Example Workflow

```text
Select Document Type
        ↓
Enter Party Information
        ↓
Enter Terms
        ↓
Enter Effective Date
        ↓
Generate Document
        ↓
Review Draft
        ↓
Download TXT / DOCX / PDF