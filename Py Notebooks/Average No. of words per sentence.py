#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from nltk import sent_tokenize, word_tokenize


# In[3]:


# Folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'

# Iterate through each text file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding = 'utf-8') as file:
            text = file.read()
            
            # Tokenize the text into sentences and words
            sentences = sent_tokenize(text)
            words = word_tokenize(text)
            
            # Calculate the number of words and sentences
            num_words = len(words)
            num_sentences = len(sentences)
            
            # Calculate the average number of words per sentence
            average_words_per_sentence = num_words / num_sentences
            
            # Print the score for the file
            print("File:", filename)
            print("Average Words per Sentence:", average_words_per_sentence)
            print()


# In[4]:


import pandas as pd
# Folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'
# empty list to store score
avg_words_per_sentence = []
# Iterate through each text file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding = 'utf-8') as file:
            text = file.read()
            
            # Tokenize the text into sentences and words
            sentences = sent_tokenize(text)
            words = word_tokenize(text)
            
            # Calculate the number of words and sentences
            num_words = len(words)
            num_sentences = len(sentences)
            
            # Calculate the average number of words per sentence
            average_words_per_sentence = num_words / num_sentences
            
            # Append the score to the list
            avg_words_per_sentence.append(average_words_per_sentence)
            
#Read existing excel file
existing_data = pd.read_excel(r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx')

# Add the new scores to the respective columns in the existing data
existing_data['AVG NUMBER OF WORDS PER SENTENCE'] = avg_words_per_sentence
# Write the updated data to the Excel file
existing_data.to_excel(r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx', index=False)
           

