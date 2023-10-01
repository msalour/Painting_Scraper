import scrapy

class PaintingSpider(scrapy.Spider):
    name = "painting"
    start_urls = ["https://www.californiawatercolor.com/collections/original-california-paintings-for-sale"]

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
            title = painting.css("a.coll-prod-title::text").get()
            artist = painting.css("div.product-item-vendor::text").get()
            size = painting.css("div.origsizecol::text").get()

            print("Title: ", title)
            print("Artist: ", artist)
            print("Size: ", size)
            print("-----------------------------------")