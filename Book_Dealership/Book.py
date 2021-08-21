from bs4 import BeautifulSoup
import requests
import pandas as pd

website="https://books.toscrape.com/"

response=requests.get(website)

response.status_code
print("Status Code : ",response)

soup=BeautifulSoup(response.content,'html.parser')
results = soup.find_all('li',{'class':'col-xs-6'})


product.find('h3').find('a').get_text()
product.find('h3').find('a').get('title')
product.find('p',{'class':'price_color'}).get_text()
product.find('p',{'class':'instock availability'}).get_text().strip()


# Method - 1
book_name = [result.find('h3').find('a').get('title') for result in results]
price=[result.find('p',{'class':'price_color'}).get_text() for result in results]
stock=[result.find('p',{'class':'instock availability'}).get_text().strip() for result in results]


book_info=pd.DataFrame({'Name':book_name,'Price':price,'Availability':stock})  

book_info.to_csv('book_website',index=False)
