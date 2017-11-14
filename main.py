import sqlite3

conn = sqlite3.connect('network.db')

c = conn.cursor()

c.execute("SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'addresses'")
exists = c.fetchone()
if exists[0] == 0:
    c.execute('''CREATE TABLE addresses
                 (ip text, mask text)''')
    print('Made Table')

while 1:
    ip = input("Please input IP address: ")
    if ip == "":
        break
    mask = input("Please input net mask: ")
    entry = (ip, mask)

    c.execute('INSERT INTO addresses VALUES (?,?)', entry)

conn.commit()

# for row in c.execute('SELECT * FROM addresses'):
#    print(row)
