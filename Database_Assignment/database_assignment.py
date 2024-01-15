
import sqlite3


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignment( ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fName TEXT)")
    conn.commit()
 
conn = sqlite3.connect('test.db')


#tuple of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


#a loop through each object to find the files that end with .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # has to have a trailing comma so that we can add multiple objects
            # from the tuple, the loop looks for files ending with .txt from the tuple
            cur.execute("INSERT INTO tbl_assignment (col_fname) VALUES (?)", (x,))
            print(x)


conn.close()
