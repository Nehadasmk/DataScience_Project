# Web Scraping and Text Analysis Project

## Overview
This project involves scraping articles from provided URLs, extracting relevant text content, and analyzing various linguistic features of the text. The analysis includes calculating variables such as sentiment polarity, subjectivity, word count, average word length, and more.

## Project Structure
- **main.py**: Python script containing the main code for web scraping, text extraction, and analysis.
- **Input.xlsx**: Excel file containing URLs to be scraped.
- **Output Data Structure.xlsx**: Excel file defining the structure of the output data.
- **extracted_texts/**: Directory to store extracted text files.
- **output.xlsx**: Excel file containing the analyzed data.
- **StopWords/**: Directory containing stop words lists.
- **MasterDictionary**: Directory containing postive_words and negative_words.txt.

## Requirements
- Python 3.x
- Libraries:
  - pandas
  - requests
  - beautifulsoup4
  - nltk
  - textblob
  - syllapy

## Output

- The analyzed data will be saved in output.xlsx.
- Extracted text files will be stored in the extracted_texts/ directory.