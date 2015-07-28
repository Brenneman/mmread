f = open('conn.txt', 'r+')
f.readline()
f.readline()
f.readline()
MMS = f.readline(17)[12:17]
print("MMS# ", MMS)
string = str(f.read())
length = len(string)
print('There are', length, 'characters in this file!')
f.close()


