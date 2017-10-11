# -*- coding: utf-8 -*-
import scrapy


class ShopcluesSpider(scrapy.Spider):
    name = "shopclues"
    allowed_domains = ["www.shopclues.com/mobiles-featured-store-4g-smartphone.html"]
    start_urls = ['http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html/']

    def parse(self, response):
        #Extracting the content using css selectors
        img = response.css("img::attr(data-img)").extract()
        name = response.css("img::attr(title)").extract()
        price = response.css(".p_price::text").extract()
        discount = response.css(".prd_discount::text").extract()
        #location of csv file
        custom_setting = {'FEED_URI':'tmp/shopclues.csv'}
        #Give the extracted content row wise
        for item in zip(img,name, price, discount):
            #create a dictionary to store the scraped info
            scraped_info = {
                'img' : item[0],
                'name' : item[1],
                'price' : [item[2]], #Set's the url for scrapy to download images
                'discount' : item[3]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info        
