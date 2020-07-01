#Saif Iqbal 1628421

import csv
import os
from datetime import datetime


class Inventory:
    
    inventoryItemsList = []

    def __init__(self):
        
        self.getInput()

        
        self.generateFullInventoryCSV()
        self.generateDamagedInventoryCSV()
        self.generateLaptopInventoryCSV()
        self.generatePastServiceDateInventoryCSV()
        self.generateTowerInventoryCSV()
        self.generatePhoneInventoryCSV()


    def getItem(self, name):
        
        fileName = "Inventory Files CSVs/ValidInventory.csv"
        with open(fileName, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                stringItem = "".join(row)
                itemDetails = stringItem.split(",")
                thisdict = {"id": itemDetails[0],"Manufacturer Name": itemDetails[1],"Item Type": itemDetails[2],"Price": itemDetails[3], "Service Date": itemDetails[4], "Item Status":itemDetails[5] }
                validItemList.append(thisdict)
        matched = []
        itemNamesList =  []
        itemTypeList = []
        for dictt in validItemList:
            itemNamesList.append(dictt.get("Manufacturer Name"))
            itemTypeList.append(dictt.get("Item Type"))
        stringList = name.split()
        manuName = ""
        itemType_ = ""

        for i in range(len(stringList)):
            for j in range(len(itemNamesList)):
                if(stringList[i].lower() == itemNamesList[j].lower()):
                    manuName = itemNamesList[j]
                if(stringList[i] == itemTypeList[j]):
                    itemType_ = itemTypeList[j]
        
        for dictt in validItemList:
            if(dictt.get("Manufacturer Name") == manuName and dictt.get("Item Type") == itemType_):
                matched.append(dictt)
            if(dictt.get("Manufacturer Name") != manuName and dictt.get("Item Type") == itemType_):
                recommend = dictt
        if(len(matched) >0 ):
            sortedItems = sorted(matched, key = lambda i: i['Price'])

            return sortedItems[0], recommend
        
   
    def getInput(self):
        
        fileName = "Input Files CSVs/ManufacturerList.csv"
        with open(fileName, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:                                                                  
                stringItem = "".join(row)
                itemDetails = stringItem.split(",")                                                
                                                                                                    
                thisdict = {"id": itemDetails[0],"Manufacturer Name": itemDetails[1],"Item Type": itemDetails[2],"Price": "", "Service Date": "", "Item Status":itemDetails[3] }
                self.inventoryItemsList.append(thisdict)                                                 


        
        priceList = []
        fileName = "Input Files CSVs/PriceList.csv"
        with open(fileName, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                stringItem = "".join(row)
                itemDetails = stringItem.split(",")
                priceList.append(itemDetails)

        
        for Id, price in priceList:
            for dictionary in self.inventoryItemsList:
                if(Id == dictionary.get("id")):
                    dictionary["Price"] = price

       
        serviceList = []
        fileName = "Input Files CSVs/ServiceDatesList.csv"
        with open(fileName, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                stringItem = "".join(row)
                itemDetails = stringItem.split(",")
                serviceList.append(itemDetails)
        
        for Id, date in serviceList:
            for dictionary in self.inventoryItemsList:
                if(Id == dictionary.get("id")):
                    dictionary["Service Date"] = date

        
        try:
            os.remove("Inventory Files CSVs/FullInventory.csv")
            os.remove("Inventory Files CSVs/DamagedInventory.csv")
            os.remove("Inventory Files CSVs/LaptopInventory.csv")
            os.remove("Inventory Files CSVs/PhoneInventory.csv")
            os.remove("Inventory Files CSVs/PastServiceDateInventory.csv")
            os.remove("Inventory Files CSVs/TowerInventory.csv")
            os.remove("Inventory Files CSVs/ValidInventory.csv")
        except Exception as e:
            pass    
   
    def generateFullInventoryCSV(self):
        
        sortedItems = sorted(self.inventoryItemsList, key = lambda i: i['Manufacturer Name'])
        for dictt in sortedItems:
            with open('Inventory Files CSVs/FullInventory.csv', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(dictt.values())


    def generateDamagedInventoryCSV(self):
        
        sortedItems = sorted(self.inventoryItemsList, key = lambda i: i['Price'],reverse=True)
        for dictt in sortedItems:
            if(dictt.get("Item Status") == "damaged"):
                with open('Inventory Files CSVs/DamagedInventory.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())
          
    def generateLaptopInventoryCSV(self):
        
        sortedItems = sorted(self.inventoryItemsList, key = lambda i: i['id'])
        for dictt in sortedItems:
            if(dictt.get("Item Type") == "laptop"):
                with open('Inventory Files CSVs/LaptopInventory.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())

   
    def generatePastServiceDateInventoryCSV(self):
        
        sortedItems = sorted(self.inventoryItemsList, key = lambda i: i['Service Date'])
        for dictt in sortedItems:
            datetime_object = datetime.strptime(dictt.get("Service Date"), "%m/%d/%Y")              
            now = datetime.today()                                                                  
            if(now > datetime_object):
                with open('Inventory Files CSVs/PastServiceDateInventory.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())  
            if(now < datetime_object and dictt.get("Item Status") == ""):           
                with open('Inventory Files CSVs/ValidInventory.csv', 'a', newline='') as csvfile:            
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values()) 

    
    def generateTowerInventoryCSV(self):
        sortedItems = sorted(self.inventoryItemsList, key = lambda i: i['id'])
        for dictt in sortedItems:
            if(dictt.get("Item Type") == "tower"):
                with open('Inventory Files CSVs/TowerInventory.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())

    
    def generatePhoneInventoryCSV(self):
        sortedItems = sorted(self.inventoryItemsList, key = lambda i: i['id'])
        for dictt in sortedItems:
            if(dictt.get("Item Type") == "phone"):
                with open('Inventory Files CSVs/PhoneInventory.csv', 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(dictt.values())
    

    
Inventory()





