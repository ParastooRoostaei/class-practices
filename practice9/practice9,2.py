import requests
import os
from bs4 import BeautifulSoup
res = requests.get("https://www.entekhabcenter.com/product-category/product/audio-video/television")
soup = BeautifulSoup(res.content,"html.parser")
items1 = soup.select('.col-lg-3.col-md-3.archive-card-m.col-sm-12.product-item')
product = "Product Name, Product Price\n"
productsList = ""
for item1 in items1:
    itemsName = item1.select("div>div>div>a>h5")
    itemsPrice = item1.select("div>div>div>div>ins>b")
    for item in itemsName:
        productsList += item.text + (",")
    for item in itemsPrice:
        productsList += item.text + ("\n")
product += productsList
print(product)
with open('product.csv','a', encoding='utf-8') as productInfow:
    productInfow.write(product)