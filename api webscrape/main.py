# import re
# import requests
# import json
import os
# # screped data list
# new_data = []
# finished_data = []
# data = []

# #ticker data
# top_gainer = []
# top_losser = []

# url = 'https://api.sheety.co/41dd22c7f17a225b8163baf1a4f965e2/finvizdata/sheet1'

# data_1 = {
#     "sheet1":{
#         "topgainer" : data[1],
#         "toplosser" : data[2]
#     }
# }


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

# for i in range(38):
#     if i <19:
#         top_gainer.append(data[i])
        
#     else:
#         top_losser.append(data[i])




# response = requests.post(url, json=data_1)

# print(response.status_code)

# with open('scrapy_scraped_data/scrapy_scraped_data/finviz.txt','r+')as file:
#     file.truncate(0)
      
    