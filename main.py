from fastapi import FastAPI
from bs4 import BeautifulSoup
import pandas as pd
import requests
import json

app = FastAPI()
 
def bot():

    link = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')

    products=[]
    prices=[]
    description=[]
    reviews_number=[]
    stars=[]

   
    for a in soup.find_all('div', attrs={'class':'thumbnail'}):
        name=a.find('a').attrs.get('title')
        price=a.find('h4', attrs={'class':'pull-right price'})
        info= a.find('p', attrs={'class':'description'})
        reviews=a.find('p', attrs={'class':'pull-right'})
        star=a.select('p[data-rating]')[0].attrs.get('data-rating')

        if 'Lenovo' in name:
            products.append(name)
            prices.append(price.text)
            description.append(info.text)
            reviews_number.append(reviews.text)
            stars.append(star)

    df = pd.DataFrame({'product_name':products,'price':prices, 'description':description, 'reviews_number':reviews_number,'stars':stars})
    df.sort_values(by=['price'])
    return df

@app.get("/")
async def root():
    data = bot()
    result = json.loads(data.to_json(orient="index"))
    return result