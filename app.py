from flask import Flask, request, render_template, redirect, url_for
from vector import build_retriever, get_retriever
from main import chain
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf_file' not in request.files:
        return "No file part"

    file = request.files['pdf_file']
    if file.filename == '':
        return "No selected file"

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        build_retriever(filepath)

        return redirect(url_for('chat'))

    return "Please upload a valid PDF file."

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    retriever = get_retriever()

    if retriever is None:
        return "Please upload a PDF first."

    response = ""
    question = ""

    if request.method == 'POST':
        question = request.form['question']
        docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in docs])

        response = chain.invoke({
            "context": context,
            "question": question
        })

    return render_template('chat.html', response=response, question=question)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

