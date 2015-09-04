import sqlite3

def getdb():
    conn = sqlite3.connect('../data/purchasing.db')
    return(conn)

def printdb():
    with open('file.txt.', 'w') as f:
        c = getdb().cursor()
        c.execute('''select * from items where br10qty > 0''')
        towrite = c.fetchall()
        for num, supp, prod, code, name, br, x, y, z, a, b in towrite:
            print(num, supp, prod, code, name, br, x, y, z, a, b)
            f.write(str(num) + supp.rstrip() + prod.rstrip() + code.rstrip() + name.rstrip() + str(br) + str(x) + str(y) + str(z) + str(a) + str(b) + '\n')
            
