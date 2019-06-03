import scrapy

class QuotesSpider(scrapy.Spider):
        name = "hotel"
        start_url = [
            'https://trangvangvietnam.com/categories/127160/khach-san.html'    
        ]

        def parse(self, response):
            print("cmm Thanh!")
            start_url = 'https://trangvangvietnam.com/categories/127160/khach-san.html'
            finalPage = start_url + response.xpath('//div[@id="contentglobals"]/div[@id="main_seach"]/div[@id="main_seachl"]/div[@id="listingsearch"]/div[@id="paging"]/a/@href')[-2].extract()
            totalPage = int(finalPage.split("=")[-1])
            for page in range(int(totalPage)):
                link = finalPage.replace(str(totalPage), str(page + 1))
                print(link)
                yield scrapy.Request(link, callback=self.crawlHotel)

        def crawlHotel(self, response):
            for linkHotel in response.xpath('//div[@id="contentglobals"]/div[@id="main_seach"]/div[@id="main_seachl"]/div[@id="listingsearch"]/div[@class="boxlistings"]/div[@class="listings_top"]/div[@class="noidungchinh"]/h2[@class="company_name"]/a/@href').extract():
                print(linkHotel)
                yield scrapy.Request(linkHotel, callback=self.saveFile)
        
        def saveFile(self, response):
            companyNameRaw = response.xpath('//div[@id="contentglobals"]/div[@id="listing_detail_left"]/div[@id="listing_basic_info"]/div[@class="tencongty"]/h1/text()').extract()
            print(companyNameRaw)