#Sherry8.py

#CSC6003OB
#William Sherry
#Assignment 08: Final Project
#Due: 00 MAY 23

import random

#Big boi class - BankManager
class BankManager:

    def __init__(self):
        pass

    class AccountClass:
        def __init__(self):
            self.account_number = random.randint(100000,999999)



bank_manager = BankManager()
account = bank_manager.AccountClass()

print(account.account_number)
