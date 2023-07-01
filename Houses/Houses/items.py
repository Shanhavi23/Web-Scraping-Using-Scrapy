# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from typing import Any

import scrapy
from scrapy import Field


class HousesItem(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    furnishing = scrapy.Field()
    pass
