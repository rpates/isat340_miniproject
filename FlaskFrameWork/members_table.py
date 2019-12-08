import sqlite3

conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

sql = "create table members (memberID integer PRIMARY KEY, firstname text, lastname text, age integer, email text, bio text)"

cursor.execute(sql)

conn.commit()

info = "insert into members values (?,?,?,?,?,?)"
data = ((1, "Riley", "Pates", 22, "patesrc@dukes.jmu.edu", "I was born in Royal Oaks, MI and rasied in Virginia."),
        (2, "Lilly", "Riggleman", 22, "rigglelb@dukes.jmu.edu", "I was born in Charlottesvilla, VA. My mother is a distiller and my father is a Congressman. I have two older sisters, and all of us like to play basketball."))

cursor.executemany(info, data)
conn.commit()

check = "SELECT * FROM members"
cursor.execute(check)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
