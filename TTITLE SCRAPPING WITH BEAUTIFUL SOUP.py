#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import json


# In[43]:


# Scrapping news wesbite from google 
URL = 'https://docs.python-requests.org/en/master/'


# In[44]:


def get_soup(URL, jar=None):
    if jar:
        r = requests.get(URL, cookies=jar)
    else:
        response = requests.get(URL)
        jar =  requests.cookies.RequestsCookieJar()
    soup = BeautifulSoup(response.content, "html.parser")
    return soup, jar


# In[45]:


soup, jar = get_soup(URL)


# In[54]:


# function to get news news titles
def get_news_titles(s):
    data = []
    titles = s.find_all("h2")
    for title in titles:
        data.append(title.text.strip())
    return data

# change h2 to h3 etc based on need


# In[55]:


get_news_titles(soup)


# In[ ]:




