#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[21]:


import requests
from bs4 import BeautifulSoup

# Send a GET request to the web page
url = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the paragraphs to extract
paragraphs = soup.find_all('p')

# Exclude paragraphs with specific classes
excluded_classes = ['entry-title', 'tdm-descr']
filtered_paragraphs = [
    p for p in paragraphs if not any(c in p.get('class', []) for c in excluded_classes)
]

# Extract the text from remaining paragraphs
text = ' '.join(p.get_text(strip=True) for p in filtered_paragraphs)

# Print the extracted text
print(text)


# In[27]:


# Load the Excel file
dataframe = pd.read_excel('E:\INtershala Assingment\Input.xlsx')

# Create a directory to store the extracted content files
output_dir = 'E:\INtershala Assingment\output'
os.makedirs(output_dir, exist_ok=True)

# Extract the website links from the 'Links' column
links = dataframe['URL'].tolist()
i=0
# Iterate over the links
for link in links:
    i=i+1
    # Send a GET request to the website
    response = requests.get(link)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    try:
        # Find the article heading
        heading = soup.find('h1').text
    except AttributeError:
        heading = 'Heading not found'

    # Find the paragraphs to extract
    text = ''
    paragraphs = soup.find_all('p')

    # Exclude paragraphs with specific classes
    excluded_classes = ['entry-title', 'tdm-descr']
    filtered_paragraphs = [
        p for p in paragraphs if not any(c in p.get('class', []) for c in excluded_classes)
    ]

    # Extract the text from remaining paragraphs
    text = ' '.join(p.get_text(strip=True) for p in filtered_paragraphs)

    # Print the extracted text
#     print('Heading:',heading)
#     print('Text:',text)
    
#     if i == 3:
#         break


#     print(i)   

    # Create the output file path using the link name
    link_name = link.split('/')[-2].rstrip('.html')
    output_file = os.path.join(output_dir, f'{link_name}.txt')

    # Write the extracted content to the output file
    with open(output_file, 'w', encoding = 'utf-8') as f:
        f.write(f'Heading: {heading}\n')
        f.write(f'Text: {text}')

    print(f'Extracted and saved: {output_file}')


# In[28]:


print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




