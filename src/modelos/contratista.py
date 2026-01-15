
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from src.modelos.mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from src.modelos.usuario import Usuario
from src.modelos import Session, Base


class Contratista(Base):
    __tablename__ = "Contratista"
    id = Column (Integer, primary_key = True)
    orden_trabajo = Column (Integer, ForeignKey("Orden_Trabajo.id"), nullable = False) 
    
    def __init__(self, contratista, usuario, orden_trabajo):
        
        self.contratista = contratista
        self.usuario = usuario
        self.orden_trabajo = orden_trabajo
           
         
   
