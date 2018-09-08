print("Content-text:text/html\r\n\r\n")
import sqlite3

def create():
	try:
		conn=sqlite3.connect("student.db")
		cursor=conn.cursor()
		sql="create table studentDetails(rollno text,name text,branch text,mobile numeric)"
		cursor.execute(sql)
		conn.commit()
		print("Success")
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
create()
