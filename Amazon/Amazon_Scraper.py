'''
Created on Feb 10, 2016

@author: niormsby
'''
from selenium import webdriver
from Scraper import Scraper
from Amazon.Scrapers.Best_Seller_Scraper import Best_Seller_Scraper

class Amazon_Scraper(object):
    '''
    classdocs    
    getStoreUrl(storeUrl) checks website passed into it and gets the url from the CONSTANT class
    
    '''    
    global driver 
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def getBestSellers(self):
        best_Seller_Scraper = Best_Seller_Scraper()
        print("Just assigned best_Seller_Scraper = Best_Seller_Scraper.Best_Seller_Scraper")
        driver = webdriver.PhantomJS("/phantomjs-2.1.1-windows/bin/phantomjs.exe")
        print("Just assigned         driver = webdriver.PhantomJS()")

        bestSellers = []
        
        #Navigate to Amazon's best seller list  
        Scraper().navigateToAmazon(driver)
        print("navigated to amazon")
        #Scrape all the Best Seller categories from Amazon and return them as an array
        bestSellerCategories = best_Seller_Scraper.getAmazonBestSellerCategories(driver)  
        print("got best seller categories")
        #Loop through each of the categories and pass them into the getSubCategories method
        for bestSellerCategory in bestSellerCategories:
            bestSellerSubCategories = best_Seller_Scraper.getSubCategories(bestSellerCategory, driver)
            #Loop through each of the subCategories and pass them into the getBestSeller method
            for bestSellerSubCategory in bestSellerSubCategories:
                bestSellers = best_Seller_Scraper.getBestSellers(bestSellerSubCategory, driver) 
        #Return the bestSellers array after it has members added to it
        return bestSellers    
        
    
            
        
