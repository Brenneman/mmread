import sqlite3
import sys

def squpdate(itemNum, supp, pcode, dcode, desc, br, oe, rsrv, bqty, br10po, br10qty):
    conn = sqlite3.connect('../data/purchasing.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS items (itemNum INTEGER, supp TEXT,
                 pcode TEXT,dcode TEXT, desc TEXT, br INTEGER, oe INTEGER, 
                 rsrv INTEGER, bqty INTEGER, br10PO INTEGER, br10qty INTEGER)''')
    c.execute("INSERT INTO items VALUES (?,?,?,?,?,?,?,?,?,?,?)",
              (itemNum, supp, pcode, dcode, desc, br, oe, rsrv, bqty, br10po, br10qty))
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
        oe = ''
        rsrv = ''
        bqty = ''
        br10po = ''
        br10qty = ''
        records = 0
        count = 0

        for line in f:
            count += line.count('')
            print(count)
            if suppLine == True:
                itemNum = int(line.lstrip('')[10:17])
                supp = line[:4]
                pcode = line[5:9]
                dcode = line.lstrip('')[18:29]
                desc = line.rstrip('\n')[29:]
                suppLine = False
            elif line[:17].lstrip() == str(itemNum):
                br = int(line[29:31])
                oe = int(line[45:51])
                rsrv = int(line[62:67])
                bqty = int(line[67:].rstrip())
                print(line)
                line10 = f.readline()
                while line10[:19].lstrip() != str(itemNum):
                    line10 = f.readline()
                print(line)
                f.seek(count)
                line10 = line10.rstrip('\n')
                br10po = line10[46:52].rstrip(' ').lstrip(' ')
                br10qty = line10[55:].rstrip(' ').lstrip(' ')
                br10po = int(br10po)
                br10qty = int(br10qty)
                squpdate(itemNum, supp, pcode, dcode, desc, br, oe, rsrv, bqty, br10po, br10qty)
            elif line[:4] == 'Supp':
                suppLine = True
                records += 1
                print(records, "records have been checked...")
            else:
                pass


if __name__ == "__main__":

    getItems(input(">>>"))
    input("DONE!")
    sys.exit()

