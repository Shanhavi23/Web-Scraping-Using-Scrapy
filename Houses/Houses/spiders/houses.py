import scrapy
from ..items import HousesItem

class HousesSpider(scrapy.Spider):
    name = "houses"
    start_urls = ["https://www.magicbricks.com/independent-house-for-sale-in-new-delhi-pppfs",
                  'https://www.magicbricks.com/independent-house-for-sale-in-ahmedabad-pppfs']

    def parse(self, response):
        items=HousesItem()

        all_houses=response.css('div.mb-srp__list')
        for house in all_houses:
            address=house.css('h2.mb-srp__card--title::text').extract()
            price=house.css('div.mb-srp__card__price--amount::text').extract()
            area=house.css('div.mb-srp__card__price--size::text').extract()
            furnishing=house.css('div.mb-srp__card__summary__list--item div.mb-srp__card__summary--value::text')[3].extract()

            items['address']=address
            items['price']=price
            items['area']=area
            items['furnishing']=furnishing

            yield items

            next_page=response.css('li.mb-pagination--next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)