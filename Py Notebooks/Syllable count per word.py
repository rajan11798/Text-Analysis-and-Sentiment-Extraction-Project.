#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import nltk
from nltk.corpus import stopwords
import string


# In[4]:



def count_syllables(word):
    vowels = 'aeiou'
    exceptions = ['es', 'ed']
    count = 0

    if word[-2:] in exceptions:
        return count

    for index, char in enumerate(word):
        if char in vowels and (index == 0 or word[index - 1] not in vowels):
            count += 1

    return count

def compute_syllable_count(file_path):
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

    # Count the syllables per word
    syllable_counts = [count_syllables(word) for word in words]

    return syllable_counts

# Folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'

# Get all file names from the folder
file_names = os.listdir(folder_path)

# Compute syllable count for each file
for file_name in file_names:
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Compute syllable count
    
    syllable_count = compute_syllable_count(file_path)

    # Print the counts for the current file
    print(f"Syllable counts for {file_name}:")
    for count in syllable_count:
        print(count)
    print()


# In[9]:



import pandas as pd

def count_syllables(word):
    vowels = 'aeiou'
    exceptions = ['es', 'ed']
    count = 0

    if word[-2:] in exceptions:
        return count

    for index, char in enumerate(word):
        if char in vowels and (index == 0 or word[index - 1] not in vowels):
            count += 1

    return count

def compute_syllable_count(file_path):
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

    # Count the syllables per word
    syllable_counts = [count_syllables(word) for word in words]

    # Calculate the total syllable count for the file
    total_syllables = sum(syllable_counts)

    return total_syllables

# Folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'

# Get all file names from the folder
file_names = os.listdir(folder_path)

# Read the existing Excel file
excel_file_path = r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx'
df = pd.read_excel(excel_file_path)

# Compute syllable count for each file and update the existing column
for file_name in file_names:
    # Construct the full file path
    file_path = os.path.join(folder_path, file_name)

    # Compute syllable count
    syllable_count = compute_syllable_count(file_path)

    # Find the row index for the current file in the DataFrame
    row_index = df.index[df['URL'] == file_name].tolist()[0]

    # Update the existing column with the syllable count for the file
    df.at[row_index, 'SYLLABLE PER WORD'] = syllable_count

# Save the modified dataframe back to the Excel file
df.to_excel(excel_file_path, index=False)

