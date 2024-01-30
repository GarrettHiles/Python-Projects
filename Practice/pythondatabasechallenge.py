import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_roster( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT, \
        col_species TEXT, \
        col_iq INT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_roster(col_name,col_species,col_iq) VALUES (?, ?, ?)", \
                ('Jean-Baptiste Zorg', 'Human', 122))
    cur.execute("INSERT INTO tbl_roster(col_name,col_species,col_iq) VALUES (?, ?, ?)", \
                ('Korben Dallas', 'Human', 100))
    cur.execute("INSERT INTO tbl_roster(col_name,col_species,col_iq) VALUES (?, ?, ?)", \
                ('Ak\'not', 'Mangalore', -5))
    conn.commit()
conn.close()
