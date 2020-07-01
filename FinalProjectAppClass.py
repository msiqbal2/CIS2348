#Saif Iqbal 1628421

from FinalProjectInventoryClass import Inventory
import csv
class App:
    def __init__(self):
        self.main_menu()

    def main_menu(self):
        print("Select an option from the following menu: ")
        print("------------------------------------------")
        print("1: Query the User\n"
              "2: Show Processed Inventory Reports\n"
              "3: Quit")

        try:
            option = int(input("Enter your choice: "))
            if(option > 0 and option < 9):
                if(option == 3):
                    exit(1)
                if(option == 2):
                    self.showInventoryMenu()

                if(option == 1):
                    self.showMenu()
                
            else:
                print("Enter a valid option\n")
            self.main_menu()
        except Exception as e:
            print(e)
            print("Enter a valid option\n")
            self.main_menu()
    def showInventoryMenu(self):
        print("Select an option from the following menu: ")
        print("------------------------------------------")
        print(
            "1: Show full inventory\n2: Show damaged inventory\n3: Show Past Service Date Inventory\n4: Show Laptop Inventory\n5: Show Phone Inventory\n6: Show tower inventory")
        print("7: Back\n8: Quit")
        try:
            option = int(input("Enter your choice: "))
            if (option > 0 and option < 9):
                if (option == 8):
                    exit(1)
                if (option == 7):
                    self.main_menu()
                if (option == 6):
                    self.print_specified_inventory("Tower")
                if (option == 5):
                    self.print_specified_inventory("Phone")
                if (option == 4):
                    self.print_specified_inventory("Laptop")
                if (option == 3):
                    self.print_specified_inventory("Service")
                if (option == 2):
                    self.print_specified_inventory("Damage")
                if (option == 1):
                    self.print_specified_inventory("Full")

            else:
                print("Enter a valid option\n")
            self.showInventoryMenu()
        except Exception as e:
            print(e)
            print("Enter a valid option\n")
            self.main_menu()
    
    def showMenu(self):
        manufacturerName = input("Please enter manufacture name and item type: ")

        result = Inventory.getItem("",manufacturerName)
        if(result != None):
            self.show_specific_items(result)
        else:
            print("Item not found! ")

        option = input("Press m for main menu, y to continue and q to exit: ")
        if(option == "q" or option == "Q"):
            exit(1)
        if(option == "y" or option == "Y"):
            self.showMenu()
        if(option == "m" or option == "M"):
            self.main_menu()
        
    
    def print_specified_inventory(self, itemType):
        fileName = ""
        if(itemType == "Full"):
            fileName = 'FullInventory.csv'
        if(itemType == "Laptop"):
            fileName = 'LaptopInventory.csv'
        if(itemType == "Tower"):
            fileName = 'TowerInventory.csv'
        if(itemType == "Phone"):
            fileName = 'PhoneInventory.csv'
        if(itemType == "Damage"):
            fileName = 'DamagedInventory.csv'
        if(itemType == "Service"):
            fileName = 'PastServiceDateInventory.csv'
        listt = []
       
        filePath = "Inventory Files CSVs/"+fileName
        with open(filePath, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                listt.append(row)
        print("%-12s %-14s %-13s %-10s %-15s %-10s" % ("ID","Name","Item Type","Price","Service Date","Condition"))
        print("--------------------------------------------------------------------------------")

        for item in listt:
            stringItem = "".join(item)
            itemDetails = stringItem.split(",")
            print("%-12s %-14s %-13s %-10s %-15s %-10s" % (itemDetails[0],itemDetails[1],itemDetails[2],itemDetails[3],itemDetails[4],itemDetails[5]))
    
    def show_specific_items(self, items):
        print("Your item is: \n")
        print("%-12s %-14s %-13s %-10s" % ("ID","Name","Item Type","Price"))
        print("---------------------------------------------------")
        itemDetails = items[0].values()
        itemDetails = list(itemDetails)
        print("%-12s %-14s %-13s %-10s" % (itemDetails[0],itemDetails[1],itemDetails[2],itemDetails[3]))

        print("\nYou may, also, consider:\n" )
        print("%-12s %-14s %-13s %-10s" % ("ID","Name","Item Type","Price"))
        print("---------------------------------------------------")
        itemDetails = items[1].values()
        itemDetails = list(itemDetails)
        print("%-12s %-14s %-13s %-10s" % (itemDetails[0],itemDetails[1],itemDetails[2],itemDetails[3]))
        print()
if __name__ == "__main__":
    App()
