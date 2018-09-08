import cgi,cgitb,sqlite3
print("Content-type:text/html\r\n\r\n")
conn=sqlite3.connect("student.db")
cursor=conn.cursor()
try:
	form=cgi.FieldStorage()
	rolls=form.getvalue("edit")
	roll=rolls
	#print("Rollno :<b>"+rolls+"</b>")

	sql="select * from studentDetails where rollno='"+roll+"'"
	cursor.execute(sql)
	for row in cursor.fetchall():
		data="""
			<link rel="stylesheet" href="../bootstrap/css/bootstrap.min.css">
			<link rel="stylesheet" href="../bootstrap/css/bootstrap-theme.min.css">
			<script src="../scripts/jquery-3.3.1.min.js"></script>
			<script src="../bootstrap/js/bootstrap.min.js"></script>

			<form action='./update.py' method='post' class='col-sm-6'>
				<label>Rollno:</label><input type='text' class='form-control' name='rollno' value='%s' readonly="readonly"><br>
				<label>Name:</label><input type='text' class='form-control' name='name' value='%s'><br>
				<label>Branch:</label><select name='branch' class='form-control' value='%s'>
							<option>CSE</option>
							<option>IT</option>
							<option>ECE</option>
							<option>MECH</option>
							<option>EEE</option>
							<option>CIVIL</option>
				       </select><br>
				<label>Mobile:</label><input type='text' class='form-control' name='mobile' value='%s'><br>
				<input type='submit' class='btn btn-warning pull-right' value='Update'>
			</form>
		"""%(row[0],row[1],row[2],row[3])
		print(data)
	cursor.close()
	conn.close()
except Exception as e:
	print(e)
