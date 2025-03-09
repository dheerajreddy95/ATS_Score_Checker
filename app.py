import base64
import io

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GENAI_API_KEY"))

def get_gemini_response(input,pdf_cotent,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    input=[
        {"text" : input+"\n"+prompt},pdf_content[0]
    ]
    response=model.generate_content(input)
    return response.text

def input_pdf_setup(uploaded_file):
    ## Covert the PDF to image
    images=pdf2image.convert_from_bytes(uploaded_file.read())

    first_page=images[0]

    ##Convert to bytes
    img_byte_arr = io.BytesIO()
    first_page.save(img_byte_arr, format='JPEG')
    img_byte_arr=img_byte_arr.getvalue()

    pdf_parts=[
    {
        "mime_type":"image/jpeg",
        "data":base64.b64encode(img_byte_arr).decode()   # enocde to base64
    }
    ]
    return pdf_parts
    


## Streamlit App

st.set_page_config(page_title="ATS Resume Expert",page_icon="📄",layout="centered",initial_sidebar_state="expanded")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ", key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

linkedin_url=None

if uploaded_file is not None:
    st.write("Resume Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")


submit2 = st.button("Percentage Match")

submit3 = st.button("What Skills are missing and How to improvise those Skills")   

submit4 = st.button("How to Tailor Your Resume to a Job Description")


input_prompt1 ="""You have worked with companies like Google, Amazon and Microsoft, Meta, Netflix  and you are an experienced HR with tech Experience in the filed of any one job roles from data science and machine learning, Full Stack Developer, Software Egineer, Software Developer, AI ENgineer, ML Engineer, Data Scientist, Data Engineer, Data Analayist, Web Developer, Devops.
Your task is to review the provided resume against the job description for these profiles and provide a detailed analysis of the resume.
Please share your professional evaluation on whether the candidate's profile aligns with the job description and highlight the strengths and weaknesses of the candidate's profile in relation to the specified job description."""


input_prompt2= """ You are a skilled and well trained ATS (Applicant Tracking System) scanner with a deep understanding of any one the job roles in the field of data science and machine learning, Full Stack Developer, Software Egineer, Software Developer, AI ENgineer, ML Engineer, Data Scientist, Data Engineer, Data Analayist, Web Developer, Devops.
and deep ATS functionality, ypur task is to evaluate the resume against the provided job description and give me the percentage match of the resume with the job description. First the output should come as percentage and then keywords missing in the resume."""


input_prompt3="""Compare my resume with the following job description and identify missing skills. Provide recommendations on how I can improve to match the requirements."""

input_prompt4="""You are an expert career coach and a skilled ATS (Applicant Tracking System) specialist with extensive knowledge of resume optimization for various job roles, including Data Scientist, ML Engineer, Software Developer, AI Engineer, and more. Your task is to analyze the provided resume and job description, then provide a step-by-step guide on tailoring the resume to improve its relevance and increase its chances of passing ATS scans and impressing recruiters.

Your response should include:

Key missing skills and keywords that should be added to align with the job description.
Sections to modify (e.g., experience, skills, summary) to better match the job role.
How to restructure the resume for better readability and ATS compatibility.
Tips on phrasing accomplishments using action-oriented language and quantifiable results.
Any additional recommendations to make the resume stand out.
Provide a structured and detailed response to help the candidate effectively tailor their resume."""



if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2: 
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

    
