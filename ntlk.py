import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')  # Download POS tagger data
nltk.download('maxent_ne_chunker')  # Download named entity chunker data
nltk.download('words')  # Download words corpus

# def preprocess_text(text):
#     # Tokenize the text
#     tokens = word_tokenize(text)

#     # Part of speech tagging
#     pos_tags = nltk.pos_tag(tokens)

#     # Named entity chunking
#     ne_chunks = nltk.ne_chunk(pos_tags, binary=True)

#     # Extract strings from Tree objects
#     chunks = []
#     for chunk in ne_chunks:
#         if isinstance(chunk, nltk.Tree):
#             chunks.append(' '.join([token[0] for token in chunk.leaves()]))
#         else:
#             chunks.append(chunk[0])

#     # Reconstruct text from tokens
#     preprocessed_text = ' '.join(chunks)
    
#     return preprocessed_text

