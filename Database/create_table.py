import sqlite3


connection = sqlite3.connect("my_db.db")
cursor = connection.cursor()

cursor.execute("create table if not exists students(name text, reg_no long primary key, mobile_no long)")
cursor.execute("insert into students (name, reg_no, mobile_no) values('Madhav', 12213356, 9693744950)")
cursor.execute("insert into students (name, reg_no, mobile_no) values('Krishna', 12213357, 9693744950)")

connection.commit()
print("table has been created and data inside table has been inserted")

cursor.execute("select * from students")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()

