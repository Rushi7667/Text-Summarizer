import streamlit as st
from txtai.pipeline import Summary, Textractor
from PyPDF2 import PdfReader
from webpage_summarizer import summarize_url

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

st.set_page_config(layout="wide")

def text_summary(text, maxlength=None):
    #create summary instance
    summary = Summary()
    text = (text)
    result = summary(text,maxlength=150)
    return result

def extract_text_from_pdf(file_path):
    # Open the PDF file using PyPDF2
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

# getting text from url
def get_text(url):
	page = urlopen(url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
	return fetched_text

choice = st.sidebar.selectbox("Select your choice", ["Summarize Text", "Summarize Document", "Summarize url"])

if choice == "Summarize Text":
    st.subheader("Summarize Text")
    input_text = st.text_area("Enter your text here")
    if input_text is not None:
        if st.button("Summarize Text"):
            col1, col2 = st.columns([1,1])
            with col1:
                st.markdown("**Your Input Text**")
                st.info(input_text)
            with col2:
                st.markdown("**Summary Result**")
                result = text_summary(input_text)
                st.success(result)

elif choice == "Summarize Document":
    st.subheader("Summarize Document")
    st.write("Rushi Lunagariya")
    input_file = st.file_uploader("Upload your document here", type=['pdf'])
    if input_file is not None:
        if st.button("summarize document"):
            with open("doc_file.pdf", "wb") as f:
                f.write(input_file.getbuffer())
            col1,col2 = st.columns([1,1])

            with col1:
                st.info("File uploaded successfully")
                extracted_text = extract_text_from_pdf("doc_file.pdf")
                st.markdown("**Extracted Text is Below**")
                st.info(extracted_text)
            with col2:
                st.markdown("**Summary Result**")
                text = extract_text_from_pdf("doc_file.pdf")
                doc_summary = text_summary(text)
                st.success(doc_summary)

elif choice == "Summarize url":
    st.subheader("Summarize url")

    # Input: URL
    url = st.text_input("Enter the URL of the webpage:")

    # Input: Number of Sentences for Summary
    sentences_count = st.slider("Select the number of sentences for the summary:", 1, 10, 3)

    if st.button("Summarize"):
        if url:
            st.write("Summarizing... Please wait.")
            try:
                summary = summarize_url(url, sentences_count)
                st.subheader("Summary:")
                st.write(summary)

            except Exception as e:
                st.error(f"Error during summarization: {e}")

        else:
            st.warning("Please enter a valid URL.")