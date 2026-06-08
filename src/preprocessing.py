import pandas as pd


def load_data(path="data/amazon_reviews.csv"):
    df = pd.read_csv(path, low_memory=False)
    return df


def clean_data(df):
    df_clean = df[[
        "name",
        "brand",
        "categories",
        "reviews.date",
        "reviews.rating",
        "reviews.title",
        "reviews.text"
    ]].copy()

    df_clean["brand"] = (
        df_clean["brand"]
        .fillna("Unknown brand")
        .astype(str)
        .str.strip()
        .str.title()
    )

    df_clean["categories"] = (
        df_clean["categories"]
        .fillna("Unknown category")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    df_clean["name"] = (
        df_clean["name"]
        .fillna("Unknown name")
        .astype(str)
        .str.replace("\r\n", " ", regex=False)
        .str.replace(",,,", "", regex=False)
        .str.strip()
    )

    df_clean["reviews.title"] = (
        df_clean["reviews.title"]
        .fillna("Unknown Title")
        .astype(str)
        .str.strip()
    )

    df_clean = df_clean.dropna(subset=[
        "reviews.rating",
        "reviews.text"
    ])

    df_clean["reviews.date"] = pd.to_datetime(
        df_clean["reviews.date"],
        errors="coerce"
    )

    df_clean["search_text"] = (
        df_clean["name"].astype(str)
        + " "
        + df_clean["reviews.title"].astype(str)
        + " "
        + df_clean["reviews.text"].astype(str)
    )
    df_clean = df_clean[
    df_clean["name"] != "Unknown name"
    ]
    return df_clean