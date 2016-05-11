'''
Created on Feb 10, 2016

@author: niormsby
'''

class Scraper(object):
    '''
    classdocs
    Base Class for AliExpress and Amazon Scrapers
    '''
    def navigateToAmazon(self, driver):        
        print("inside the def navigateToAmazon(self, driver): ")
        driver.get("http://www.amazon.com")
        
    def navigateToAliExpress(self, driver):        
        driver.get("http://www.aliexpress.com")

    