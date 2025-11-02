# 📰 News Summarizer Website

This project is a simple news website that fetches the latest headlines using the NewsAPI and generates concise summaries for each article using Natural Language Processing (NLP).

---

## 📌 Project Overview

- **Goal**: Fetch the latest news and provide short, readable summaries for each article.
- **API Used**: [NewsAPI](https://newsapi.org/)
- **Summarization**: LexRank algorithm from the `sumy` library.
- **Data Source**: Top U.S. headlines (`country=us`)

---

## ⚙️ Features

✅ Fetches top news headlines using an API key  
✅ Cleans article text (removes HTML, extra characters, etc.)  
✅ Summarizes content into 2-sentence summaries  
✅ Saves results to a local `news.json` file  

---

## 📁 File Structure

```
├── news.json             # Output file containing summarized news
├── main.py               # Main Python script (based on the provided code)
├── .env                  # Stores the NEWS_API_KEY securely
```

---

## 🔑 Environment Variables

Create a `.env` file and add your News API key:

```
NEWS_API_KEY=your_api_key_here
```

You can get an API key from: https://newsapi.org/

---

## 🚀 How It Works

### 1️⃣ Install Dependencies
```bash
pip install requests python-dotenv beautifulsoup4 sumy nltk
```

### 2️⃣ Download Required NLTK Files
These are included in the script:
```python
nltk.download('punkt')
```

### 3️⃣ Run the Script
```bash
python main.py
```

### 4️⃣ Output
A `news.json` file is created with article titles, sources, URLs, and summaries.

---

## 🧠 How Summaries are Generated

The script:
1. Fetches raw news data using `requests`
2. Cleans the text using `BeautifulSoup` and regex
3. Uses **LexRank (Text Ranking Algorithm)** to summarize text into 2 key sentences
4. Saves the summarized version of each article to `news.json`

---

## 🛠️ Code Breakdown

### ✅ Fetch News
```python
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
response = requests.get(URL)
new_data = response.json()
```

### ✅ Clean and Summarize
```python
def summarize_articles(article):
    summarizer = LexRankSummarizer()
    ...
    summary = summarizer(parser.document, sentences_count=2)
```

---

## 🔮 Future Improvements

- Add a front-end UI for displaying news
- Support multiple countries and news categories
- Store news data in a database instead of a JSON file
- Deploy as a web app using Flask / Django

---

## 🙌 Acknowledgements

- News source: **NewsAPI**
- NLP Tools: **NLTK** & **Sumy**
- HTML Cleaning: **BeautifulSoup**

---

Made with ❤️ and Python 🐍
