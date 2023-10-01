from openpyxl import Workbook
from itemadapter import ItemAdapter


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
