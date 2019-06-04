import scrapy
import pdb
import re
class NewsSpider(scrapy.Spider):
  name = "tech-industry"
  start_urls = [ 'https://trangvangvietnam.com/categories/127160/khach-san.html']

  def parse(self, response):
    source = "https://www.cnet.com"
    list_topic = response.xpath('//section[@id="topicListing"]/div')
    links =  list_topic[1].xpath('//div[@class = "row asset"]/div[@class="col-2 assetThumb"]/a/@href').extract()
    regex = r"\/news\/.*"
    print("cmm")
