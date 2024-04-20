
from flask import Flask, request, render_template
import spacy
from spacy import displacy
from PyPDF2 import PdfReader  # Import PdfReader from PyPDF2
import pandas as pd

nlp = spacy.load('en_core_web_lg')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entity', methods=['POST', 'GET'])
def entity():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Check if the file is a PDF
            if file.filename.endswith('.pdf'):
                # Read the PDF file and extract text
                pdf_doc = PdfReader(file)
                text = ''
                for page in pdf_doc.pages:
                    text += page.extract_text()
            elif file.filename.endswith('.xlsx'):
                df = pd.read_excel(file)
                text = df.to_string()
            elif file.filename.endswith('.csv'):
                df = pd.read_csv(file)
                text = df.to_string()
            else:
                # For non-PDF files, read as plain text
                text = file.read().decode('utf-8', errors='ignore')

            docs = nlp(text)
            html = displacy.render(docs, style='ent', jupyter=False)
            return render_template('index.html', html=html, text=text)
    # Return an empty response for GET requests
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)







