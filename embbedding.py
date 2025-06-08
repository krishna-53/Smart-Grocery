from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from database import fetch_all_products
import pickle
import os

model = SentenceTransformer('all-MiniLM-L6-v2')
index_file = "faiss_index.pkl"
products_file = "products.pkl"

def build_faiss_index():
    products = fetch_all_products()
    texts = [f"{p['product_name']} {p['category']}" for p in products]
    embeddings = model.encode(texts, convert_to_numpy=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    with open(products_file, "wb") as f:
        pickle.dump(products, f)
    with open(index_file, "wb") as f:
        pickle.dump(index, f)

    return index, products

def load_faiss_index():
    if os.path.exists(index_file) and os.path.exists(products_file):
        with open(index_file, "rb") as f:
            index = pickle.load(f)
        with open(products_file, "rb") as f:
            products = pickle.load(f)
        return index, products
    else:
        return build_faiss_index()

def semantic_search(query, index, products, top_k=5):
    query_vec = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_vec, top_k)
    results = [products[i] for i in indices[0]]
    return results