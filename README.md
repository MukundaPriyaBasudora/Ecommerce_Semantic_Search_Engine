🛒 E-commerce Semantic Search & Review Analytics Engine:
An intelligent NLP-powered application designed to search, analyze, and visualize product reviews. This tool helps users discover meaningful insights from customer feedback using semantic search and sentiment analysis.

🏗️ Tech Stack
Programming Language: Python
Data Processing: Pandas
NLP: Sentence Transformers, Hugging Face
Vector Database: ChromaDB
Sentiment Analysis: VADER
Visualization & UI: Streamlit


🚀 What This Project Does:
This project combines Natural Language Processing (NLP) and data analytics to:

🔍 Understand search queries like a human (not just keywords)
😊 Analyze customer sentiments across thousands of reviews
📊 Turn raw review data into actionable insights
🌐 Provide an interactive and easy-to-use web interface


✨ Features:
🔍 Semantic Search
Search reviews using natural language queries
Finds contextually relevant results, not just keyword matches
Built using Sentence Transformers and ChromaDB vector search

😊 Sentiment Analysis
Automatically classifies reviews into:
✅ Positive
😐 Neutral
❌ Negative
Powered by VADER Sentiment Analysis

📊 Interactive Analytics Dashboard
Gain insights through visualizations like:
Sentiment distribution
Rating breakdown
Top-performing brands (by average rating)
Trends in reviews over time
Overall dataset statistics

🌐 User Interface
Built with Streamlit
Clean, responsive, and interactive UI
Real-time search and analytics updates

📂 Project Structure:
Ecommerce_Semantic_Search_Engine/
│
├── data/
│   ├── amazon_reviews.csv
│   └── processed_reviews.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── review_analytics.py
│   └── semantic_search.py
│
├── app.py
├── requirements.txt
└── README.md

📊 Dataset Overview
This project uses a dataset of:
📦 34,000+ Amazon product reviews
⭐ Ratings and review scores
📝 Review titles and full text
🕒 Review timestamps
🛍️ Product categories such as:
Amazon Echo
Fire TV
Kindle
Fire Tablets


⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repo-link>
cd Ecommerce_Semantic_Search_Engine
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will be available at:
```text
http://localhost:8501


## 📸 Screenshots

### 📊 Analytics Dashboard
![Analytics Dashboard](images/Screenshot 2026-06-08 165200.png)
![Analytics Dashboard](images/Screenshot 2026-06-08 165210.png)
![Analytics Dashboard](images/Screenshot 2026-06-08 165139.png)

### 🔍 Semantic Search
![Semantic Search](images/Screenshot 2026-06-08 165043.png)
![Semantic Search](images/Screenshot 2026-06-08 165008.png)