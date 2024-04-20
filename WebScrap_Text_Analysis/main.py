import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import numpy as np
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
import syllapy

nltk.download('punkt')

# Load URLs from the Excel file
df_urls = pd.read_excel('Input.xlsx')

# Create a directory to save extracted text files
output_directory = 'extracted_texts'
os.makedirs(output_directory, exist_ok=True)

# Load the output data structure file to get the variable order
output_data_structure = pd.read_excel('Output Data Structure.xlsx')

# Function to calculate variables for each article text
def calculate_variables(article_text, stop_words_df, positive_words_df, negative_words_df):
    # Tokenize article text into sentences
    sentences = sent_tokenize(article_text)
    # Tokenize article text into words
    words = word_tokenize(article_text)
    
    # Remove stop words
    stop_words = set(stop_words_df['StopWords'].values)
    words = [word for word in words if word.lower() not in stop_words]
    
    # Calculate average sentence length
    avg_sentence_length = len(words) / len(sentences)
    
    # Calculate percentage of complex words
    complex_word_count = sum(1 for word in words if syllapy.count(word) >= 3)
    percentage_complex_words = (complex_word_count / len(words)) * 100
    
    # Calculate fog index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    # Calculate average number of words per sentence
    avg_words_per_sentence = len(words) / len(sentences)
    
    # Calculate word count
    word_count = len(words)
    
    # Calculate syllable per word
    syllable_per_word = sum(syllapy.count(word) for word in words) / len(words)
    
    # Calculate personal pronouns count
    personal_pronouns = sum(1 for word in words if word.lower() in ['i', 'we', 'my', 'ours', 'us'])
    
    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / len(words)
    
    # Perform sentiment analysis
    text_blob = TextBlob(article_text)
    polarity_score = text_blob.sentiment.polarity
    subjectivity_score = text_blob.sentiment.subjectivity
    positive_score = len([word for word in text_blob.words if word.lower() in positive_words_df['PositiveWords'].values])
    negative_score = len([word for word in text_blob.words if word.lower() in negative_words_df['NegativeWords'].values])

    return [positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length,
            percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count,
            syllable_per_word, personal_pronouns, avg_word_length]

def process_stop_words(stop_words_directory):
    stop_words_list = []

    for filename in os.listdir(stop_words_directory):
        if filename.startswith("StopWords_") and filename.endswith(".txt"):
            with open(os.path.join(stop_words_directory, filename), 'r', encoding='latin1') as file:
                # Read stop words from the file and append to the list
                stop_words = file.read().splitlines()
                stop_words_list.extend(stop_words)

    stop_words_df = pd.DataFrame(stop_words_list, columns=['StopWords'])
    return stop_words_df

stop_words_directory = '/home/nfe1cob/Documents/Data/BlackCoffer-internship/StopWords'
stop_words = process_stop_words(stop_words_directory)

def load_words_from_file(file_path):
    with open(file_path, 'r', encoding='latin1') as file:
        words = file.read().splitlines()
    return words

# Load positive words
positive_words_path = '/home/nfe1cob/Documents/Data/BlackCoffer-internship/MasterDictionary/positive-words.txt'
positive_words_list = load_words_from_file(positive_words_path)
positive_words_df = pd.DataFrame(positive_words_list, columns=['PositiveWords'])

# Load negative words
negative_words_path = '/home/nfe1cob/Documents/Data/BlackCoffer-internship/MasterDictionary/negative-words.txt'
negative_words_list = load_words_from_file(negative_words_path)
negative_words_df = pd.DataFrame(negative_words_list, columns=['NegativeWords'])

# # Create a DataFrame to store the calculated variables
output_df = pd.DataFrame(columns=['URL_ID', 'URL'] + list(output_data_structure.columns)[2:])

# Iterate through each text file and calculate variables
for index, row in df_urls.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            title = soup.find('h1').text.strip()
            content = '\n'.join([p.text.strip() for p in soup.find_all('p')])
            
            output_filename = f"{output_directory}/{url_id}.txt"
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(f"Title: {title}\n\n{content}")

            variables = calculate_variables(content, stop_words, positive_words_df, negative_words_df)
            print(f"Number of variables calculated for {url_id}: {len(variables)}")
            print(f"Number of columns in output DataFrame: {len(output_data_structure.columns)}")

            if len(variables) == len(output_data_structure.columns) - 2:  
                output_df.loc[len(output_df)] = [url_id, url] + variables
                print(f"Added data for {url_id}")
            else:
                print(f"Skipping {url_id}: Mismatched number of columns")

        else:
            print(f"Failed to fetch URL: {url_id}")
    except Exception as e:
        print(f"Error extracting text for {url_id}: {str(e)}")

# Save the DataFrame to Excel
output_df.to_excel('output.xlsx', index=False)
