# Packages
from bs4 import BeautifulSoup
import requests 
import pandas as pd

# HTTP Request
#store website in variable
website='https://www.cars.com/shopping/results/?stock_type=new&makes%5B%5D=mercedes_benz&models%5B%5D=&list_price_max=&maximum_distance=20&zip='

# Get Request
response=requests.get(website)

#Status Code
response.status_code
a=response.status_code


soup=BeautifulSoup(response.content,'html.parser')


#https://github.com/istar0me/udacity-introduction-to-python-programming/blob/master/L3_data_structure/README.md
#https://github.com/udacity-china-translation/yaml-translation-2017-07-liam-august-h/blob/master/ud1110/en-us/3_Data%20structures%20and%20Loops.yaml


results = soup.find_all('div',{'class':'vehicle-card'})

results[0].find('h2').get_text()
results[0].find('span',{'class':'primary-price'}).get_text()
results[0].find('div',{'class':'dealer-name'}).get_text()
results[0].find('span',{'class':'sds-rating__count'}).get_text()
results[0].find('span',{'class':'sds-rating__link'}).get_text()




name=[]
dealer_name=[]
rating=[]
review_count=[]
price=[]


for result in results:


  # NAME
  try:
    name.append(result.find('h2').get_text())
  except:
    name.append('NA')  
  
  # PRICING
  try:
    price.append(result.find('span',{'class':'primary-price'}).get_text())
  except:
    price.append(0)

  # CAR DEALING COMPANY
  try:
    dealer_name.append(result.find('div',{'class':'dealer-name'}).get_text().strip())
  except:
    dealer_name.append('NA')

  # RATING
  try:
    rating.append(result.find('span',{'class':'sds-rating__link'}).get_text())
  except:
    rating.append(0)

  # REVIEW COUNT
  try:
    review_count.append(result.find('span',{'class':'sds-rating__count'}).get_text())
  except:
    review_count.append(0)





car_dealer = pd.DataFrame({'Name':name,'Price':price,'Dealer':dealer_name,'Rating':rating,'Review':review_count})


car_dealer['Rating']=car_dealer['Rating'].apply(lambda x:x.strip('reviews)').strip('('))

car_dealer.to_excel('Car_Dealer.xlsx',index=False)
print("DONE!!")




name=[]
price=[]
dealer_name=[]
rating=[]
review_count=[]


for i in range(1,11):
  
  # Website into a Variable
  website="https://www.cars.com/shopping/results/?page=" +str(i)+ "&page_size=20&list_price_max=&makes[]=mercedes_benz&maximum_distance=20&models[]=&stock_type=new&zip="

  # Request to Website
  response=requests.get(website)

  # SOUP Object
  soup=BeautifulSoup(response.content,'html.parser')

  #Results
  results=soup.find_all('div',{'class':'vehicle-card'})
  

  for result in results:
    # NAME
    try:
      name.append(result.find('h2').get_text())
    except:
      name.append('NA')  
  
    # PRICING
    try:
      price.append(result.find('span',{'class':'primary-price'}).get_text())
    except:
      price.append(0)

    # CAR DEALING COMPANY
    try:
      dealer_name.append(result.find('div',{'class':'dealer-name'}).get_text().strip())
    except:
      dealer_name.append('NA')

    # RATING
    try:
      rating.append(result.find('span',{'class':'sds-rating__link'}).get_text())
    except:
      rating.append('NA')

    # REVIEW COUNT
    try:
      review_count.append(result.find('span',{'class':'sds-rating__count'}).get_text())
    except:
      review_count.append(0)



car_dealer = pd.DataFrame({'Name':name,'Price':price,'Dealer':dealer_name,'Rating':rating,'Review':review_count})
car_dealer 


car_dealer['Rating']=car_dealer['Rating'].apply(lambda x:x.strip('reviews)').strip('('))
car_dealer


car_dealer.to_excel('Car_Dealer.xlsx',index=False)
print("DOuble DOne!")