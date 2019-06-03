import scrapy

class QuotesSpider(scrapy.Spider):
    name='test'
    start_url = [
        'https://trangvangvietnam.com/categories/127160/khach-san.html'
    ]

    def parse(self, response):
        print("cmm Thanh!")