import os
import datetime


print("Enter the choice: ")
print("1: Create a new Account")
print("2: Enquiry Balance")
print("3: Deposit Balance")
print("4: Withraw Balance")
print("5: Account Delete")

class Log:
    def __init__(self):
        self.showAll = True
        self.currentLevel = 0
        self.errorLevel = 0
        self.infoLevel = 1
        self.warningLevel = 2

    def logWarning(self, providedString):
        if self.currentLevel == self.warningLevel or self.showAll:
            print("[WARNING] " + providedString)
        else:
            pass
    def logError(self, providedString):
        if self.currentLevel == self.errorLevel or self.showAll:
            print("[ERROR] " + providedString)
        else:
            pass
    def logInfo(self, providedString):
        if self.currentLevel == self.infoLevel or self.showAll:
            print("[INFO] " + providedString)
        else:
            pass
    


intInput = int(input("Enter the input: "))
myLog = Log()
if (intInput == 1):
    userId = input("Enter the userId: ")
    while True:
        if os.path.isdir("database/" + userId):
            print("Sorry Choose a different userId this one already exists")
            continue
        else:
            os.mkdir("database/" + userId)
            userPassword = input("Enter the password: ")

            with open("database/" + userId + "/" + "userPassword.txt", "w+") as f_obj:
                f_obj.write(userPassword)
                myLog.logInfo("User Password file created")

            intialBalance = input("Enter the initial amount: ")
            with open("database/" + userId + "/" + "bank.txt", "w+") as f_obj:
                f_obj.write(intialBalance)
                myLog.logInfo("Bank file created")

            with open("database/" + userId + "/" + "transactionUnit.txt", "w+") as f_obj:
                myLog.logInfo("Transaction Unit file created")
                pass
            myLog.logInfo("Account Create Succesfully")
            break
elif (intInput == 2):
    while True:
        userId = input("Enter the userId: ")
        if os.path.isdir("database/" + userId):
            userPassword = input("Enter the userPassword: ")
            with open("database/" + userId + "/" + "userPassword.txt", "r") as f_obj:
                content = f_obj.read()
                if userPassword == content:
                    with open("database/" + userId + "/" + "bank.txt", "r") as f_obj:
                        content = f_obj.read()
                        print("Your bank balance is " + content)
                        break
                else:
                    myLog.logError("Please enter the correct password")
                    continue

        else:
            myLog.logError("Enter the currect userId this one not already exists:")
elif (intInput == 3):
    while True:
        userId = input("Enter the userId: ")
        if os.path.isdir("database/" + userId):
            userPassword = input("Enter the userPassword: ")
            with open("database/" + userId + "/" + "userPassword.txt", "r") as f_obj:
                realPassword = f_obj.read()
                if userPassword == realPassword:
                    providedAmount = int(input("Enter the deposit amount: "))
                    with open("database/" + userId + "/bank.txt", "r") as f_obj:
                        previosBalance = f_obj.read()
                        realPrevios = previosBalance
                    with open("database/" + userId + "/bank.txt", "w") as f_obj:
                        f_obj.write(str(int(realPrevios) + int(providedAmount)))
                        myLog.logInfo("Amount deposited")
                    with open("database/" + userId + "/transactionUnit.txt", "a") as f_obj:
                        f_obj.write("Amount " + str(providedAmount) + " deposited" + "\n")
                else:
                    myLog.logError("Please enter a valid password")
                    continue
        else:
            myLog.logError("Enter a valid user Id")
            continue
elif (intInput == 4):
    while True:
        userId = input("Enter the userId: ")
        if os.path.isdir("database/" + userId):
            userPassword = input("Enter the userPassword: ")
            with open("database/" + userId + "/" + "userPassword.txt", "r") as f_obj:
                realPassword = f_obj.read()
                if userPassword == realPassword:
                    providedAmount = int(input("Enter the withraw amount: "))
                    with open("database/" + userId + "/bank.txt", "r") as f_obj:
                        previosBalance = f_obj.read()
                        realPrevios = previosBalance
                    with open("database/" + userId + "/bank.txt", "w") as f_obj:
                        f_obj.write(str(int(realPrevios) - int(providedAmount)))
                        myLog.logInfo("Withraw Succesful")
                    with open("database/" + userId + "/transactionUnit.txt", "a") as f_obj:
                        f_obj.write("Amount " + str(providedAmount) + " Withraw" + "\n")
                else:
                    myLog.logError("Please enter a valid password")
                    continue
        else:
            myLog.logError("Enter a valid user Id")
            continue
elif (intInput == 5):
    while True:
        userId = input("Enter the userId: ")
        if os.path.isdir("database/" + userId):
            userPassword = input("Enter the userPassword: ")
            with open("database/" + userId + "/" + "userPassword.txt", "r") as f_obj:
                realPassword = f_obj.read()
                if userPassword == realPassword:
                    print("1: Yes, Delete my Account")
                    print("2: No, I want to rethink")
                    isGood = int(input("Enter the confirmation"))
                    if (isGood == 1):
                        os.rmdir("database/" + userId)
                        myLog.logWarning("Your account has been deleted succesfully")
                    elif (isGood == 2):
                        myLog.logInfo("You have aborted your account deletion")
                        break
                else:
                    myLog.logError("Please enter a valid password")
                    continue
        else:
            myLog.logError("Enter a valid user Id")
            continue




