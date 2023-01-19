import scrapy

class finviz(scrapy.Spider):
    name = "fin"
    start_urls = [
        'https://finviz.com/',
    ]

    def parse(self, response):
        f_data =[]
        data=response.css('tr.table-light-row-cp')
        for i in data:
            first_data= i.css('a ::text')
            s_data= first_data[0]
            t_data=str(s_data)
            fo_data=t_data.split()
            answer=fo_data[2]
            f_data.append(answer)
        with open("finviz.txt", "w") as file:
            file.writelines("\n".join(f_data))
            
        
        