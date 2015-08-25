#This will parse the .txt file and prepare it for writing to csv
#Tristan Brenneman
#St. John's Music
#August 2015


#This opens the file for parsing. Will be removed in later versions.
#Currently for testing purposes
def fopen(fname):
    f = open(fname)
    return(f)

#Finds the line with supplier and item information and adds it to lists for
#later interpretation
def getSupp(f):
    f.seek(0)   #reset to inital file position
    suppLine = False
    supp = []
    prod = []
    itemNum = []
    descCode = []
    desc = []
    

    for line in f:
        if suppLine == True:
            supp.append(line[:4])
            prod.append(line[5:9])
            itemNum.append(line.lstrip('')[10:17])
            descCode.append(line.lstrip('')[18:29])
            desc.append(line.rstrip('\n')[29:])
            suppLine = False
            
        elif line[:4] == 'Supp':
            suppLine = True

        else:
            suppLine == False
            
    return(supp, prod, itemNum, descCode, desc)


#Builds a dictionary for each item that is to be ordered.
#As of yet it doesn't include Branch or BuyQty. This may change.
def buildItemDict(itemNum, supp, prod, descCode, desc, br, bQty):
    itemDict = {}

    while True:
        itemDict[itemNum.pop().lstrip()] = supp.pop(), prod.pop().rstrip(), descCode.pop().rstrip(), desc.pop().rstrip()

        if len(itemNum) == 0:
            break

    for key in itemDict:
        itemDict[key] += br.pop(), bQty.pop()
        

    return(itemDict)

#Uses the list of item numbers to get the Branch and BuyQty for each item.
#Needs to be updated/fixed for items with multiple branch buys required.        
def getBrBqty(itemNums, f):
    f.seek(0)   #reset to initial file position
    br = []
    bqty = []
    itemNum = []
    [itemNum.append(x) for x in itemNums if x not in itemNum]
    i = 0
    
        
    for line in f:
        
        if i == len(itemNum):
            break
        
        inum = itemNum[i]

        if line[:17].lstrip() == inum.lstrip():

            br.append(line[29:31])
            bqty.append(line[63:68].lstrip())
            i += 1

    return(br, bqty)

        
        

#Test code for testing the implementations of the above functions.
#May become a function for the whole file later.
fname = input(">>> File Name: \n")
ifile = fopen(fname)
isupp, iprod, iitemNum, idescCode, idesc = getSupp(ifile)
ibr, ibQty = getBrBqty(iitemNum, ifile)
iitemDict = buildItemDict(iitemNum, isupp, iprod, idescCode, idesc, ibr, ibQty)


#CSV writing testing area.... 
'''import csv
with open('output.csv', 'w') as f:
    fieldnames = ["item#"]	
    w = csv.writer(f)
    for key in iitemDict:
        w.writerow([key])
        w.writerow(iitemDict[key])'''

import sqlite3
conn = sqlite3.connect('purchasing.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS items (number text, supplier text, pcode text, dcode text, desc text, br text, bqty text)''')

c.executemany('INSERT INTO items VALUES (?,?,?,?,?,?,?)', (iitemDict.keys(), iitemDict))
