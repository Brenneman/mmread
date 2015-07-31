#This will parse the .txt file and prepare it for writing to csv
'''
def fopen(fname):
    f = open(fname)
    print("Opened " + fname)
    return(f)

def getSupp(f):
    f.seek(0)
    suppLine = False
    supp = []

    for line in f:
        if suppLine == True:
            supp.append(line[:4])
            suppLine = False

        elif line[:4] == 'Supp':
            suppLine = True

        else:
            suppLine == False
            
    return(supp)

def getItemNum(f, supp):
    f.seek(0)
    itemNum = []
    i = 0

    for line in f:

        if i == len(supp):
            return(itemNum)
            break

        elif line[:4] == supp[i]:
            itemNum.append(line[9:17])
            i += 1

        else:
            pass

def getItemCode(f)
    f.seek(0)
    itemCode = []

    for line in f:
        

##testcode

fname = input("File name:\n>>>")
ifile = fopen(fname)
isupp = getSupp(ifile)
iitemNum = getItemNum(ifile, isupp)
#iitemCode = getItemCode(ifile, i'''
    
import struct

fieldwidths = (2, 10, 24)  # negative widths represent ignored padding fields
fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's')
                        for fw in fieldwidths)
fieldstruct = struct.Struct(fmtstring)
parse = fieldstruct.unpack_from
print('fmtstring: {!r}, recsize: {} chars'.format(fmtstring, fieldstruct.size))

line = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\n'
fields = parse(line)
print('fields: {}'.format(fields))



