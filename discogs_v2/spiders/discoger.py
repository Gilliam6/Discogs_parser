import scrapy
import re 
from bs4 import BeautifulSoup
import time
mega_links = []
class DiscogerSpider(scrapy.Spider):
    name = 'discoger'
    allowed_domains = ['discogs.com']
    start_urls = ['https://www.discogs.com']
    with open("xml_release_links.txt", "r") as f: #сохраним все ссылки (13664694) в переменной
        for row in f:
            mega_links.append(row)
    print(len(mega_links))
    print(mega_links[0])
    def parse(self, response): #Функция частичной обработки ссыллок стеками по 500 000
        n = 1
        count = 0
        links = mega_links

        while count < 500000:
             yield scrapy.Request(links[count], callback = self.stack_parse)
             count += 1
        pass

    def stack_parse(self, response): #Функция парсинга отдельных страниц
        soup = BeautifulSoup(response.text, 'html.parser')
        name = []
        info = []
        url = []
        head = soup.find('div', re.compile("body\w*"))
        h1 = head.find_all('h1')
        content = head.find('div', re.compile("info\w*"))
        for n in h1:
            tempt = n.text
            name.append(tempt)
        for c in content:
            tempi = c.text
            split = re.split(r':', tempi, maxsplit=1)
            info.append(split)
        url.append(response.url)
        print(url)
        scraped_data = dict(info)
        scraped_data['name'] = name[0]
        scraped_data['url'] = url[0]
        print(scraped_data)
        yield scraped_data

        
        

