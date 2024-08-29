class User:
    _email:str
    _password:str
    _name:str
    _surname:str
    _username:str
    _google_id:str
    _microsoft_id:str
    
    
    def __init__(self,email="", password="", name="", surname="", username="", google_id="", microsoft_id=""):
        self._email=email
        self._password=password
        self._name=name
        self._surname=surname
        self._username=username
        self._google_id=google_id
        self._microsoft_id = microsoft_id
        
        
    def setFromObj(self,obj):
        self._email=getattr(obj, "email", "")
        self._password=getattr(obj, "password", "")
        self._password=getattr(obj, "name", "")
        self._password=getattr(obj, "surname", "")
        self._password=getattr(obj, "username", "")
        self._password=getattr(obj, "google_id", "")
        self._password=getattr(obj, "microsoft_id", "")