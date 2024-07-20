
# importing marshmallow package 
from marshmallow import Schema,fields,validate


# EmployeeSchema class to validate the employee details in database
class EmployeeSchema(Schema):

    id=fields.Int(dump_only=True)

    name=fields.Str(required=True,Validate=validate.Length(min=1))

    department=fields.Str(required=True,Validate=validate.Length(min=1))

    age=fields.Int(required=True,Validate=validate.Length(min=1))
