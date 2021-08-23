from bs4 import BeautifulSoup
import requests
import pandas as pd

# Create Empty Data Frame

real_estate_multiple=pd.DataFrame(columns=['Street','Regions','Beds','Baths','Price'])

# Website Request - Code for Scrapping Multiple Pages

for i in range(1,4):
  website=requests.get('https://www.trulia.com/NY/New_York/' +str(i)+ '_p/')

  # Create soup object
  soup=BeautifulSoup(website.content,'html.parser')

  # Result
  result=soup.find_all('li',{'class':'SearchResultsList__WideCell-b7y9ki-2'})
  
  # Update Results

  results_update=[]
  for r in result:
    if r.has_attr('data-testid'):
      results_update.append(r)

  streets=[result.find('div',{'data-testid':'property-street'}).get_text() for result in results_update]
  pricing=[result.find('div',{'data-testid':'property-price'}).get_text() for result in results_update]
  regions=[result.find('div',{'data-testid':'property-region'}).get_text() for result in results_update]
  bed=[result.find('div',{'data-testid':'property-beds'}).get_text().replace("bd",'') for result in results_update]
  bathroom=[result.find('div',{'data-testid':'property-baths'}).get_text().replace("ba",'') for result in results_update]


  for k in range(len(streets)):
    real_estate_multiple=real_estate_multiple.append({'Street':streets[k],'Regions':regions[k],'Beds':bed[k],'Baths':bathroom[k],'Price':pricing[k]},ignore_index=True)
    
    
real_estate_multiple.info()

real_estate_multiple.to_excel('real_estate_multiple_pages.xlsx',index=False)
