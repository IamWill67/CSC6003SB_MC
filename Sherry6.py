"""
Sherry6.py
William Sherry
CSC6003OB
Professor: GK
Assignment: 06 Dequeue
Due: 25 April 2023
"""


"""
This is a double-ended queue data structure

Attributes:
items (list): The items in the deque.

Methods:

__init__(): Initializes a new deque with an empty list.
add_front(items): Adds items to the front of the deque.
add_rear(items): Adds items to the rear of the deque.
"""
class Deque:
    def __init__(self):
        self.items = []

    #adding to the front of the line
    def add_front(self, items):
        self.items.insert(0, items)

    #adding to the rear of the line
    def add_rear(self,items):
        self.items.append(items)

    #removing from the front of the line
    def remove_front(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    #removing from the rear of the line
    def remove_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    #Check if line is empty
    def is_empty(self):
        return len(self.items)==0
    
    #Check the size of the line
    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)


#Testing with a new class - constructor method  
my_deque = Deque()


item1 = int(input("Please provide int 'a': "))
item2 = int(input("Please provide int 'b': "))
item3 = int(input("Please provide int 'c': "))
item4 = int(input("Please provide int 'd': "))

itemList = [item1, item2, item3, item4]

for number in itemList:
    frontOrBack = str(input("Would you like to add to the front or back? [f/b"))
    if frontOrBack == 'f':
        var_name = "item{}".format(number)
        value = globals()[var_name]
        my_deque.add_front(value)
    else:
        var_name = "item{}".format(number)
        value = globals()[var_name]
        my_deque.add_rear(value)




my_deque.display()