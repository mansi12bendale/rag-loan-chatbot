# 🧠 RAG Loan Chatbot

A lightweight **Retrieval-Augmented Generation (RAG)** based Q&A chatbot that intelligently answers questions related to **loan approval** by retrieving relevant information from a structured dataset.

🔗 **Live App**: [rag-loan-chatbot Streamlit App](https://rag-loan-chatbot-nlezm4znpmltksj2fmlcqw.streamlit.app/)

---

## 📌 Features

- 💬 Ask questions related to loan applications.
- 🔍 Document retrieval using sentence embeddings.
- 🤖 Intelligent answers generated using a lightweight Hugging Face transformer model.
- 🌐 Deployed using Streamlit Cloud.
- 📁 Small app size (<5MB) optimized for fast deployment.

---
## 📂 Folder Structure

<details>
<summary>Click to expand</summary>

```
Assignment 8/
├── app.py                 # Streamlit main app
├── rag_utils.py           # RAG logic: retrieval & generation
├── Training Dataset.csv   # Source data for loan-related questions
├── requirements.txt       # App dependencies
└── README.md              # Project documentation
```

</details>



---

## 📊 Dataset

- **Source**: [Loan Approval Prediction Dataset - Kaggle](https://www.kaggle.com/datasets/sonalisingh1411/loan-approval-prediction)
- **File Used**: `Training Dataset.csv`

---

## 🚀 Run Locally

```bash
git clone https://github.com/mansi12bendale/rag-loan-chatbot.git
cd rag-loan-chatbot
python -m venv venv
# Activate virtual environment:
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py


