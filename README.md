                                                                                    ### ATS Resume Expert

This repository hosts a Streamlit app designed to help users optimize their resumes for ATS (Applicant Tracking Systems). It enables users to upload their resumes (in PDF format) and analyze them against a provided job description. The app leverages Google's Gemini model API to offer detailed responses, such as:

- Resume analysis and evaluation.
- Percentage match between the resume and job description.
- Identification of missing skills and suggestions for improvement.
- Tailoring the resume to match a specific job description.

## Features

- **Job Description Analysis**: Users can paste a job description to evaluate how well their resume matches the specified job role.
- **Resume Upload**: Users can upload a PDF version of their resume for analysis.
- **ATS Evaluation**: The app evaluates the resume based on ATS functionalities, providing a percentage match and missing keywords.
- **Tailored Resume Advice**: Offers tailored advice on how to improve the resume based on the job description provided.

## Prerequisites

- Python 3.x
- Required Python libraries (installed via `requirements.txt`)

### Libraries
- `streamlit` - For the frontend web interface.
- `pdf2image` - For converting PDF pages to images.
- `google-generativeai` - For generating responses via the Google Gemini API.
- `dotenv` - For managing environment variables like the API key.
