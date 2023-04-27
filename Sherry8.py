#Sherry8.py

#CSC6003OB
#William Sherry
#Assignment 08: Final Project
#Due: 00 MAY 23


#Big boi class - BankManager
class BankManager:

    def __init__(self, account, password):

        self.account = account
        self.password = password
    

    def display(self,):

        print(self.account)
        print(self.password)


#childclass of BankManager - AccountClass

class AccountClass(BankManager):
    def randomAccNumber(self):
        




def main():

    account = 12345
    password = "password"

    bank_Manager = BankManager(account,password)

    bank_Manager.display()

    #prompt user for input __ if '11' entered, quit program
    while True:
        

if __name__ == "__main__":
    main()