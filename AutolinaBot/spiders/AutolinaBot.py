import scrapy
from AutolinaBot.items import AutolinabotItem
import logging
import time
import csv

class AutolinaBotSpider(scrapy.Spider):

    name = "AutolinaBot"

    allowed_domain = ['https://m.autolina.ch']

    Output = {} # Stores the extracted information
    '''
        custom settings, log file is out.log, output file and output format(csv)
    '''
    custom_settings = {
        'LOG_ENABLED': True,
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': 'out.log',
        'FEED_URI': 'Output_Files/ExportedFile_%(time)s.csv',
        'FEED_FORMAT': 'csv'
    }

    # This micmics the next page buttons and get all the pages
    start_urls = [
        f'https://m.autolina.ch/en/carList?sort=year_desc&page={page}' for page in range(1,10)
        ]
    

    def parse(self, response):
        """ACCESSES ALL INDIVIDUAL SEARCH DIRECTORIES"""
        
        logging.info("Processing url " + str(response.request.url))

        for href, year in zip(response.xpath("//li[re:test(@class, 'car-title')]/a[re:test(@class, 'carDetailsAnchor')]//@href"), response.xpath("//li[re:test(@class, 'year')]/p/text()").getall()):
            # Add the scheme for proper format
            self.year = year
            url = "https://m.autolina.ch" + href.get()
            yield scrapy.Request(url, callback=self.parse_content)
            

    def parse_content(self, response, **Output):
        """SCRAPES VEHICLE DATA AND EXPORTS TO CSV"""

        time.sleep(2) # Delay

        # Getting Vehicle Name
        name = response.xpath("//div[re:test(@class, 'heading')]//text()").getall()[1].split("\n")[0]
        if name is not None:
            Output['VEHICLE NAME'] = name
            Output['MAKE'] = name.split(" ")[0]
            Output['MODEL'] = name.split(" ")[1]
        else:
            pass
        logging.info("Started Scraping Process")

        Output['YEAR'] = self.year

        # All needed tags on page
        tag = response.xpath("//div[re:test(@class, 'tables carDtls-properties')]/div/ul/li[1]//text()").getall()
        tags = [x.strip() for x in tag]
        length = len(tags)

        # All needed information on page
        data = response.xpath("//div[re:test(@class, 'tables carDtls-properties')]/div/ul/li[2]/b/text()").getall()
        chan = [x.strip() for x in data]
        content = [x for x in chan if x]


        for each in range(length):
            if tags[each] == 'Mileage':
                Output['KM'] = content[each].split(" ")[0]
                Output['KM_UNIT'] = 'KM'
            elif tags[each] == 'Power':
                Output['KW'] = content[each].split(" ")[0]
                Output['KW_UNIT'] = 'KW'
                if len(content[each].split(" ")) > 3:
                    Output['PS'] = content[each].split(" ")[3]
                    Output['PS_UNIT'] = 'PS'

            elif tags[each] == 'Cubic Capacity':
                Output['CAPACITY'] = content[each].split(" ")[0]
                Output['CAPACITY UNIT'] = 'cc'
            elif tags[each] == 'Price':
                Output['PRICE'] = int(content[each].split(' ')[1][:2] + content[each].split(' ')[1][3:6])
                Output['CURRENCY'] = 'CHF'
            else:
                Output[tags[each]] = content[each]

        # Store page url
        Output['URL'] = response.request.url
        logging.info("Scraping Successful")

        yield Output