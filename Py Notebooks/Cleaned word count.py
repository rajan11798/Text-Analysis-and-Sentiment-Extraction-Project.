#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import nltk
from nltk.corpus import stopwords
import string


# In[2]:


def compute_word_count(file_path):
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Remove punctuation
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    # Count the words
    word_count = len(words)

    return word_count

# Folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'

# Get all file names from the folder
file_names = os.listdir(folder_path)

# Compute word count for each file
for file_name in file_names:
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Compute word count
    count = compute_word_count(file_path)
    print(f"Word count for {file_name}: {count}")


# In[3]:



import pandas as pd

def compute_word_count(file_path):
    # Read the text file
    with open(file_path, 'r', encoding = 'utf-8') as file:
        text = file.read()

    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Remove punctuation
    words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]

    # Count the words
    word_count = len(words)

    return word_count

# Folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'

# Get all file names from the folder
file_names = os.listdir(folder_path)

# Compute word count for each file
counts = []
for file_name in file_names:
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Compute word count
    count = compute_word_count(file_path)
    counts.append(count)

# Read the existing Excel file
excel_file_path = r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx'
df = pd.read_excel(excel_file_path)

# Add the word counts to the existing column
df['WORD COUNT'] = counts

# Save the modified dataframe back to the Excel file
df.to_excel(excel_file_path, index=False)

