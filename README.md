# 📄 Chat with Your PDF (Flask + LangChain + Ollama)
This is a simple AI PDF Chatbot Web App built using Flask, LangChain, and Ollama.
It allows you to upload any PDF file and then chat with it by asking questions about its content.

🚀 Features
Upload and process your own PDF file

Vector-based document retrieval (using FAISS)

Embedding with Hugging Face (all-MiniLM-L6-v2)

Local LLM querying via Ollama (gemma3:latest by default)

Simple Flask web interface for chat interaction

# Project Structure
```bash
pdf_chatbot/
├── app.py                # Flask app with routes
├── vector.py             # PDF loading, splitting, embedding, retriever setup
├── llm_chain.py          # LLM model and LangChain chain setup
├── uploads/              # Folder to store uploaded PDFs
├── templates/
│   ├── index.html        # PDF upload form
│   └── chat.html         # Chat interface
└── README.md             # Project documentation
```
🛠️ Requirements
Python 3.8+

Ollama installed and running locally (https://ollama.com/)

Python libraries:

Flask

LangChain

Hugging Face Transformers

Sentence Transformers

⚙️ Installation
Clone the repository:
git clone https://github.com/alibelhrak/Chat_With_Your-_PDF.git
cd app.py

Install required Python packages:
flask
langchain
langchain_community
langchain_core
sentence-transformers
faiss-cpu


☣️ Make sure Ollama is running locally and that the LLM (e.g., gemma3) is downloaded.
