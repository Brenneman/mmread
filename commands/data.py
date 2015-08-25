# Tristan Brenneman
# St. John's Music
# August 2015

import sqlite3


#open the database
conn = sqlite3.connect('../purchasing.db')
c = conn.cursor()


c.execute('''SELECT * FROM items''')
