#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re


# In[3]:


def count_complex_words(text):
    # Regular expression pattern to match words with more than two syllables
    pattern = r'\b\w{3,}\b'

    # Count the number of matches
    matches = re.findall(pattern, text)
    return len(matches)

def compute_complex_word_scores(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Compute the complex word count for each file
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding= 'utf-8') as file:
                text = file.read()
                complex_word_count = count_complex_words(text)
                print(f"File: {file_name}\nComplex Word Count: {complex_word_count}\n")

# Provide the folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'
compute_complex_word_scores(folder_path)


# In[5]:


import pandas as pd
def count_complex_words(text):
    # Regular expression pattern to match words with more than two syllables
    pattern = r'\b\w{3,}\b'

    # Count the number of matches
    matches = re.findall(pattern, text)
    return len(matches)

def compute_complex_word_scores(folder_path):
    complx_word_count = []
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Compute the complex word count for each file
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding= 'utf-8') as file:
                text = file.read()
                complex_word_count = count_complex_words(text)
                complx_word_count.append(complex_word_count)
    #Read existing excel file
    existing_data = pd.read_excel(r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx')
    # Add the new scores to the respective columns in the existing data
    existing_data['COMPLEX WORD COUNT'] = complx_word_count
    # Write the updated data to the Excel file
    existing_data.to_excel(r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx', index=False)

# Provide the folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'
compute_complex_word_scores(folder_path)

