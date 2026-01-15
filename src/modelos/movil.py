from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from .mis_enums import MovilEnum 
from src.modelos import Session, Base 



class Movil(Base):
    __tablename__ = "Movil"
    id = Column (Integer, primary_key = True)
    movil = Column (Enum(MovilEnum), unique=True, nullable = False)
    
    
    def __init__(self, movil):
        
        self.movil = movil
        
    
    

        
 
   