import sqlite3
import tkinter

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
                l.configure(text="Done!")
            else:
                pass

def clearDB(check):
    
    conn = sqlite3.connect('purchasing.db')
    c = conn.cursor()

    c.execute("DELETE FROM items")

    conn.commit()
    conn.close()
    check.destroy()

def clearCheck():
    check = tkinter.Tk()
    check.title("Clear DataBase?")
    l = tkinter.Label(check, text="Really clear DataBase?")
    l.pack()
    byes = tkinter.Button(check, text="Yes", command= lambda: clearDB(check))
    byes.pack(side="left", padx=50)
    bno = tkinter.Button(check, text="No", command= lambda: check.destroy())
    bno.pack(side="right", padx=50)
    
#Minimalist GUI
if __name__ == '__main__':
    master = tkinter.Tk()
    master.title("SJM MINMAX Parser")
#    master.geometry("300x300")
    e = tkinter.Entry(master)
    e.pack(pady=12)
    b = tkinter.Button(master, text="Go!", command= lambda: getItems(e.get()))
    b.pack(pady=12, padx=150)
    l = tkinter.Label(master, text="")
    b2 = tkinter.Button(master, text="Clear DataBase", command= lambda: clearCheck())
    b2.pack(pady=12)
    master.mainloop()
