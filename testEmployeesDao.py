from EmployeesDao import employeesDao

employee1 = {
    'ID':1,
    'name': 'Daser',
    'age' : 80,
    'employmentyears':70,
    'nosecolour': 'Black'



}
employee2 = {
    'ID':2,
    'name': 'Prancer',
    'age' : 7,
    'employmentyears':6,
    'nosecolour': 'Black'



}
employee3 = {
    'ID':3,
    'name': 'Vixen',
    'age' : 6,
    'employmentyears':5,
    'nosecolour': 'Black'



}
employee4 = {
    'ID':4,
    'name': 'Rudolph',
    'age' : 2,
    'employmentyears':1,
    'nosecolour': 'Red'



}
#returnvalue = employeesDao.create(employee)
#print(returnValue)
returnValue =  employeesDao.getAll()
print(returnValue)

returnValue =  employeesDao.update(employee1)
print(returnValue)

returnValue =  employeesDao.update(employee3)
#print(returnValue)
returnValue =  employeesDao.update(employee4)
print(returnValue)
#returnValue =  employeesDao.findById(employee3['ID'])
#print(returnValue)

print('This is a Get all') # coming in as tuple
returnValue =  employeesDao.getAll()
print(returnValue)
returnValue =  employeesDao.delete(employee3['ID'])
print(returnValue)
returnValue =  employeesDao.getAll()
print(returnValue)


