import requests
from bs4 import BeautifulSoup

from math import ceil



def get_max_page_num():    
    response = requests.get(url="https://vista-centr.ru/catalog/catalog-search/?cur_cc=766&action=index&admin_mode=&search_userquery=шампунь")
    
    soup = BeautifulSoup(response.content, "lxml")

    # Общее количество товаров
    nunbers_product = int(soup.find("span", class_="product-list-total-count-value").text)   

    print(f"\n  [!] Количество товаров всего: {nunbers_product}") 
    
    # Вычисляю общее количество страниц, поделив Количество товаров/количество товаров на одной странице
    # max_page_num = round((nunbers_product/30)+1)
    max_page_num = ceil(nunbers_product/30)

    print(f"\n [!] Количество страниц: {max_page_num}")

    return max_page_num


# print(get_max_page_num())

