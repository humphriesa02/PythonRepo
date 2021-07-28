from bs4 import BeautifulSoup
from datetime import date
import requests

html_text = requests.get('https://store.steampowered.com/specials/#p=0&tab=TopSellers').text

soup = BeautifulSoup(html_text, 'lxml')

list = soup.find('div', id = 'TopSellersRows')
listElements = list.find_all('a')

print('Steam Top Sellers Discounts for: ' + str(date.today()))
for elements in listElements:
    #listImg = elements.find('div','col search_capsule')
    listName = elements.find('div', class_ = 'tab_item_name').text
    listDiscount = elements.find('div', class_ = 'discount_pct').text.replace(' ', '')
    origPrice = elements.find('div', class_ = 'discount_original_price').text
    discountPrice = elements.find('div', class_ = 'discount_final_price').text
    print('Name: ' +listName)
    print('Discount: ' +listDiscount)
    print('Original Price: ' +origPrice)
    print('Discount Price: ' +discountPrice)
    print('')
    
