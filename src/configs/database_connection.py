import psycopg2
from src.configs.config import bbdd
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

def create_connection():
  engine = bbdd["engine"]
  dbname = bbdd["name_db"]
  user=bbdd["user"]
  pssw = bbdd["pssw"]
  host = bbdd["host"]
  port=bbdd["port"]
  
  max_connections = int(bbdd["max_connections"] )
  
  url = f"{engine}://{user}:{pssw}@{host}:{port}/{dbname}"
  engine = sqlalchemy.create_engine(url,echo=True, pool_size=max_connections, pool_timeout=10000)
  
  return engine