import re
import requests
import json

# new_data = []
# finished_data = []
# data = []
# last = []

# with open('scrapy_scraped_data/scrapy_scraped_data/finviz.txt','r')as file:
#     lines = file.readlines()
#     for line in lines:
#         u_line = re.sub("=","", line)
#         new_data.append(u_line)
# for i in new_data:
#     lines = re.sub(">", "", i)
#     finished_data.append(lines)

# for i in finished_data:
#     line = re.sub("data", "",i)
#     data.append(line)


datas = {
    "sheet1":{
        "ticker":"asela"
    }
}


url = 'https://api.sheety.co/41dd22c7f17a225b8163baf1a4f965e2/finvizdata/sheet1'
response = requests.post(url, json=datas)

print(response.status_code)
    
    
        
        
        
    



