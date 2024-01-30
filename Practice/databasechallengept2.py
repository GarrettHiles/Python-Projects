import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_name,col_iq FROM tbl_roster WHERE col_species = 'Human'")
    varPerson = cur.fetchall()
    for i in varPerson:
        msg = "Name: {} IQ: {}".format(i[0],i[1])
        print(msg)
