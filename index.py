#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[3]:


url = "https://movie.naver.com/movie/running/premovie.nhn"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')


# In[4]:


soup_by_date = soup.find_all("div", class_="lst_wrap")
date_all_list = soup_by_date[1].ul.find_all("li")
date_all_list


# In[5]:


date_all_list[1].find("dt", class_="tit").a.text

for li in date_all_list:
    print(li.find("dt", class_="tit").a.text)


# In[8]:


daily_movies = []
for by_date in soup_by_date:
    all_list = by_date.ul.find_all("li")
    titles = []
    for list in all_list:
        titles.append(list.find("dt", class_="tit").a.text)
    daily_movies.append(titles)

daily_movies


# In[ ]:




