#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from urllib.request import urlopen


# In[2]:


url = "https://movie.naver.com/movie/running/premovie.nhn"
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')


# In[44]:


soup_by_date = soup.find_all("div", class_="lst_wrap")[1]
date_all_list = soup_by_date.ul.find_all("li")
date_all_list


# In[29]:


date_all_list[1].find("dt", class_="tit").a.text

for li in date_all_list:
    print(li.find("dt", class_="tit").a.text)


# In[42]:


daily_movies = []
for by_date in soup_by_date:
    


# In[ ]:


daily_movies = []
for by_date in soup_by_date:
    if by_date is not None:
        all_list = by_date.ul.find_all("li")
        continue
    titles = []
    for list in all_list:
        titles.append(list.find("dt", class_="tit").a.text)
    daily_movies.append(titles)

daily_movies

