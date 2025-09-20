import requests
import json
import os
import nltk
import re
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer  # Or any other summarizer
nltk.download('punkt')
nltk.download('punkt_tab')
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
if not NEWS_API_KEY:
    raise ValueError("❌ No API key found. Set NEWS_API_KEY environment variable.")
# fix the key
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
response = requests.get(URL)
new_data = response.json()
with open("news.json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, indent=4)
file_path = "data/my_data.json"

def clean_text(text: str) -> str:
    if not text:
        return ""
    # 1. Remove HTML tags (like <ul>, <li>, <p>, etc.)
    text = BeautifulSoup(text, "html.parser").get_text()
    # 2. Remove the "[+123 chars]" endings
    text = re.sub(r"\[\+\d+\s*chars\]", "", text, flags=re.IGNORECASE)
    # 3. Strip extra spaces
    return text.strip()


def summarize_articles(article):
    summarizer = LexRankSummarizer()
    summarized_articles = []

    for article in new_data.get("articles", []):
        raw_text = article.get("content") or article.get("description") or ""
        text = clean_text(raw_text)
        if not text:
            continue

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summary = summarizer(parser.document, sentences_count=2)

        # Convert sentences into plain text
        summary_text = " ".join(str(sentence) for sentence in summary)

        # Copy original article and add a summary field
        article_copy = article.copy()
        article_copy["summary"] = summary_text
        summarized_articles.append(article_copy)

    return {"articles": summarized_articles}

summarized_data = summarize_articles(new_data)
with open("news.json", "w", encoding="utf-8") as f:
    json.dump(summarized_data, f, indent=4)

#just a comment