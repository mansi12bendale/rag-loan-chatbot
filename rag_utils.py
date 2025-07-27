import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

# Load the dataset and prepare documents
def load_documents(csv_path):
    df = pd.read_csv(csv_path)
    # Combine important text columns for semantic matching
    df['document'] = df.apply(lambda row: ' '.join([str(row[col]) for col in df.columns]), axis=1)
    return df['document'].tolist()

# Retrieve top-k relevant documents using TF-IDF + Cosine Similarity
def retrieve_documents(query, documents, top_k=3):
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(documents)
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    top_indices = similarities.argsort()[::-1][:top_k]
    return [documents[i] for i in top_indices]

# Generate answer using a lightweight model (e.g., distilgpt2 or similar)
def generate_answer(query, retrieved_docs):
    context = "\n".join(retrieved_docs)
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    
    generator = pipeline("text-generation", model="distilgpt2")
    
    # Use `max_new_tokens` instead of `max_length` to avoid input length issues
    result = generator(
        prompt,
        do_sample=True,
        top_k=50,
        num_return_sequences=1,
        max_new_tokens=100  # You can adjust this value as needed
    )
    
    return result[0]['generated_text'].split("Answer:")[-1].strip()
