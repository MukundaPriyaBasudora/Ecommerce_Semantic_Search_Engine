import chromadb
from sentence_transformers import SentenceTransformer


class SemanticSearchEngine:
    def __init__(self, collection_name="amazon_reviews"):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def build_index(self, df, sample_size=1000):
        subset = df.sample(sample_size, random_state=42)

        embeddings = self.model.encode(
            subset["search_text"].tolist(),
            show_progress_bar=True
        )

        self.collection.add(
            ids=[str(i) for i in range(len(subset))],
            documents=subset["search_text"].tolist(),
            embeddings=embeddings.tolist(),
            metadatas=[
                {
                    "name": str(row["name"]),
                    "brand": str(row["brand"]),
                    "rating": float(row["reviews.rating"]),
                    "category": str(row["categories"])
                }
                for _, row in subset.iterrows()
            ]
        )

    def search(self, query, top_k=5):
        query_embedding = self.model.encode(query)

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )

        return results