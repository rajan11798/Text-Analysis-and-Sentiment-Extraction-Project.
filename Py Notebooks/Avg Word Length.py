#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

def calculate_average_word_length(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        total_characters = sum(len(word) for word in words)
        total_words = len(words)
        average_word_length = total_characters / total_words
        return average_word_length

folder_path = r'E:\INtershala Assingment\output'
files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        average_length = calculate_average_word_length(file_path)
        print(f"Average word length for {file}: {average_length:.2f}")


# In[4]:


import pandas as pd

def calculate_average_word_length(file_path):
    with open(file_path, 'r',encoding ='utf-8') as file:
        content = file.read()
        words = content.split()
        total_characters = sum(len(word) for word in words)
        total_words = len(words)
        average_word_length = total_characters / total_words
        return average_word_length

folder_path = r'E:\INtershala Assingment\output'
files = os.listdir(folder_path)

excel_file_path = r'C:\Users\user\OneDrive\Desktop\Output Data Structure.xlsx'

average_lengths = []

for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        average_length = calculate_average_word_length(file_path)
        average_lengths.append(average_length)

# Load the existing Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path)

# Assign the average_lengths list to the existing column
df['AVG WORD LENGTH'] = average_lengths

# Save the updated DataFrame to the Excel file
df.to_excel(excel_file_path, index=False)


# In[ ]:




