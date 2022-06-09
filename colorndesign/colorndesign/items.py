# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst

class ColorndesignItem(scrapy.Item):
    # define the fields for your item here like:
    name =          scrapy.Field()
    Sku =           scrapy.Field()
    color =         scrapy.Field()
    Breadcrumbs =   scrapy.Field()
    Product_Url =   scrapy.Field()

    # job_id =        scrapy.Field()
    # job_time =      scrapy.Field()
    # timestamp =     scrapy.Field()
    # spider =        scrapy.Field()
    # url =           scrapy.Field()
