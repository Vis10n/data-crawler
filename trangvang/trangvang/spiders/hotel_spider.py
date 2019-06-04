import scrapy
import csv
import re

# File labels
data_hotel_file = 'D:\Documents\Work\Data Crawler\\trangvang\\trangvang\spiders\data\hotel.csv'

class HotelSpider(scrapy.Spider):
    name = "hotelSpider"
    start_urls = [
        'https://trangvangvietnam.com/categories/127160/khach-san.html'    
    ]

    def parse(self, response):
        print("cmm Thanh!")

        print("Prepare something...")
        with open(data_hotel_file, 'a', newline='', encoding='utf8') as dataFile:
            row = ['COMPANY_NAME', 'EMAIL_ADDRESS', 'TELE_NUMBERS']
            writer = csv.writer(dataFile)
            writer.writerow(row)
        dataFile.close()

        start_url = 'https://trangvangvietnam.com/categories/127160/khach-san.html'
        finalPage = start_url + response.xpath('//div[@id="contentglobals"]/div[@id="main_seach"]/div[@id="main_seachl"]/div[@id="listingsearch"]/div[@id="paging"]/a/@href')[-2].extract()
        totalPage = int(finalPage.split("=")[-1])

        print("Begin the party!!")
        for page in range(int(totalPage)):
            link = finalPage.replace(str(totalPage), str(page + 1))
            print(link)
            yield scrapy.Request(link, callback=self.crawlHotel)

    def crawlHotel(self, response):
        for linkHotel in response.xpath(
                '//div[@id="contentglobals"]/div[@id="main_seach"]/div[@id="main_seachl"]/div[@id="listingsearch"]/div[@class="boxlistings"]/div[@class="listings_top"]/div[@class="noidungchinh"]/h2[@class="company_name"]/a/@href'
                ).extract():
            yield scrapy.Request(linkHotel, callback=self.saveFile)
    
    def saveFile(self, response):
        companyNameRaw = response.xpath('//div[@id="contentglobals"]/div[@id="listing_detail_left"]/div[@id="listing_basic_info"]/div[@class="tencongty"]/h1/text()').get()
        emailRaw = response.xpath('//div[@id="contentglobals"]/div[@id="listing_detail_left"]/div[@id="listing_basic_info"]/div[@class="email_website"]/div[@class="box_email_website"]/div[@class="text_email"]/p/a/text()').get()
        teleNumberRaw = response.xpath('//div[@id="contentglobals"]/div[@id="listing_detail_left"]/div[@id="listing_basic_info"]/div[@class="logo_diachi_xacthuc"]/div[@class="diachi_chitietcongty"]/div[@class="diachi_chitiet_li"]/div[@class="diachi_chitiet_li2"]/span/text()').get()
        print(str(companyNameRaw))
        companyName = str(companyNameRaw)
        email = str(emailRaw)
        teleNumber = str(re.search(r'[0-9\(\)\.\,\s]+', teleNumberRaw).group())
        with open(data_hotel_file, 'a', newline='', encoding='utf8') as dataFile:
            row = [companyName, email, teleNumber]
            writer = csv.writer(dataFile)
            writer.writerow(row)
        dataFile.close()