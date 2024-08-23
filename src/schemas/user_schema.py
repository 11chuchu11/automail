from datetime import datetime
from sqlalchemy import Column, String, UUID,Integer,DateTime, ForeignKey
from src.schemas.base import Base

class User(Base):
  __tablename__ = "users"
  
  id = Column(UUID, primary_key=True)
  username = Column(String, nullable=False)
  password = Column(String, nullable=False)
  name = Column(String, nullable=False)
  last_name = Column(String, nullable=True)
  user_type = Column(String, ForeignKey("user_types.id"), nullable=False,)
  is_active = Column(Integer, nullable=False)
  created = Column(DateTime, nullable=False, default=datetime.now())
  modified = Column(DateTime, nullable=True)
  last_login = Column(DateTime, nullable=True)
  token = Column(String, nullable=True)
  
  def get_values(self):
    return {
      "id":self.id,
      "username":self.username,
      "password": self.username,
      "name": self.name,
      "last_name": self.last_name,
      "user_type": self.user_type,
      "is_active": self.is_active,
      "created":self.created,
      "modified": self.modified,
      "last_login":self.last_login,
      "token":self.token
      } 