from typing import List


class File:
    name:str
    path:str
class Replacement: 
    name: str
    file: File

class Email:
    __id:int
    __user_id:str
    __email: str
    __subject:str
    __body: str
    __replacements: dict
    __files: List[File]
    __templates: List[Replacement]
    
    def __init__(self,id=0, user_id="",email="",subject="", body="",replacements:dict={}, files:List[File]=[], templates:List[Replacement]=[]):
        
        self.__id=id
        self.__user_id=user_id
        self.__email=email
        self.__subject=subject
        self.__body=body
        self.__replacements=replacements
        self.__files=files
        self.__templates=templates
        
    def setFromObj(self,obj):
        self.__id = getattr(obj, "id", 0)
        self.__user_id=getattr(obj, "user_id", "")
        self.__email = getattr(obj, "email", "")
        self.__subject = getattr(obj, "subject", "")
        self.__body = getattr(obj, "body", "")
        self.__replacements = getattr(obj, "replacements", {})
        self.__files = getattr(obj, "files", [])
        self.__templates = getattr(obj, "templates", [])