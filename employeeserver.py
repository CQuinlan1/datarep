from flask import Flask, url_for, request ,redirect, abort, jsonify
from EmployeesDao import employeesDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
    #get all

@app.route('/employees')
def getAll():
    return jsonify(employeesDao.getAll())
    # find by id 


@app.route('/employees/<int:ID>')
def findById(Id):
    return jsonify(employeesDao.findById(ID))


# create 
# curl -X POST  -d "{\"name\":\"new name\", \"age\:\new age\",\"employmentyears"\ ....

@app.route('/employees', methods=['POST'])
def create():

    if not request.json:
        abort(400)

    employee = {
       
        "ID": request.json["ID"],
        "name": request.json["name"],
        "age": request.json["age"],
        "employmentyears": request.json["employmentyears"],
        "nosecolours": request.json["nosecolours"]
    }

    return jsonify(employeesDao.create(employee))

    return "served by Create "

# update
# curl -X PUT -d "{\"


@app.route('/employees/<int:ID>', methods=['PUT'])
def update(ID):
    foundEmployee=employeesDao.findById(ID)
    print (foundEmployee)
    if foundEmployee == {}:
        return jsonify(()), 404
    currentEmployee = foundEmployee
    if 'name' in request.json:
        currentEmployee['name'] = request.json['name']
    if 'age' in request.json:
        currentEmployee['age'] = request.json['age']
    if 'employmentyears' in request.json:
        currentEmployee['employmentyears'] = request.json['employmentyears']
    if 'nosecolour' in request.json:
        currentEmployee['nosecolour'] = request.json['nosecolour']
    employeesDao.update(currentEmployee)

    return jsonify(currentEmployee)

#@app.route('/employees/<int:ID>',methods=['PUT'])

#delete
# curl -X DELETE

 
@app.route('/employees/<int:ID>',methods=['DELETE'])
def delete(ID):
    employeesDao.delete(ID)

    return jsonify({"done": True})


if __name__== "_main_":

    app.run(debug=True)




