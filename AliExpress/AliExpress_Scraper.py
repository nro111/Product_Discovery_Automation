'''
Created on May 11, 2016

@author: niormsby
'''
from Web_Listing import Web_Listing
from selenium import webdriver

class AliExpress_Scraper(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def searchFor(self, amazonItems, driver):
        '''
        Takes in a list of items to search for on AliExpress
        '''
        aliExpress_WebListings = [] 
        driver.get("http://www.aliexpress.com/")
        searchBox = driver.find_element_by_id("search-key").clear()
        for amazonItem in amazonItems:
            web_Listing = Web_Listing
            searchBox.send_Keys(amazonItem)
            web_Listing.setItemName(driver.find_element_by_class())
            web_Listing.setDescription(driver.find_element_by_class())
            web_Listing.setItemPrice(driver.find_element_by_class())
            web_Listing.setShippingPrice(driver.find_element_by_class())            
            web_Listing.setImage(driver.find_element_by_class())            
            web_Listing.setNumberOfProductsAvaliable(driver.find_element_by_class())
            web_Listing.setItemSerialNumber(driver.find_element_by_class())
            web_Listing.setPackageSize(driver.find_element_by_class())
            web_Listing.setPackageWeight(driver.find_element_by_class())
            web_Listing.setEstimatedDeliveryTime(driver.find_element_by_class())
            web_Listing.setReturnPolicy(driver.find_element_by_class())
            aliExpress_WebListings.add(web_Listing)

        return aliExpress_WebListings
    
    def searchFor(self, amazonItem, driver):
        '''
        Takes in a single item to search for on AliExpress
        '''     
        web_Listing = Web_Listing   
        driver.get("http://www.aliexpress.com/")
        searchBox = driver.find_element_by_id("search-key").clear()
        searchBox.send_Keys()  
        web_Listing.setItemName(driver.find_element_by_class())
        web_Listing.setDescription(driver.find_element_by_class())
        web_Listing.setItemPrice(driver.find_element_by_class())
        web_Listing.setShippingPrice(driver.find_element_by_class())            
        web_Listing.setImage(driver.find_element_by_class())            
        web_Listing.setNumberOfProductsAvaliable(driver.find_element_by_class())
        web_Listing.setItemSerialNumber(driver.find_element_by_class())
        web_Listing.setPackageSize(driver.find_element_by_class())
        web_Listing.setPackageWeight(driver.find_element_by_class())
        web_Listing.setEstimatedDeliveryTime(driver.find_element_by_class())
        web_Listing.setReturnPolicy(driver.find_element_by_class())  
        
        return web_Listing