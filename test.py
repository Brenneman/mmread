f = open('conn.txt')

supp = []
suppLine = False
for line in f:
    if suppLine == True:
        supp.append(line)
        suppLine = False
    elif line[0:3] == 'Supp':
        suppLine = True
    else:
        suppLine = False
print(supp)
f.seek(0)
print(f.readline())
