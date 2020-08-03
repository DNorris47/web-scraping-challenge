#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import requests


# In[2]:


#----------NASA Mars News -------------


# In[3]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
soup = bs(html, "html.parser")


# In[7]:


article = soup.find("div", class_='list_text')
news_title = article.find('div', class_='content_title').text
news_p = article.find('div', class_="article_teaser_body").text
print(news_title)
print(news_p)


# In[ ]:


#----------JPL Mars Space ----------------


# In[8]:


jpl_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(jpl_image_url)
html = browser.html
soup = bs(html, "html.parser")


# In[9]:


image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image
print(featured_image_url)


# In[ ]:


#----------Mars Weather ----------------


# In[22]:


#get Mars weather twitter account and scrap lastest tweet
url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)


# In[30]:


import re
html_weather = browser.html
soup = bs(html_weather, "html.parser")

from selenium import webdriver
driver = webdriver.Chrome()
driver.get(url_weather)
html = driver.page_source
driver.close()

pattern = re.compile(r'sol') 
mars_weather = soup.find('span', text=pattern).text

#mars_weather = soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
#mars_weather = soup.find('div', {'class':"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"})
print(mars_weather)
    


# In[ ]:


#----------Mars Facts ----------------


# In[13]:


#scrape Mars fact table
url_mars_facts = "https://space-facts.com/mars/"
mars_facts_table=pd.read_html(url_mars_facts)
mars_facts_table [0]


# In[14]:


df_mars_facts = mars_facts_table[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index("Parameter")
df_mars_facts


# In[15]:


mars_html_table = df_mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n","")
mars_html_table


# In[ ]:


#----------Mars Hemispheres ----------------


# In[16]:


url_mars_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_mars_hemisphere)
html = browser.html
soup=bs(html, "html.parser")
mars_hemisphere = []


# In[17]:


products = soup.find("div", class_="result-list")
hemisphere = products.find_all("div", class_="item")

for hemisphere in hemisphere:
    title = hemisphere.find('h3').text
    title = title.replace('Enhanced',"" )
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/"+ end_link
    browser.visit(image_link)
    html = browser.html
    soup=bs(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title":title,"img_url":image_url})


# In[18]:


mars_hemisphere


# In[ ]:





# In[ ]:




