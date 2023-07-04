#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

def remove_stopwords(text, stopword_list):
    tokens = text.split()
    filtered_tokens = [word for word in tokens if word.lower() not in stopword_list]
    return ' '.join(filtered_tokens)

# Path to the directory containing the text files
directory = 'E:\INtershala Assingment\output'

# Path to the directory containing the stop word text files
stopwords_directory = 'E:\INtershala Assingment\StopWords'

# Read stop words from the text files in the stop words directory
stopword_list = []
for filename in os.listdir(stopwords_directory):
    if filename.endswith('.txt'):
        stopword_file_path = os.path.join(stopwords_directory, filename)
        with open(stopword_file_path, 'r') as stopword_file:
            stopwords = stopword_file.read().splitlines()
            stopword_list.extend(stopwords)

# Iterate through each text file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r' , encoding = 'utf-8') as file:
            text = file.read()
            # Remove stop words
            processed_text = remove_stopwords(text, stopword_list)
            # Perform sentiment analysis on processed_text
            # (implement your sentiment analysis code here)


# # creating Dictionary

# In[6]:


import os

def remove_stopwords(text, stopword_list):
    tokens = text.split()
    filtered_tokens = [word for word in tokens if word.lower() not in stopword_list]
    return ' '.join(filtered_tokens)

# Path to the directory containing the text files
directory = r'E:\INtershala Assingment\output'

# Path to the positive words text file
positive_words_file = r'E:\INtershala Assingment\MasterDictionary\positive-words.txt'

# Path to the negative words text file
negative_words_file = r'E:\INtershala Assingment\MasterDictionary\negative-words.txt'

# Path to the directory containing the stop word text files
stopwords_directory = r'E:\INtershala Assingment\StopWords'

# Read stop words from the text files in the stop words directory
stopword_list = []
for filename in os.listdir(stopwords_directory):
    if filename.endswith('.txt'):
        stopword_file_path = os.path.join(stopwords_directory, filename)
        with open(stopword_file_path, 'r') as stopword_file:
            stopwords = stopword_file.read().splitlines()
            stopword_list.extend(stopwords)

# Create a set to store positive and negative words
positive_words = set()
negative_words = set()

# Read positive words from the positive words text file
with open(positive_words_file, 'r') as positive_file:
    positive_words_list = positive_file.read().splitlines()
    for word in positive_words_list:
        if word not in stopword_list:
            positive_words.add(word)

# Read negative words from the negative words text file
with open(negative_words_file, 'r') as negative_file:
    negative_words_list = negative_file.read().splitlines()
    for word in negative_words_list:
        if word not in stopword_list:
            negative_words.add(word)

# Iterate through each text file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding = 'utf-8') as file:
            text = file.read()
            # Remove stop words
            processed_text = remove_stopwords(text, stopword_list)
            
            # Create a dictionary of positive and negative words
            sentiment_dictionary = {}
            for word in processed_text.split():
                if word in positive_words:
                    sentiment_dictionary[word] = 'Positive'
                elif word in negative_words:
                    sentiment_dictionary[word] = 'Negative'
            
            # Use sentiment_dictionary as needed for further analysis


# # Calculating scores for each article

# In[15]:


import os
import nltk
from nltk.tokenize import word_tokenize

def remove_stopwords(text, stopword_list):
    tokens = text.split()
    filtered_tokens = [word for word in tokens if word.lower() not in stopword_list]
    return ' '.join(filtered_tokens)

# Path to the directory containing the text files
directory = r'E:\INtershala Assingment\output'

# Path to the positive words text file
positive_words_file = r'E:\INtershala Assingment\MasterDictionary\positive-words.txt'

# Path to the negative words text file
negative_words_file = r'E:\INtershala Assingment\MasterDictionary\negative-words.txt'

# Path to the directory containing the stop word text files
stopwords_directory = r'E:\INtershala Assingment\StopWords'

# Read stop words from the text files in the stop words directory
stopword_list = []
for filename in os.listdir(stopwords_directory):
    if filename.endswith('.txt'):
        stopword_file_path = os.path.join(stopwords_directory, filename)
        with open(stopword_file_path, 'r') as stopword_file:
            stopwords = stopword_file.read().splitlines()
            stopword_list.extend(stopwords)

# Create a set to store positive and negative words
positive_words = set()
negative_words = set()

# Read positive words from the positive words text file
with open(positive_words_file, 'r') as positive_file:
    positive_words_list = positive_file.read().splitlines()
    for word in positive_words_list:
        if word not in stopword_list:
            positive_words.add(word)

# Read negative words from the negative words text file
with open(negative_words_file, 'r') as negative_file:
    negative_words_list = negative_file.read().splitlines()
    for word in negative_words_list:
        if word not in stopword_list:
            negative_words.add(word)
i = 0
# Iterate through each text file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r' , encoding = 'utf-8') as file:
            text = file.read()
            # Remove stop words
            processed_text = remove_stopwords(text, stopword_list)
            
            # Tokenize the processed text
            tokens = word_tokenize(processed_text)
            
            # Variables for derived scores
            positive_score = 0
            negative_score = 0
            total_words = len(tokens)
            
            # Calculate positive and negative scores
            for word in tokens:
                if word in positive_words:
                    positive_score += 1
                elif word in negative_words:
                    negative_score += 1
            
            # Calculate derived variables
            polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
            subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)
            
            # Print the scores for the current text file
            print("File:", filename)
            print("Positive Score:", positive_score)
            print("Negative Score:", -negative_score)  # Multiplying with -1 to make it a positive number
            print("Polarity Score:", polarity_score)
            print("Subjectivity Score:", subjectivity_score)
            print("---------------------")
            
            i= i+1
#             if i==3:
#                 break
# print(i)


# In[16]:


print(i)


# # Writing values to the output Sheet

# In[22]:


import pandas as pd

# Initialize empty lists to store the scores
positive_scores = []
negative_scores = []
polarity_scores = []
subjectivity_scores = []

# Iterate through each text file and retrieve the scores
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding = 'utf-8') as file:
            text = file.read()
            # Remove stop words and tokenize the text
            processed_text = remove_stopwords(text, stopword_list)
            tokens = word_tokenize(processed_text)
            
            # Calculate the scores
            positive_score = 0
            negative_score = 0
            total_words = len(tokens)
            
            for word in tokens:
                if word in positive_words:
                    positive_score += 1
                elif word in negative_words:
                    negative_score += 1
            
            polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
            subjectivity_score = (positive_score + negative_score) / (total_words + 0.000001)
            
            # Append the scores to the respective lists
            positive_scores.append(positive_score)
            negative_scores.append(-negative_score)  # Multiplying with -1 to make it a positive number
            polarity_scores.append(polarity_score)
            subjectivity_scores.append(subjectivity_score)

# Read the existing Excel file
existing_data = pd.read_excel(r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx')

# Add the new scores to the respective columns in the existing data
existing_data['POSITIVE SCORE'] = positive_scores
existing_data['NEGATIVE SCORE'] = negative_scores
existing_data['POLARITY SCORE'] = polarity_scores
existing_data['SUBJECTIVITY SCORE'] = subjectivity_scores

# Write the updated data to the Excel file
existing_data.to_excel(r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx', index=False)


# In[ ]:




