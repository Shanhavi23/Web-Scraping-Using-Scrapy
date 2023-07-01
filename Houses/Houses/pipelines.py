# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class HousesPipeline:
    def __init__(self):
        self.curr=None
        self.conn=None
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=mysql.connector.connect(host='localhost',user='root',
                                          password='Shanhavi@4431',database='housesforsale')
        self.curr=self.conn.cursor()

    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS houses''')
        self.curr.execute('''create table houses(
                            address text,
                            price text,
                            area text,
                            furnishing text)''')

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("insert into houses values (%s,%s,%s,%s)",(
            item['address'][0],
            item['price'][0],
            item['area'][0],
            item['furnishing'][0]
        ))
        self.conn.commit()

    def close_spider(self,spider):
        self.curr.close()
        self.conn.close()
