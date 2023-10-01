import scrapy
from painting_scraper.items import PaintingScraperItem
from scrapy.loader import ItemLoader

class PaintingSpider(scrapy.Spider):
    name = "painting"
    start_urls = ["https://www.californiawatercolor.com/collections/original-california-paintings-for-sale"]
    cols=["Title", "Artist","Size"]
    
    def parse(self, response):
        """
        Parse the response from the website and extract painting information.

        Args:
            response (scrapy.http.Response): The response object from the website.

        Yields:
            dict: A dictionary containing information about each painting, including title, artist, and size.
        """
        self.logger.info("Received response from %s", response.url)

        paintings = response.css("body div div ul#coll-product-list.clearfix li")
        for painting in paintings:
            loader=ItemLoader(item=PaintingScraperItem(), selector=painting)
            loader.add_css('title', "a.coll-prod-title::text")
            loader.add_css('artist', "div.product-item-vendor::text")
            loader.add_css('size', "div.origsizecol::text")
            yield loader.load_item()
            
            # painting_item=PaintingScraperItem()
            # painting_item['title'] = painting.css("a.coll-prod-title::text").get()
            # painting_item['artist'] = painting.css("div.product-item-vendor::text").get()
            # painting_item['size'] = painting.css("div.origsizecol::text").get()

            # print("Title: ", painting_item['title'])
            # print("Artist: ", painting_item['artist'])
            # print("Size: ", painting_item['size'])
            # print("-----------------------------------")

           # yield painting_item  # Properly indented yield statement
           