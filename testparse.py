class SuppItemLine(object):

    fields = (('supp', 5),
              ('prod', 6),
              ('itemNum', 7),
              ('descCode', 11),
              ('desc', 21))

    def __init__(self):
        self.supp = ''
        self.prod = ''
        self.itemNum = ''
        self.descCode = ''
        self.desc = ''

    def __str__(self):
        return ''.join([getattr(self, field_name).ljust(width) 
                        for field_name, width in self.fields])
   

f = SuppItemLine()
f.supp = '1CON'
f.prod = 'ER3K'
f.itemNum = '184050'
f.descCode = 'F30030'
f.desc = 'REED SAX TENOR FIBRA'

g = SuppItemLine()
g.supp = '1CON'
g.prod = 'EM5'
g.itemNum = '67798'
g.descCode = '3511HC'
g.desc = 'MPC TRUMPET BACH'

print(f)
print(g)
