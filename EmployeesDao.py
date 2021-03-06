import mysql.connector
import dbconfig as cfg

class EmployeesDao:
    db = " "
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['user'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database']
        )
        #print("connection made")
    
    def create(self,employee):
        cursor = self.db.cursor()
        sql = "insert into employees (ID, name, age, employmentyears, nosecolour) values (%s,%s,%s,%s,%s)"
        values = [
            employee['ID'],
            employee['name'],
            employee['age'],
            employee['employmentyears'],
            employee['nosecolour']

        ]

        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor =self.db.cursor()
        sql = 'select * from employees'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray


    def findById(self, ID):
        cursor =self.db.cursor()
        sql = 'select from employees where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertoDict(result)

    def update(self, employee):
        cursor = self.db.cursor()
        sql = "update employees set name =%s, age = %s, employmentyears = %s, nosecolour = %s where ID  = %s"
        values = [
            
            employee['name'],
            employee['age'],
            employee['employmentyears'],
            employee['nosecolour'],
            employee['ID']
           
        ]
        cursor.execute(sql, values)
        self.db.commit()

        return employee  

    def delete(self, ID):
        cursor =self.db.cursor()
        sql = 'delete from employees where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        return{}

    def convertToDict(self, result):
        colnames = ['ID', 'name', 'age', 'employmentyears', 'nosecolour']
        employee ={}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                employee[colName] = value


        return employee



employeesDao = EmployeesDao()
