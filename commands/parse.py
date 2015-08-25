import sqlite3

def squpdate(itemNum, supp, pcode, dcode, desc, br, bqty):
    conn = sqlite3.connect('purchasing.db')
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS items (itemNum INTEGER, supp TEXT, pcode TEXT, dcode TEXT, desc TEXT, br INTEGER, bqty INTEGER)")
    c.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?)",
              (itemNum, supp, pcode, dcode, desc, br, bqty))
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
                squpdate(itemNum, supp, pcode, dcode, desc, br, bqty)
            elif line[:4] == 'Supp':
                suppLine = True
                records += 1
                print(records, "records have been checked...")
            else:
                pass


#getItems(input(">>>"))
