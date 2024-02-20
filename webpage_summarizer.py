# webpage_summarizer.py
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import requests

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
