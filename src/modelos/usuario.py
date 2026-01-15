from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
import datetime
from sqlalchemy.ext.declarative import declarative_base
from .mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum, MovilEnum
from src.modelos import Session, Base 
from sqlalchemy.orm import relationship




class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column (Integer, primary_key = True)
    fecha_reporte = Column(DateTime, default=datetime.datetime.now, nullable=False)
    nombre = Column (String, nullable=False)
    apellido = Column (String, nullable=False)
    tipo_documento = Column (Enum(TipoDocumentoEnum), nullable=False)
    numero_documento = Column (String(20), nullable=False )
    direccion_falla = Column (String(100), nullable=False)
    localidad = Column (Enum(LocalidadEnum),  nullable = False) 
    email = Column (String)
    celular = Column (String)
    tipo_falla = Column (Enum(TipoFallaEnum),  nullable = False)  
    
    ordenes_trabajo = relationship("Orden_Trabajo", back_populates="usuario")
    
          
        
    def __init__(self, nombre, apellido, tipo_documento, numero_documento, direccion_falla,localidad, email, celular, tipo_falla):
        
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.direccion_falla = direccion_falla
        self.localidad = localidad
        self.email = email
        self.celular = celular
        self.tipo_falla = tipo_falla
        
    @staticmethod
    def obtener_datos_usuario():
      with Session() as session:
            usuarios = session.query(Usuario).all()                            
      return usuarios
    
    
    @staticmethod
    def agregar_datos_usuario(datos_usuario):
      with Session() as session:
         usuarios = session.add(datos_usuario)
         session.commit()
      return usuarios
    
    