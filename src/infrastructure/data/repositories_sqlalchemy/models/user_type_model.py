from sqlalchemy import Column, String, UUID, Integer
from src.infrastructure.data.repositories_sqlalchemy.models.base import Base

class User_Type(Base):
  __tablename__ = "user_types"
  
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  
  def get_values(self):
    return {
      "id": self.id,
      "name": self.name
    }