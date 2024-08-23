class User_Type_Entitie:

  def __init__(self, id=0,name=""):
    self.id = id
    self.name = name
    
  def set_from_dict(self, dict):
    self.id = dict.get("id", 0)
    self.name = dict.get("name", "")