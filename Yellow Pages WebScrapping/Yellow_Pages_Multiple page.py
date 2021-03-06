# -*- coding: utf-8 -*-
"""Yellow_Pages.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bi_7XLSDHB0gnV3_bJJ6mTArIcoDuZbj
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

website='https://www.yellowpages.com/search?search_terms=Restaurant&geo_location_terms=New+York%2C+NY'

response=requests.get(website)

response.status_code

soup=BeautifulSoup(response.content,'html.parser')

soup

result_container=soup.find_all('div',{'class':'result'})

result_container

len(result_container)

"""### **CONCATENATING 2 URLS into 1 URL**

### URL_part 1
"""

url_part_1='https://www.yellowpages.com/'

"""### URL_part 2"""

url_part_2=[]
# loop through the results

for item in result_container:
  #loop through links
  for link in item.find_all('a',{'class':'business-name'}):
    url_part_2.append(link.get('href'))

len(url_part_2)

"""###  **JOIN URL-1 & URL-2**"""

import urllib.parse

url_joined=[]
for link_2 in url_part_2:
  url_joined.append(urllib.parse.urljoin(url_part_1,link_2))

url_joined

"""## GET DATA FROM LINK"""

first_link=url_joined[0]
response=requests.get(first_link)
response.status_code

soup=BeautifulSoup(response.content,'html.parser')
soup

# NAME
 soup.find('h1').get_text()

# Address
soup.find('h2').get_text()

# Phone
soup.find('p',{'class':'phone'}).get_text()

# EMail - Important part
soup.find('a',{'class':'email-business'}).get('href').split('mailto:')[1]

# Website
soup.find('a',{'class':'website-link'}).get('href')

# Ratings
soup.find('span',{'class':'count'}).get_text().replace('(','').replace(')','')

results=[]

 for link in url_joined:
   response= requests.get(link)

   soup=BeautifulSoup(response.content,'html.parser')

   # NAME
   try:
       name=soup.find('h1').get_text()
   except:
       name='NA'
   
   # Address
   try:
       address=soup.find('h2').get_text()
   except:
       address='NA'

   # Phone
   try:
       phone=soup.find('p',{'class':'phone'}).get_text()
   except:
       phone='NA'
   
   # EMail - Important part
   try:
       email=soup.find('a',{'class':'email-business'}).get('href').split('mailto:')[1]
   except:
       email='NA'
  
   # Website
   try:
       website=soup.find('a',{'class':'website-link'}).get('href')
   except:
       website='NA'
     
   # Ratings
   try:
       ratings=soup.find('span',{'class':'count'}).get_text().replace('(','').replace(')','')
   except:
       ratings='NA'    

   # Create a DICTIONARY with resutls

   output={'Restaurant Name': name,'Address': address,'Phone Number': phone,'Email': email,'Website': website,'Ratings':ratings}
   results.append(output)

df=pd.DataFrame(results)
df

df.to_excel('Yellow_Pages.xlsx',index=False)

"""# **WEBSCRAPPING FOR MULTIPLE PAGES**"""

df_restaurant=pd.DataFrame(columns=['Restaurant Name','Address','Phone','Email','Website','Ratings'])

for i in range(1,4):
  website='https://www.yellowpages.com/search?search_terms=Restaurant&geo_location_terms=New%20York%2C%20NY&page='+str(i)
  response=requests.get(website)

  soup=BeautifulSoup(response.content,'html.parser')
  result_container=soup.find_all('div',{'class':'result'})
  url_part_1='https://www.yellowpages.com/'
  url_part_2=[]

  for item in result_container:
    for link in item.find_all('a',{'class':'business-name'}):
      url_part_2.append(link.get('href'))  

  url_joined=[]
  for link_2 in url_part_2:
    url_joined.append(urllib.parse.urljoin(url_part_1,link_2))   
   

  results=[]

  for link in url_joined:
    response= requests.get(link)

    soup=BeautifulSoup(response.content,'html.parser')

    # NAME
    try:
       name=soup.find('h1').get_text()
    except:
       name='NA'
    
    # Address
    try:
       address=soup.find('h2').get_text()
    except:
        address='NA'

    # Phone
    try:
        phone=soup.find('p',{'class':'phone'}).get_text()
    except:
        phone='NA'
    
    # EMail - Important part 
    try:
        email=soup.find('a',{'class':'email-business'}).get('href').split('mailto:')[1]
    except:
        email='NA'
    
    # Website
    try:
        website=soup.find('a',{'class':'website-link'}).get('href')
    except: 
        website='NA'
      
    # Ratings
    try:
        ratings=soup.find('span',{'class':'count'}).get_text().replace('(','').replace(')','')
    except:
        ratings='NA'    

    # Create a DICTIONARY with resutls

    df_restaurant=df_restaurant.append({'Restaurant Name': name,'Address': address,'Phone Number': phone,'Email': email,'Website': website,'Ratings':ratings},ignore_index=True)

df_restaurant

df_restaurant.to_excel('Yellow_pages_Multiple.xlsx',index=False)