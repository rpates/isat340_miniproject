import sqlite3

conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()

sql = "create table celebs (celebID inetger PRIMARY KEY, firstname text, lastname text, age integer, email text, photo text, bio text)"

cursor.execute(sql)

conn.commit()

info = "insert into celebs values (?,?,?,?,?,?,?)"
data = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402019/aj.jpg", "Angelina Jolie is an American actress, filmmaker, and humanitarian."),
        (2, "Brad", "Pitt", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402019/bp.jpg", "William Bradley Pitt is an American actor and film producer."),
        (3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402019/sw.jpg", "Princess with hair as black as ebony, lips as red as the rose, skin as white as snow."),
        (4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402019/dv.jpg", "Darth Vader is a fictional character in the Star Wars franchise."),
        (5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402019/ts.jpg", "Taylor Alison Swift is an American singer and songwriter."),
        (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402019/bk.jpg", "Beyoncé Giselle Knowles-Carter is an American singer, songwriter, and actress."),
        (7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402019/sg.jpg", "Selena Marie Gomez is an American singer, songwriter, actress, and television producer."),
        (8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402019/sc.jpg", "Stephen Curry is a professional American basketball player with the Golden State Warriors."))

cursor.executemany(info, data)
conn.commit()

check = "SELECT * FROM celebs"
cursor.execute(check)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
