#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
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

    print(response)
    # check if the link goes to a pdf

    # if it does, scrape it

    #if not, ignore it and move on to the next link

    # write that data to the csv


    return