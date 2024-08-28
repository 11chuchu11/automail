from marshmallow import Schema, fields

class User_Type_Validation_Schema(Schema):
  id = fields.Int(required= False)
  name = fields.String(required=True,validate= lambda e : e != "")
  