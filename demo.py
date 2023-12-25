import streamlit as st
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import requests

# Function to summarize the content of a webpage given its URL
def summarize_url(url, sentences_count):
    try:
        # Fetch HTML content from the URL
        parser = HtmlParser.from_url(url, Tokenizer("english"))
        # Initialize LsaSummarizer
        summarizer = LsaSummarizer()
        # Get a summary with the specified number of sentences
        summary = summarizer(parser.document, sentences_count)
        # Join the summary sentences into a string
        summary_text = " ".join(str(sentence) for sentence in summary)
        return summary_text
    except requests.RequestException as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Streamlit app
def main():
    st.title("Web Page Summarizer")

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

if __name__ == "__main__":
    main()
