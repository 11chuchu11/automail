from typing import List


class File:
    name:str
    path:str
class Replacement: 
    name: str
    file: File

class Email:
    _id:int
    _user_id:str
    _email: str
    _subject:str
    _body: str
    _replacements: dict
    _files: List[File]
    _templates: List[Replacement]
    
    def __init__(self,id=0, user_id="",email="",subject="", body="",replacements:dict={}, files:List[File]=[], templates:List[Replacement]=[]):
        
        self._id=id
        self._user_id=user_id
        self._email=email
        self._subject=subject
        self._body=body
        self._replacements=replacements
        self._files=files
        self._templates=templates
        
    def setFromObj(self,obj):
        self._id = getattr(obj, "id", 0)
        self._user_id=getattr(obj, "user_id", "")
        self._email = getattr(obj, "email", "")
        self._subject = getattr(obj, "subject", "")
        self._body = getattr(obj, "body", "")
        self._replacements = getattr(obj, "replacements", {})
        self._files = getattr(obj, "files", [])
        self._templates = getattr(obj, "templates", [])