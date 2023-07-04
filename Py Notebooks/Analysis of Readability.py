#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import cmudict


# In[5]:



# Function to count the number of syllables in a word
def count_syllables(word):
    try:
        # Use the CMU Pronouncing Dictionary to count syllables
        syllables = [len(list(y for y in x if y[-1].isdigit())) for x in cmudict.dict()[word.lower()]]
        return max(syllables)
    except KeyError:
        # If the word is not found in the CMU Pronouncing Dictionary, estimate the syllables based on length
        # This is a simple approach and may not be accurate for all words
        return max(1, len(word) // 2)

# Folder path containing the text files
folder_path = r'E:\INtershala Assingment\output'

# Iterate through each text file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding = 'utf-8') as file:
            text = file.read()
            
            # Tokenize the text into sentences
            sentences = sent_tokenize(text)
            
            # Count the number of words and sentences
            num_words = len(word_tokenize(text))
            num_sentences = len(sentences)
            
            # Calculate the average sentence length
            average_sentence_length = num_words / num_sentences
            
            # Calculate the number of complex words and count their occurrences
            complex_words = 0
            for word in word_tokenize(text):
                if count_syllables(word) > 2:
                    complex_words += 1
            
            # Calculate the percentage of complex words
            percentage_complex_words_val = (complex_words / num_words) * 100
            
            # Calculate the Fog Index
            fog_index = 0.4 * (average_sentence_length + percentage_complex_words_val)
            
            # Print the readability metrics for the file
            print("File:", filename)
            print("Average Sentence Length:", average_sentence_length)
            print("Percentage of Complex Words:", percentage_complex_words_val)
            print("Fog Index:", fog_index)
            print()

