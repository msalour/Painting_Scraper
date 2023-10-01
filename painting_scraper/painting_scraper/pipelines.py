from pymongo import MongoClient
from openpyxl import Workbook
from itemadapter import ItemAdapter

     
# Saving Data Locally to Excel
class PaintingScraperPipeline:
    def open_spider(self, spider):
        self.workbook=Workbook()
        self.sheet=self.workbook.active
        self.sheet.title="paintings"
        self.sheet.append(spider.cols)

    def process_item(self, item, spider):
        self.sheet.append([ item['title'], item['artist'], item['size']])
        return item

    def close_spider(self, spider):
        self.workbook.save("paintings.xlsx")   

        #Saving data to Mongo DB
# class PaintingScraperPipeline:
#     def open_spider(self, spider):
#         self.client=MongoClient(
#             host=""
#             connect=False
#         )
#         self.collection=self.client.get_database("Painting").get_collection("Cityscape Art")

#     def process_item(self, item, spider):
#         self.collection.insert_one(
#            # {"title":item['title'],"artist":item['artist'],"size":item['size']}
#            ItemAdapter(item).asdict()
#         )
#         return item

#     def close_spider(self, spider):
#         self.client.close() 
