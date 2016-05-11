'''
Created on Feb 15, 2016

@author: niormsby
'''

class MyClass(object):
    '''
    classdocs
    '''
    
    import array
    
    def __init__(self, params):
        '''
        Constructor
        '''
        
    def getAmazonStoreCategories(self):
        categoryButton = driver.find_element_by_id("nav-link-shopall")
        categoryButton.click()
        categoryList[] = null
        categoryTable = driver.find_element_by_id("shopAllLinks")
        for categori in categoryTable:
            categoryList.add(categori)
        return categoryTable
    
    def getTop100Products(self, subCategory):
        subCategory.click()
        
        '''
        get all the products from the webpage and add them to a list. 
        click the product and scrape all the product details. 
    
        '''                
            
    def getSubCategories (self, categori):
        categori.click()
        subCategoryHolder = driver.find_element_by_class("categoryRefinementsSection")
        subCategoryList[] = null
        for subCategory in subCategoryHolder:
            subCategoryList.add(subCategory)
        return subCategoryList