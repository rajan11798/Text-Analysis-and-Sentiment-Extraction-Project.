#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import os

def count_personal_pronouns(file_path):
    pronoun_counts = {'I': 0, 'we': 0, 'my': 0, 'ours': 0, 'us': 0}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        matches = re.findall(r'\b(I|we|my|ours|us)\b', text)
        
        for match in matches:
            pronoun_counts[match] += 1
    
    return pronoun_counts

def count_personal_pronouns_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            file_counts = count_personal_pronouns(file_path)

            print(f"Counts for file: {file_name}")
            for pronoun, count in file_counts.items():
                print(f"{pronoun}: {count}")
            print()  # Empty line for separation


folder_path = r'E:\INtershala Assingment\output'
count_personal_pronouns_in_folder(folder_path)


# In[ ]:





# In[ ]:




