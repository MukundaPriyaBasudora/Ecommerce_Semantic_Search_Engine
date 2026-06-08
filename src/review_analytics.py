import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text):
    score = analyzer.polarity_scores(str(text))["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"


def add_sentiment(df):
    df["sentiment"] = df["reviews.text"].apply(get_sentiment)
    return df


def get_sentiment_distribution(df):
    return df["sentiment"].value_counts()


def get_rating_sentiment_crosstab(df):
    return pd.crosstab(df["reviews.rating"], df["sentiment"])


def get_brand_stats(df):
    brand_stats = (
        df.groupby("brand")
        .agg(
            avg_rating=("reviews.rating", "mean"),
            review_count=("reviews.rating", "count")
        )
    )

    return brand_stats[brand_stats["review_count"] >= 50].sort_values(
        "avg_rating",
        ascending=False
    )


def get_product_stats(df):
    product_df = df[df["name"] != "Unknown name"]

    product_stats = (
        product_df.groupby("name")
        .agg(
            avg_rating=("reviews.rating", "mean"),
            review_count=("reviews.rating", "count")
        )
    )

    return product_stats[product_stats["review_count"] >= 100].sort_values(
        "avg_rating",
        ascending=False
    )


def get_reviews_per_year(df):
    df = df.copy()

    df["reviews.date"] = pd.to_datetime(
        df["reviews.date"],
        errors="coerce"
    )

    df["year"] = df["reviews.date"].dt.year

    return df["year"].value_counts().sort_index()

def get_yearly_ratings(df):
    df["year"] = df["reviews.date"].dt.year
    return df.groupby("year")["reviews.rating"].mean()