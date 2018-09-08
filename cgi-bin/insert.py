import cgi,sqlite3
print("Content-type:text/html \r\n\r\n")

def insert():
	try:
		form=cgi.FieldStorage()
		
		rollno=form.getvalue("rollno")
		name=form.getvalue("name")
		branch=form.getvalue("branch")
		mobile=form.getvalue("mobile")

		conn=sqlite3.connect("student.db")
		cursor=conn.cursor()
		sql="insert into studentDetails values(?,?,?,?)"
		cursor.execute(sql,(rollno,name,branch,mobile))
		conn.commit()
		print("<a href='../index.html'><<Back</a> Success")
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
insert()