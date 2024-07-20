

# importing all necessary classes of flask
from flask import Blueprint,request,jsonify,abort

# importing EmployeeSchema class from Schemas file
from .schemas import EmployeeSchema

# importing db variable/object and Employee class from models file
from .models import Employee,db

# creating a blueprint route
main=Blueprint('main',__name__)

employee_schema=EmployeeSchema() #creating an object for EmployeeSchema file 


# an entry message
@main.route('/',methods=['GET'])
def index():
    return ({"message":"Welcome to the Employee Management System !"})


#create an employee to add to database
@main.route('/employees',methods=['POST']) #decorater line

def create_Employee():

    data=request.get_json() # requesting data from json

    errors=employee_schema.validate(data) #validating the data

    if errors: # checking the error
        return jsonify(errors),400
    
    new_Employee=Employee(name=data['name'], department=data['department'], age=data['age']) # giving the input

    db.session.add(new_Employee) # adding to database

    db.session.commit() # commit message
    
    return ({'message':'employee added successfully'}),201 # output to url



# reading an employee data stored in database
@main.route('/employees',methods=['GET']) #decorater line

def get_all_Employee():

    employee=Employee.query.all() # enquiring for data

    return jsonify({"employee":[emp.to_dict()for emp in employee]}) #returning whole data



# reading an employee from database by ID
@main.route('/employees/<int:id>',methods=['GET']) #decorater line

def get_Employee(id):

    employee=Employee.query.all()

    if not employee:
        abort(404, description= f"Employee with id {id} not found!")

    return ([{
        'id':employee.id,
        'department':employee.department,
        'age':employee.age,
        'name':employee.name
        } for employee in employee if employee.id==id]) #returning the employee detail of given id


                   

# updating details of existing employee
@main.route('/employees/<int:id>',methods=['PUT']) #decorater line

def update_Employee(id):

    data=request.get_json()

    errors=employee_schema.validate(data) # validating data

    if errors: # checking for error
        return jsonify(errors),400
    
    employee= Employee.query.get_or_404(id) # enquiring employee id

        
    employee.name=data['name'] #updated name
    employee.department=data['department'] #updated department
    employee.age=data['age'] #updated age

    db.session.commit() # commiting the change to database

    return ([{
        'id':employee.id,
        'department':employee.department,
        'age':employee.age,
        'name':employee.name
        } ]) # output message for webpage
    
    


# route for deleting an employee
@main.route('/employees/<int:id>',methods=['DELETE']) #decorater line
def delete_Employee(id):

    employee=Employee.query.get_or_404(id) #enquiring employee detail

    if not employee:
       return ({'error':'employee not found'}),404
    
    db.session.delete(employee) # deleting the employee detail of given id

    db.session.commit() # commit the change to database

    return jsonify({'message':'employee deleted successfully'}) # output message for url

