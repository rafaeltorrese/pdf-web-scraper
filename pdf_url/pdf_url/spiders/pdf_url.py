#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
import re 
from ..items import PdfUrlItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PdfUrlSpider(CrawlSpider):

    #
    name = 'pdf_url'

    allowed_domains = ['adobe.com']

    #
    start_urls = ['https://www.adobe.com']

    #
    # This Rule says:
    # 1. allow all links to be extracted
    # 2. call response_httpresponse on each extracted link
    # 3. follow all links ("click" on them) so we can check all the links on THAT webpage too
    rules = [Rule(LinkExtractor(allow=''), callback='parse_httpresponse' , follow=True)]


    def parse_httpresponse(self,response):

        print(response.url)
        item = PdfUrlItem()

        # check if the link goes to a pdf
        # if it does, scrape it
        #if not, ignore it and move on to the next link
        if ('Content-Type' in response.headers.keys()) and ('pdf' in response.headers['Content-Type']):
            if 'Content-Disposition' in response.headers.keys():
                ContentDisposition = str(response.headers['Content-Disposition'])
                item['filename'] = re.search('filename="(.+)"', ContentDisposition).group(1)
            else:
                item['filename'] = response.url.split('/')[-1]
            item['url'] = response.url
 
        # write that data to the csv
        return item
