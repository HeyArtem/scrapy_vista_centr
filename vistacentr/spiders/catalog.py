import scrapy

from .paginator.pagination import get_max_page_num


class CatalogSpider(scrapy.Spider):
    name = "catalog"
    allowed_domains = ["vista-centr.ru"]
    start_urls = ["http://vista-centr.ru/"]

# этот метод вызывается при запуске парсера, формирует адреса страниц, где будут находится карточки с товарами. По этим url-ам буду отправлять паука, что бы он парсил    
    def start_requests(self):
        # last_page_num = get_max_page_num()

        # print(f"\n  [!] Количество товаров всего: {last_page_num}")

        # for page in range(1, last_page_num + 1):
        for page in range(1, 3):
        
            url = f"https://vista-centr.ru/catalog/catalog-search/?cur_cc=766&action=index&admin_mode=&search_userquery=шампунь&curPos={(page - 1) * 30}"

            print(f" [!] work page: {url}")

            # yield - выражение для генераторной ф-ции, будет выдавать по одному url за запрос
            yield scrapy.Request(url=url, callback=self.parse_pages)
            

    # response-принимает страницу, собираю ссылки на карточки
    def parse_pages(self, response, **kwargs):

        print("\n [!] start on parse_pages")

        # достаю все ссылки, неребираю в цикле        
        for href in response.css("div.price + a::attr('href')").extract():        

            # print(f"\n [!] href on product: {href}")

            # формирую новый url
            url = response.urljoin(f"https://vista-centr.ru{href}")

            # print(f"\n [!] url on product: {url}")

            # делаю запрос, обращаюсь к ф-ции parse
            yield scrapy.Request(url, callback=self.parse)
            

    def parse(self, response, **kwargs):
        item = {
            "title": response.css("h1::text").extract_first("").strip(),
            "price": response.css("span.price::text").extract_first("").strip(),
            "url": response.request.url,
        }
        # print(f" [!] title & url: {item['title']} \n {item['url']}")
        yield item
