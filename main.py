import streamlit as st
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

import os

import zipfile

os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")

st.set_page_config(
    page_title="AI Website Builder",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
    /* Main background gradient */
    .main {
        background: linear-gradient(135deg, #1d3557, #457b9d, #a8dadc);
        padding: 20px;
    }
    /* Title */
    .title {
        color: #f1faee;
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        text-shadow: 2px 2px 5px #000;
        margin-bottom: 30px;
    }
    /* Text area styling */
    .stTextArea textarea {
        background-color: #f1faee !important;
        border-radius: 6px !important;
        border: 2px solid #1d3557 !important;
        font-size: 18px !important;
        color: #1d3557 !important;
    }
    /* Button styling */
    .stButton>button {
        background-color: #e63946 !important;
        color: white !important;
        border-radius: 10px !important;
        font-size: 18px !important;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s;
        border: none;
    }
    .stButton>button:hover {
        background-color: #b82a39 !important;
        transform: scale(1.05);
    }
    /* Download Button */
    .stDownloadButton > button {
        background-color: #2a9d8f !important;
        color: white !important;
        padding: 10px 20px;
        font-size: 18px !important;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stDownloadButton > button:hover {
        background-color: #21867a !important;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1 class='title'> AI AUTOMATION WEBSITE CREATION</h1>", unsafe_allow_html=True)

prompt = st.text_area(" Write about your website idea below:")

if st.button("generate"):
     with st.spinner("Creating your website... Please wait ⏳"):
        message = [("system","""you are an expert in web development creating a professional website.
                    
                    so create html,css,java scripts code for creating a frontend based website professional

                    The output should be in the below format:

                    --html--
                    [html code]
                    --html--
                    
                    --css--
                    [css code]
                    --css--
                    
                    --js--
                    [java script code]
                    --js--
                    
                    """)]
        
        message.append(("user",prompt))

        model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

        response = model.invoke(message)

        with open("index.html","w",encoding="utf-8") as file:
            file.write(response.content.split("--html--")[1])

        with open("style.css","w",encoding="utf-8") as file:
            file.write(response.content.split("--css--")[1])

        with open("scripts.js","w",encoding="utf-8") as file:
            file.write(response.content.split("--js--")[1])


        with zipfile.ZipFile("website.zip","w") as zip:
            zip.write("index.html")
            zip.write("style.css")
            zip.write("scripts.js")

        st.success("🎉 Your website has been created successfully!")

        st.download_button("click to download" ,
            data = open("website.zip","rb"),
            file_name="website.zip" )
            
       
