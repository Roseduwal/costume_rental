import datetime

def ReadTextFile():
    costumes = open("costumes.txt", "r")
    data = costumes.readlines()
    costumes.close()
    return data


def StoreDressDetails(FileData):
    
    Dict = {}

    for index in range(len(FileData)):
        
        Dict[index + 1] = FileData[index].replace("\n", "").split(",")
    
    return Dict


def ShowCostumesInTable(Dict):
    
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print()
    print("ID", "\t", "Costume Name", "\t","Brand", "\t\t", "Price", "\t", "Quantity")
    print()
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

    for key, value in Dict.items():
        print()
        print(key, "\t", value[0], "\t", value[1],"\t", value[2], "\t", value[3])

    print()
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    
    return ""




def CostumeID(Dict):
    
   while True:
        print()
        try:
            ID = int(input("Enter the Costume ID: "))

            if ID > 0 and ID <= len(Dict):
                
                quantity = int(Dict[ID][3])

                if quantity == 0:
                        
                    print()
                    print("==============================================================")
                    print("Out of the stock. Please choose other costumes")
                    print("==============================================================")

                    
                else:
                    
                    print()
                    print("==============================================================")
                    print("      The costume is avialable")
                    print("==============================================================")
                    print()
                      
                    return ID
                                            

            else:
                print()
                print("==============================================================")
                print("Please enter the valid Costume ID")
                print("==============================================================")


        except:
            print()
            print("==============================================================")
            print("Please enter the valid Costume ID")
            print("==============================================================")
            

def CostumeQuantity(Dict, ID):
    
    while True:
        
        try:
            print()
            quantity = int(input("Enter the number of costumes you want to rent the costume for: "))

            if quantity > 0 and quantity <= int(Dict[ID][3]):

                Dict[ID][3] = str(int(Dict[ID][3]) - quantity)
                
                print()
                print("Rent Sucesfull")
                print()
                
                return quantity                        

            elif quantity == 0:
                print()
                print("==============================================================")
                print("Please enter the valid quantity")
                print("==============================================================")
            
            else:
                print()
                print("==============================================================")
                print("Quantity provided is greater than what we have in stock!!!")
                print("==============================================================")


        except:
            print()
            print("==============================================================")
            print("Please enter the valid quantity")
            print("==============================================================")
    

def UpdateStock(Dict):
    costumes = open("costumes.txt", "w")
    
    for value in Dict.values():
        data = value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n"
        costumes.write(data)
    costumes.close()


def Rent():
    
    cart = []
    ContinueLoop = True
    
    while ContinueLoop:
        
        ShowCostumesInTable(Dict)
        ID = CostumeID(Dict)
        Quantity = CostumeQuantity(Dict, ID)

        cart.append([ID, Quantity])

        UpdateStock(Dict)

        ShowCostumesInTable(Dict)
        
        
        while True:
            print()
            print()
            RentAgain = input("Do you want to rent any thing else? (Y/N): ")
            print()
            print()
            
            if RentAgain.upper() == "Y":
                
                break
            
            elif RentAgain.upper() == "N":

                ContinueLoop = False
                
                RentBill(cart, Dict)
                
                break

            else:
                print("==========================")
                print("  Enter either Y or N  ")
                print("==========================")
            
            
def RentBill(cart, Dict):
    
    Hour = str(datetime.datetime.now().hour)
    Minute = str(datetime.datetime.now().minute)
    Second = str(datetime.datetime.now().second)

    date = datetime.date.today()
    
    time = str(Hour+":"+Minute+":"+Second)

    time2 = time.replace(":","-")
    
    name = input("Enter your name: ")
    ContactNum = input("Enter your phone number: ")
    
    print()
    print()
    print("============================================")
    print("\t\tYour rent bill")
    print("============================================")
    print()
    print("Name: ", name)
    print("Phone Number: ", ContactNum)
    print("Date of rent: ", date)
    print("Time: ", time)
    print()
    print("=======================================================================================================================")
    print("SN\t\tCostume Name\t\tBrand\t\tQuantity\trate\t\tTotal  ")
    print("=======================================================================================================================")

    
    TotalCost = 0
    
    for i in range(0, len(cart)):
        ID = cart[i][0]
        quantity = cart[i][1]
        total = quantity * float(Dict[ID][2])
        TotalCost += total 
        print(i+1, "\t\t", Dict[ID][0], "\t\t", Dict[ID][1], "\t", quantity,"\t\t", Dict[ID][2],"\t\t", total)

    print()
    print("TotalCost: Rs.", TotalCost)
    print("=======================================================================================================================")

    invoice = open(name + " " + str(date) + " " + time2 + ".txt", "w")
    
    invoice.write("\t\tYour rent bill\n")
    invoice.write("\n\n")
 
    invoice.write("Name: " + name +"\n")
    invoice.write("Phone Number: "+ContactNum+"\n")
    invoice.write("Date of rent: " + str(date) + "\n")
    invoice.write("Time: " + str(time)+"\n")
    invoice.write("Total Cost: " + str(TotalCost)+"\n")
    invoice.write("\n")
    invoice.write("=======================================================================================================================\n")
    invoice.write("SN\t\tCostume Name\t\tBrand\t\tQuantity\trate\t\tTotal  \n")
    invoice.write("=======================================================================================================================\n")
    invoice.write("\n")
    
    for i in range(0, len(cart)):
        ID = cart[i][0]
        quantity = cart[i][1]
        total = quantity * float(Dict[ID][3])
        
        invoice.write(str(i+1) + "\t\t" + Dict[ID][0] + "\t\t" + Dict[ID][1] + "\t\t" + str(quantity) + "\t\t" + Dict[ID][2] + "\t\t" +
                      str(total) + "\n")

    invoice.write("=======================================================================================================================\n")

    invoice.close()



