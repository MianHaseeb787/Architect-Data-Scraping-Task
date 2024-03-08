# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
from itemadapter import ItemAdapter


class EmpdataPipeline:
    def process_item(self, item, spider):


        adapter = ItemAdapter(item)

        #removing telephone from phone number
        value =  adapter.get('telephone')
        new_val = re.sub(r'\D', '', value)
        adapter['telephone'] = new_val



        # removing email from mail strings
        mail_value = adapter['email']
        mail_list = mail_value.split()
        new_mail_value = mail_list[1]
        adapter['email'] = new_mail_value
        
        
        return item
    
