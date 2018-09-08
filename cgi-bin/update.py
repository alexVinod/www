import cgi,sqlite3
print("Content-type:text/html \r\n\r\n")

def update():
	try:
		conn=sqlite3.connect("student.db")
		cursor=conn.cursor()
		
		form=cgi.FieldStorage()
		rollno=form.getvalue('rollno')
		name=form.getvalue('name')
		branch=form.getvalue('branch')
		mobile=form.getvalue('mobile')

		sql="update studentDetails set name=?,branch=?,mobile=? where rollno='"+rollno+"'"
		cursor.execute(sql,(name,branch,mobile))
		conn.commit()
		print("<a href='../index.html'><<Back</a>"+"Success")
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
update()