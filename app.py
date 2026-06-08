import pandas as pd
import streamlit as st

from src.review_analytics import (
    get_sentiment_distribution,
    get_brand_stats,
    get_reviews_per_year,
)

from src.semantic_search import SemanticSearchEngine


st.set_page_config(
    page_title="E-commerce Semantic Search Engine",
    layout="wide"
)

st.title("🛒 E-commerce Semantic Search & Review Analytics Engine")


def clean_product_name(product_name):
    product_name = str(product_name).strip()

    words = product_name.split()

    if len(words) % 2 == 0:
        half = len(words) // 2

        if words[:half] == words[half:]:
            product_name = " ".join(words[:half])

    return product_name


@st.cache_data
def load_clean_data():
    df_clean = pd.read_csv("data/processed_reviews.csv")

    df_clean["reviews.date"] = pd.to_datetime(
        df_clean["reviews.date"],
        errors="coerce"
    )

    return df_clean


df_clean = load_clean_data()


@st.cache_resource
def load_search_engine():
    engine = SemanticSearchEngine()
    engine.build_index(df_clean, sample_size=1000)
    return engine


page = st.sidebar.selectbox(
    "Choose Section",
    ["Semantic Search", "Analytics Dashboard"]
)


if page == "Semantic Search":
    st.header("🔍 Semantic Search")

    query = st.text_input(
        "Enter your search query",
        placeholder="Example: tablet for kids"
    )

    if query:
        with st.spinner("Searching relevant reviews..."):
            engine = load_search_engine()
            results = engine.search(query=query, top_k=5)

        st.subheader("Search Results")

        for i in range(len(results["documents"][0])):
            st.markdown("---")

            metadata = results["metadatas"][0][i]

            product_name = clean_product_name(metadata["name"])

            st.subheader(product_name)
            st.write(f"**Brand:** {metadata['brand']}")
            st.write(f"**Rating:** {metadata['rating']} ⭐")
            st.write(results["documents"][0][i][:500])


if page == "Analytics Dashboard":
    st.header("📊 Analytics Dashboard")

    st.subheader("Dataset Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Reviews", len(df_clean))
    col2.metric("Products", df_clean["name"].nunique())
    col3.metric("Brands", df_clean["brand"].nunique())

    st.subheader("Sentiment Distribution")

    sentiment_counts = get_sentiment_distribution(df_clean)
    sentiment_percent = (sentiment_counts / sentiment_counts.sum()) * 100

    st.bar_chart(sentiment_percent)

    st.subheader("Rating Distribution")

    rating_counts = (
        df_clean["reviews.rating"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    rating_counts.columns = ["Rating", "Count"]

    st.bar_chart(
        rating_counts.set_index("Rating")
    )

    st.subheader("Top Brands by Average Rating")

    brand_stats = get_brand_stats(df_clean)
    st.dataframe(brand_stats.head(10))

    st.subheader("Reviews Over Time")

    reviews_per_year = get_reviews_per_year(df_clean)
    st.line_chart(reviews_per_year)