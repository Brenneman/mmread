#Tristan Brenneman
#St John's Music
#August 2015

#imports
from commands import *
import sqlite3


#Main Functions
def Welcome():
    with open('welcome.txt') as f:
        for line in f:
            print(line)

#Main run sequence
Welcome()
#Choose from below
choice = ""
while choice != 'quit' or 'q':
    choice = input(">>>").lower()
    if choice == 'h' or choice == 'help':
        hlp()
    elif choice == 'u' or choice == 'update':
        parse.getItems(input("File Name?\n>>>"))
    else:
        pass
        

#Update database from a file?


#Select and view by Supplier or Department?

#Which purchases have you made?
#             OR 
#Which items/suppliers/departments would you like to clear?
#Need to decide which works better/Performs task wanted/Decide on task



