import streamlit as st
from rag_utils import load_documents, retrieve_documents, generate_answer

# Title
st.title("Loan Approval Q&A Chatbot 🤖💬")
st.markdown("Ask any question based on the loan approval dataset.")

# Load CSV as documents (cached for speed)
@st.cache_data
def get_documents():
    return load_documents("Training Dataset.csv")

documents = get_documents()

# User input
query = st.text_input("Enter your question:")
if query:
    with st.spinner("Generating answer..."):
        relevant_docs = retrieve_documents(query, documents)
        answer = generate_answer(query, relevant_docs)
        st.success("Answer:")
        st.write(answer)
