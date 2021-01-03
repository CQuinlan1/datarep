import mysql.connector

db = mysql.connector.connect
{
    host= "DESKTOP-HBPVVO3",
    user= "",
    password= " ",
    database= "employees "
}
cursor = db.cursor()
sql="select * from employees"
cursor.execute(sql)
result = cursor.fetchall()
    for x in result:
        print(x)

