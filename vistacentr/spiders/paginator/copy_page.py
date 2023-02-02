import requests
import os

def get_page():
    response = requests.get(url="https://vista-centr.ru/catalog/catalog-search/?cur_cc=766&action=index&admin_mode=&search_userquery=%D1%88%D0%B0%D0%BC%D0%BF%D1%83%D0%BD%D1%8C&curPos=360")
    with open(file="copy_page.html", mode="w") as file:
        file.write(response.text)
    


get_page()
