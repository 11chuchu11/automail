class User:
    __email:str
    __password:str
    
    def __init__(self,email="", password=""):
        self.__email=email
        self.__password=password
        
    def setFromObj(self,obj):
        self.__email=getattr(obj, "email", "")
        self.__password=getattr(obj, "password", "")