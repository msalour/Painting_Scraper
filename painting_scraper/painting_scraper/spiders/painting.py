import scrapy
from painting_scraper.items import PaintingScraperItem
from scrapy.loader import ItemLoader
from urllib.parse import urljoin

class PaintingSpider(scrapy.Spider):
    name = "painting"
    start_urls = ["https://www.californiawatercolor.com/collections/original-california-paintings-for-sale"]
    cols=["Title", "Artist","Size"]
    def __init__(self):
        super().__init__()
        self.page_count= 0
    def parse(self, response):
        self.page_count += 1
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

        print("[ PAGE COUNT]:",self.page_count)
        pagination_div = response.css('div.pagination.wide')

        if pagination_div:
            # Extract the next page URL and its href
            next_page_element = pagination_div.css('a:contains("Next →")')
            if next_page_element:
                next_page_url = next_page_element.xpath("@href").get()
                full_next_page_url = urljoin(self.start_urls[0], next_page_url)
                print("Next Page URL:", full_next_page_url)
                yield scrapy.Request(url=full_next_page_url)
                
            else:
                print("Next page not found.")
        else:
            print("Pagination div not found.")


            # painting_item=PaintingScraperItem()
            # painting_item['title'] = painting.css("a.coll-prod-title::text").get()
            # painting_item['artist'] = painting.css("div.product-item-vendor::text").get()
            # painting_item['size'] = painting.css("div.origsizecol::text").get()

            # print("Title: ", painting_item['title'])
            # print("Artist: ", painting_item['artist'])
            # print("Size: ", painting_item['size'])
            # print("-----------------------------------")

           # yield painting_item  # Properly indented yield statement
           