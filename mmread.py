
#Get and open the MINMAX report file
def getFile(f):
    open(f)
    return(f)

#Here is the old code for reference
'''f = open('conn.txt', 'r+')
f.readline()
f.readline()
f.readline()
MMS = f.readline(17)[12:17]
print(line)
print("MMS# ", MMS)
string = str(f.read())
length = len(string)
print('There are', length, 'characters in this file!')
for line in f:
    print(line)
f.close()'''


#Main run sequence

#Get file name and open file
Print('File you wish to update from?')
fname = input(">>>")
f = getFile(fname)


#Read file and print list of suppliers found

#Ask whether to output, display items for a supplier, select new file, or exit
