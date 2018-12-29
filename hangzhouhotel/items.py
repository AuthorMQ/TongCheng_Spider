# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class HangzhouhotelItem(scrapy.Item):
    Id=Field()
    Name=Field()
    Address=Field()
    ImgUrl=Field()
    Tell=Field()
    Lon=Field()
    Lat=Field()
    Grade=Field()


class commentItem(scrapy.Item):
    hotelId=Field()
    dpUserName=Field()
    dpId=Field()
    dpDate=Field()
    dpContent=Field()
    replyContent=Field()



