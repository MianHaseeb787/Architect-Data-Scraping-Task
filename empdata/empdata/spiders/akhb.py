import scrapy
from ..items import EmpItem

class AkhbSpider(scrapy.Spider):
    name = "akhb"
    allowed_domains = ["akhb.de"]
    start_urls = ["https://akhb.de/architektensuche"]

    def parse(self, response):

        emp_item = EmpItem()


        empdata = response.css('.views-row')
        

        for emp in empdata:
            
          emp_item['name'] = emp.css('.views-field-title').css('::text').get()
          emp_item['telephone'] = emp.css('.views-field-field-gob-phone').css('::text').get()
          emp_item['email'] = emp.css('.views-field-field-gob-mail').css('::text').get()


          yield emp_item

        next_url =   response.css('li.pager__item.is-active + li > a::attr(href)').get()
        
        if next_url is not None:
           next_page_url =   'https://www.akhb.de/architektensuche?' + next_url
           yield response.follow(next_page_url, callback = self.parse)




        
            

    
