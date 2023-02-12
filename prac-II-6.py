import mysql.connector as mcon
mycon=mcon.connect(host='localhost',user='root',password='20060201')#password for school is 123456
cur=mycon.cursor()
cur.execute('use SCHOOL')
q='insert into student (rollno,name,age) values (1,"Amit",22)'
cur.execute(q)
cur.execute('commit')