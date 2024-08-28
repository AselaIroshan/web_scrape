import datetime
import json
import scrapy
import http.client
import requests
from Keys import *



##Scrapy spider
class Scrape_Spider(scrapy.Spider):
    name = "finviz"
    data = []
    conn = http.client.HTTPSConnection("n84gy8.api.infobip.com")

    url = f"https://script.google.com/macros/s/{GID}/exec?path=sheet&action=write"


    def start_requests(self):
        urls = "https://finviz.com/"
        yield scrapy.Request(url=urls, callback=self.parse)

    def parse(self, response):
        ## left and right table of finviz web (Data contain table in finviz)
        left = response.xpath('//*[@id="js-signals_1"]')
        right = response.xpath('//*[@id="js-signals_2"]')

        for li in left.xpath('.//tr'):
            self.clear_data(li)
        for li in right.xpath('.//tr'):
            self.clear_data(li)

        self.Api_sms()
        self.Api_Gsheet()
        
    ##send a SMS 
    def Api_sms(self):
        payload = json.dumps({
            "messages": 
            [
                {
                    "destinations": [{"to":p_NUMBER}],
                    "from": "StockData",
                    ##sms contain
                    "text": f"Today top gain ticker is {self.data[0]["name"]},volume {self.data[0]["volume"]} and change {self.data[0]["change"]}"
                }
            ]
        })
        headers = {
            'Authorization': Auth_ID,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.conn.request("POST", "/sms/2/text/advanced", payload, headers)
        res = self.conn.getresponse()
        print(res.read())

    def Api_Gsheet(self):
        response = requests.post(self.url, json={"Users": self.data})
        print(response.text)


    ##extract data from single tag
    def clear_data(self,single_data):

        name = single_data.xpath(".//td[1]/a/text()").get()
        price = single_data.xpath(".//td[2]/text()").get()
        change = single_data.xpath(".//td[3]/span/text()").get()
        volume = single_data.xpath(".//td[4]/text()").get()
        signal = single_data.xpath(".//td[6]/a/text()").get()

        self.data.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "name": name,
            "price": price,
            "change": change,
            "volume": volume,
            "signal": signal
        })