def CostumeIDReturn(Dict):
    
   while True:
        print()
        try:
            ID = int(input("Enter the Costume ID: "))

            if ID > 0 and ID <= len(Dict):
                      
                return ID
                                            

            else:
                print()
                print("==============================================================")
                print("Please enter the valid Costume ID")
                print("==============================================================")


        except:
            print()
            print("==============================================================")
            print("Please enter the valid Costume ID")
            print("==============================================================")

def CostumeQuantityReturn(Dict, ID):
    
    while True:
        
        try:
            print()
            quantity = int(input("Enter the number of costumes you want to return the costume for: "))

            if quantity > 0:

                Dict[ID][3] = str(int(Dict[ID][3]) + quantity)
                
                print()
                print("Return Sucesfull")
                print()
                
                return quantity                        

            else:
                print()
                print("==============================================================")
                print("Please enter the valid quantity")
                print("==============================================================")


        except:
            print()
            print("==============================================================")
            print("Please enter the valid quantity")
            print("==============================================================")

def RentDays():

    while True:
        try:
            days = int(input("Enter the number of days you want to renturn the costume for: "))

            if days > 0:
                
                return days

            else:
                print()
                print("============================================")
                print("Invalid input!!!")
                print("============================================")
                print()

        except:
            print()
            print("============================================")
            print("Invalid input!!!")
            print("============================================")
            print()

def ReturnBill(cart, Dict):
    
    Hour = str(datetime.datetime.now().hour)
    Minute = str(datetime.datetime.now().minute)
    Second = str(datetime.datetime.now().second)

    date = datetime.date.today()
    
    time = str(Hour+":"+Minute+":"+Second)
    time2 = time.replace(":","-")
    
    name = input("Enter your name: ")
    ContactNum = input("Enter your phone number: ")
    days = RentDays()
  
    
    print()
    print()
    print("============================================")
    print("\t\tYour return bill")
    print("============================================")
    print()
    print("Name: ", name)
    print("Phone Number: ", ContactNum)
    print("Date of return: ", date)
    print("Time: ", time)
    print()
    
    print("======================================================================")
    print("SN\t\tCostume Name\t\tBrand\t\tQuantity  ")
    print("======================================================================")
    
    fine = 0
    
    for i in range(0, len(cart)):
        ID = cart[i][0]
        quantity = cart[i][1]

        if days > 5:
            extradays = days - 5
            fine += (quantity * 5 * extradays)
        
        print(i+1, "\t\t", Dict[ID][0], "\t\t", Dict[ID][1], "\t", quantity)

    print()
    print("Total Fine: Rs.", fine)
    print("======================================================================")

    invoice = open(name + " " + str(date) + " " + time2 + ".txt", "w")
    
    invoice.write("\t\tYour return bill\n")
    invoice.write("\n\n")
 
    invoice.write("Name: " + name +"\n")
    invoice.write("Phone Number: "+ContactNum+"\n")
    invoice.write("Date of return: " + str(date) + "\n")
    invoice.write("Time: " + str(time)+"\n")
    invoice.write("Total Fine: " + str(fine)+"\n")
    invoice.write("\n")
    invoice.write("======================================================================\n")
    invoice.write("SN\t\tCostume Name\t\tBrand\t\tQuantity\n")
    invoice.write("======================================================================\n")
    invoice.write("\n")
    
    for i in range(0, len(cart)):
        ID = cart[i][0]
        quantity = cart[i][1]        
        invoice.write(str(i+1) + "\t\t" + Dict[ID][0] + "\t\t" + Dict[ID][1] + "\t\t" + str(quantity) + "\n")

    invoice.write("======================================================================\n")

    invoice.close()
    
def Return():

    cart = []
    ContinueLoop = True
    
    while ContinueLoop:
        
        ShowCostumesInTable(Dict)
        ID = CostumeIDReturn(Dict)
        Quantity = CostumeQuantityReturn(Dict, ID)

        cart.append([ID, Quantity])

        UpdateStock(Dict)

        ShowCostumesInTable(Dict)
        
        
        while True:
            print()
            print()
            ReturnAgain = input("Do you want to return any thing else? (Y/N): ")
            print()
            print()
            
            if ReturnAgain.upper() == "Y":
                
                break
            
            elif ReturnAgain.upper() == "N":

                ContinueLoop = False
                
                ReturnBill(cart, Dict)
                
                break

            else:
                print("==========================")
                print("  Enter either Y or N  ")
                print("==========================")
            
    
FileData = ReadTextFile()
Dict = StoreDressDetails(FileData)


