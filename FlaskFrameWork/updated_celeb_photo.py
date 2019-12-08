import sqlite3

conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

sql = "update celebs set photo=replace(photo,'http://www.nphinity.com/pics/','https://s3.amazonaws.com/isat3402019/')"

cursor.execute(sql)

conn.commit()
