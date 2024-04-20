# NRE_analyser

NRE_analyser is a tool for Named Entity Recognition (NER) and analysis of text documents, PDF, CSV files also Excel sheets. It utilizes spaCy for natural language processing tasks and provides a Flask web interface for users to upload documents and visualize named entities detected in them.

## Features

- Supports analysis of PDF, Excel, CSV, and plain text files.
- Pre-trained spaCy model for named entity recognition.
- User-friendly web interface for document upload and entity visualization.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- spaCy
- PyPDF2
- pandas
- nltk

Install the dependencies using pip:

```bash
pip install Flask spacy PyPDF2 pandas nltk
```

You'll also need to download the spaCy English model:

```bash
python -m spacy download en_core_web_lg
```

 Run ntlk.py script in your virtual environment to download the NLTK resources by executing python nltk.py in your terminal or command prompt or virtual enviornment.

### Running the Application

Clone the repository:

```bash
git clone https://github.com/your_username/NRE_analyser.git
cd NRE_analyser
```

Run the Flask application:

```bash
python app.py
```

The application will be running on <http://localhost:5000> by default.

## Usage

1. Access the web interface by navigating to <http://localhost:5000> in your web browser.
2. Upload a document (PDF, Excel, CSV, or plain text).
3. The application will process the document and display the named entities detected.
4. Visualize the entities using the provided interface.

## NRE_analyser

![NRE_Analyser](https://github.com/Nehadasmk/DataScience_Project/blob/main/images/NRE_Analyzerapp_image.png)
