import sqlite3
print("Content-type:text/html \r\n\r\n")

def retrive():
	try:
		table="""
			<script>
				$(document).ready(function(){
				    $('[data-toggle="tooltip"]').tooltip();   
				});
			</script>
		
			<table border='2' class="table table-bordered">
				<tr class="bg-primary">
					<th>Roll Number</th>
					<th>Name</th>
					<th>Branch</th>
					<th>Mobile</th>
					<th colspan='2'>Operations</th>
				</tr>
		"""
		print(table)
		conn=sqlite3.connect("student.db")
		cursor=conn.cursor()
		sql="select * from studentDetails"
		cursor.execute(sql)
		for row in cursor.fetchall():
			print("<tr>")
			print("<td>"+row[0]+"</td>")
			print("<td>"+row[1]+"</td>")
			print("<td>"+row[2]+"</td>")
			print("<td>",row[3],"</td>")
			print("<td><form action='./cgi-bin/edit.py' method='post'><button name='edit' data-toggle='tooltip' data-placement='right' title='edit "+row[0]+"' value="+row[0]+" class='glyphicon glyphicon-edit btn btn-info btn-xs'></button></td></form>")
			print("<td><form action='./cgi-bin/delete.py' method='post'><button name='delete' data-toggle='tooltip' data-placement='right' title='delete "+row[0]+"' value="+row[0]+" class='glyphicon glyphicon-remove btn btn-danger btn-xs'></button></td></form>")
			print("</tr>")
		print("</table>")
		print(scripts)
		scripts="""
		  <!-- Modal -->
		  <div class="modal fade" id="myModal" role="dialog">
		    <div class="modal-dialog modal-sm">
		      <div class="modal-content">
		        <div class="modal-header">
		          <button type="button" class="close" data-dismiss="modal">&times;</button>
		          <h4 class="modal-title">Are You Sure to Delete Record ..!</h4>
		        </div>
		        <div class="row modal-body">
		          <div col-6><button class='btn btn-sm btn-danger'>Delete</button></div>
		          <div col-6><button class='btn btn-sm btn-info close' data-dismiss="modal" >Cancel</button></div>
		        </div>
		      </div>
		    </div>
		  </div>
		  $(document).ready(function(){
			$('#records tr:nth-of-type(n+2)').click(function(){
				var tds=$(this).children();
				$("#id").val(tds.eq(1).text());
			})
		})


		"""


	except Exception as e:
		print(e)
# <input type='hidden' name='edits' value="+row[0]+"><button type='submit'>Edit</button>
# print("<td><a href='edit?rollno="+row[0]+"'><button name='edit' value="+row[0]+">Edit</button></a></td>")
retrive()