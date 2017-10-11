# -*- coding: utf-8 -*-
import scrapy


class VidyabotSpider(scrapy.Spider):
    name = "vidyabot"
    allowed_domains = ["https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/?utm_source=fbremk"]
    start_urls = ['http://https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/?utm_source=fbremk/']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()
       
        #Give the extracted content row wise
        for item in zip(titles,votes,times,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'created_at' : item[2],
                'comments' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
