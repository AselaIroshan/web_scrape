import re
import requests
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy_scraped_data.scrapy_scraped_data.spiders.asela import finviz
import url_api 

# url of the API
url = url_api.url_api1

# screped data list
new_data = []
finished_data = []
data = []

#ticker data
top_gainer = []
top_losser = []

# run scrapy
process = CrawlerProcess()
process.crawl(finviz)
process.start()
      

# filter data

with open('scrapy_scraped_data/scrapy_scraped_data/finviz.txt','r')as file:
    lines = file.readlines()
    for line in lines:
        u_line = re.sub("=","", line)
        new_data.append(u_line)

for i in new_data:
    lines = re.sub(">", "", i)
    finished_data.append(lines)

for i in finished_data:
    line = re.sub("data", "",i)
    data.append(line)



for i in range(38):
    if i <19:
        top_gainer.append(data[i])
        data_1 = {
            "sheet1":{
                "topgainer" : data[i],
            }
        }
        # send to google sheet via api
        response = requests.post(url, json=data_1)
        print(response.status_code)
        
        
    else:
        top_losser.append(data[i])
        data_1 = {
            "sheet1":{
                "toplosser" : data[i]
            }
        }
        # send to google sheet via api
        response = requests.post(url, json=data_1)
        print(response.status_code)

#after sent to the google sheet, finviz data will be deleat

with open('scrapy_scraped_data/scrapy_scraped_data/finviz.txt','r+')as file:
    file.truncate(0)

