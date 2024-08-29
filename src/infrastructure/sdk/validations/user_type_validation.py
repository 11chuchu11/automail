from marshmallow import Schema, fields
from marshmallow.validate import Length

class User_Type_Validation_Schema(Schema):
  id = fields.Int(required= False)
  name = fields.String(required=True,validate=Length(min=1, error="El campo no puede estar en blanco"))
  