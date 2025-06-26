
import scrapy
import csv



class TopFundsSpider(scrapy.Spider):
    name = 'top_funds'
    start_urls = ['https://sarmaaya.pk/mutual-funds/top-performing']  # Replace with the actual URL


    def parse(self, response):

        # Open a CSV file to write data
        with open('top_100_funds.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'link', '1D', '30D',"1Y"])
            writer.writeheader()

            average_year_growth = []
            rows = response.xpath('//*[@id="top-funds"]/tbody/tr')

            #num_etfs = response.xpath('/html/body/div/section[1]/div/div[2]/div[1]/div[4]/div[2]/div/div[3]/div[1]/div')


            for i in range(1, 504):
                name = response.xpath(f'//*[@id="top-funds"]/tbody/tr[{i}]/td[1]/a/text()').get()
                link = response.xpath(f'//*[@id="top-funds"]/tbody/tr[{i}]/td[1]/a/@href').get()
                col2 = response.xpath(f'//*[@id="top-funds"]/tbody/tr[{i}]/td[2]/text()').get()
                col4 = response.xpath(f'//*[@id="top-funds"]/tbody/tr[{i}]/td[4]/text()').get()
                col8 = response.xpath(f'//*[@id="top-funds"]/tbody/tr[{i}]/td[8]/text()').get()

                average_year_growth.append(col8)
                row = []
                writer.writerow({
                    'name': name,
                    'link': link,
                    '1D': col2,
                    '30D':col4,
                    "1Y":col8,
                })


            print(f"the average year on year growth for all funds in pakistan was {average_year_growth}last year")









if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
    
    process = CrawlerProcess()
    process.crawl(TopFundsSpider)
    process.start()

#response.xpath('//*[@id="top-funds"]/tbody/tr[2]/td[1]/a/text()').get()
#//*[@id="top-funds"]/tbody/tr[100]/td[1]/a#






# Open a CSV file to write data
