'''
Created on Feb 10, 2016

@author: niormsby
'''

class Web_Listing(object):
    
    def __init__(self, itemName, description, image, itemPrice, shippingPrice, numberOfProductsAvaliable, 
                 itemSerialNumber, estimatedDeliveryTime, packageSize, packageWeight, returnPolicy):
        self._itemName = itemName
        self._description = description
        self._image = image
        self._itemPrice = itemPrice
        self._shippingPrice = shippingPrice
        self._numberOfProductsAvaliable = numberOfProductsAvaliable
        self._itemSerialNumber = itemSerialNumber
        self._estimatedDeliveryTime = estimatedDeliveryTime
        self._packageSize = packageSize
        self._packageWeight = packageWeight
        self._returnPolicy = returnPolicy
    
    def getImage(self):
        return self._image
    
    def getItemPrice(self):
        return self._itemPrice
        
    def getShippingPrice(self):
        return self._shippingPrice
        
    def getDescription(self):
        return self._description
        
    def getItemName(self):
        return self._itemName
        
    def getItemSerialNumber(self):
        return self._itemSerialNumber
    
    def getEstimatedDeliveryTime(self):
        return self._estimatedDeliveryTime
        
    def getNumberOfProductsAvaliable(self):
        return self._numberOfProductsAvaliable
        
    def getPackageSize(self):
        return self._packageSize
        
    def getPackageWeight(self):
        return self._packageWeight
        
    def getReturnPolicy(self):
        return self._returnPolicy

    def setImage(self, image):
        self._image = image
    
    def setItemPrice(self, itemPrice):
        self._itemPrice = itemPrice
        
    def setShippingPrice(self, shippingPrice):
        self._shippingPrice = shippingPrice
        
    def setDescription(self, description):
        self._description = description
        
    def setItemName(self, itemName):
        self._itemName = itemName
        
    def setItemSerialNumber(self, itemSerialNumber):
        self._itemSerialNumber = itemSerialNumber
    
    def setEstimatedDeliveryTime(self, estimatedDeliveryTime):
        self._estimatedDeliveryTime = estimatedDeliveryTime
        
    def setNumberOfProductsAvaliable(self, numberOfProductsAvaliable):
        self._numberOfProductsAvaliable = numberOfProductsAvaliable
        
    def setPackageSize(self, packageSize):
        self._packageSize = packageSize
        
    def setPackageWeight(self, packageWeight):
        self._packageWeight = packageWeight
        
    def setReturnPolicy(self, returnPolicy):
        self._returnPolicy = returnPolicy
        

    
       
        