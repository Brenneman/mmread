import sqlite3

def squpdate(itemNum, supp, pcode, dcode, desc, br, bqty, br10po, br10qty):
    conn = sqlite3.connect('purchasing.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS items (itemNum INTEGER, supp TEXT, pcode TEXT,
                 dcode TEXT, desc TEXT, br INTEGER, bqty INTEGER, br10PO INTEGER, br10qty INTEGER)''')
    c.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?,?)",
              (itemNum, supp, pcode, dcode, desc, br, bqty, br10po, pr10qty))
    conn.commit()
    conn.close()
    

def getItems(file):
    with open(file) as f:
        f.seek(0)
        suppLine = False
        brLine = False
        itemNum = 0
        supp = ''
        pcode = ''
        dcode = ''
        desc = ''
        br = ''
        bqty = ''
        br10po = ''
        br10qty = ''
        records = 0

        for line in f:
            if suppLine == True:
                itemNum = int(line.lstrip('')[10:17])
                supp = line[:4]
                pcode = line[5:9]
                dcode = line.lstrip('')[18:29]
                desc = line.rstrip('\n')[29:]
                suppLine = False
            elif line[:17].lstrip() == str(itemNum):
                br = int(line[29:31])
                bqty = int(line[64:])
                f.readline()
                line10 = f.readline().rstrip().lstrip()
                br10po = line10[45:50].rstrip().lstrip()
                br10qty = line10[55:].rstrip()
                print(line10, br10po, br10qty)
                #squpdate(itemNum, supp, pcode, dcode, desc, br, bqty)
            elif line[:4] == 'Supp':
                suppLine = True
                records += 1
                print(records, "records have been checked...")
            else:
                pass


getItems(input(">>>"))
input("DONE!")

