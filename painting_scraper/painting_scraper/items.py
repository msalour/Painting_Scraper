# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from itemloaders.processors import MapCompose,TakeFirst
  
class PaintingScraperItem(Item):
     # define the fields for your item here like:
    title = Field(
        output_processor=TakeFirst()
    )
    artist = Field(
         output_processor=TakeFirst()
    )
    size = Field(
         output_processor=TakeFirst()
    )
