from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from vector import retriever  

model = OllamaLLM(model='gemma3:latest', temperature=0.1)

prompt = ChatPromptTemplate.from_template("""
You are an expert assistant for answering questions about a PDF document.

Context:
{context}

Question:
{question}

Answer in a clear and concise way:
""")

chain = prompt | model | StrOutputParser()

