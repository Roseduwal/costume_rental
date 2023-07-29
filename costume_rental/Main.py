import Operations
def Messages():
    """
    Here, the options i.e. features provided by software is displayed and user enters the options to do tasks repectively
    like rent or return the costumes
    """

    while True:
        print()
        print("Select a desirable Option: \n\n(1)  1 to rent a costume\n(2)  2 to return a costume\n(3)  3 to exit.\n")
        print()

        print()
        user = input("Enter a option: ")
        print()

        if(user == "1"):            
            Operations.Rent()

        elif(user == "2"):
            Operations.Return()
            

        elif (user == "3"):
            print()
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
            print("Thank you for using our application. see you!")
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
            print()

            exit()
            break

        else:
            print()
            print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            print("Invalid Input!!!")
            print("!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!-!")
            print()






print()
print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
print()
print("Welcome to the Custome rental application")
print()
print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")



Messages()





