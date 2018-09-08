import cgi,sqlite3
print("Content-type:text/html \r\n\r\n")

def delete():
	try:
		conn=sqlite3.connect("student.db")
		form=cgi.FieldStorage()
		roll=form.getvalue('delete')
		cursor=conn.cursor()

		sql="delete from studentDetails where rollno='"+roll+"'"
		cursor.execute(sql)
		conn.commit()
		print("<a href='../index.html'><<Back</a>"+"Delete Success")
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
delete()