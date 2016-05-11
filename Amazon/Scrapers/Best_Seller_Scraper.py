'''
Created on Feb 15, 2016

@author: niormsby
'''
from Web_Listing import Web_Listing
from bs4 import element

class Best_Seller_Scraper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def getAmazonBestSellerCategories(self, driver):
        print("inside the def getAmazonBestSellerCategories(self, driver):")
        driver.get("http://www.amazon.com/Best-Sellers/zgbs")
        print("driver was able to get to http://www.amazon.com/Best-Sellers/zgbs")
        categoryTable = driver.find_element_by_id("zg_browseRoot")
        print("found sub category table")
        categoryHolder = categoryTable.find_element_by_tag_name("ul")
        categoryList = categoryHolder.find_elements_by_tag_name("li")
        print("assigned elements to categoryList")
        for categori in categoryList:            
            print(categori)          
        return categoryList
    
    def getSubCategories (self, categori, driver):
        categori.click()
        subCategoryHolder = driver.find_element_by_class("categoryRefinementsSection")
        subCategoryList = []
        for subCategory in subCategoryHolder:
            subCategoryList.add(subCategory)
        return subCategoryList
    
    def getBestSellers (self, subCategory, driver):
        subCategory.click()
        bestSellerHolder = driver.find_element_by_id("zg_browseRoot")
        web_Listing = Web_Listing
        bestSellers = []
        for bestSeller in bestSellerHolder:
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
            bestSellers.append(web_Listing)        
        
        return bestSellers