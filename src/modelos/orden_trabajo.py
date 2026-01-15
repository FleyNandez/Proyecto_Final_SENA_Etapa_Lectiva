from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
import datetime
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 
from .mis_enums import TipoFallaEnum, LocalidadEnum, MovilEnum, EstadoOrdenEnum
from flask import jsonify
from src.modelos.usuario import Usuario

from sqlalchemy.orm import relationship



class Orden_Trabajo(Base):
    __tablename__ = "Orden_Trabajo"
    id = Column(Integer, ForeignKey("Usuario.id"), primary_key=True)    
    direccion_falla = Column(String(300), unique=False, nullable=False)
    localidad = Column(Enum(LocalidadEnum), unique=False, nullable=False)
    tipo_falla = Column(Enum(TipoFallaEnum), unique=False, nullable=False)    
    movil = Column(Enum(MovilEnum), nullable=True) 
    estado = Column(Enum(EstadoOrdenEnum), default=EstadoOrdenEnum.PENDIENTE)

   
    
    usuario = relationship("Usuario", back_populates="ordenes_trabajo")
        

    def __init__(self, id, direccion_falla, localidad, tipo_falla, movil=None):
        self.id = id        
        self.direccion_falla = direccion_falla
        self.localidad = localidad
        self.tipo_falla = tipo_falla
        self.movil = movil
        
        

    @staticmethod
    def obtener_datos_orden():
        with Session() as session:
            ordenes = session.query(Orden_Trabajo).all() 
        return ordenes

    @staticmethod
    def asignar_movil(orden_trabajo_id, movil):
        with Session() as session:
            orden_trabajo = session.query(Orden_Trabajo).filter_by(id=orden_trabajo_id).first()
            
            if orden_trabajo:
                orden_trabajo.movil = movil                  
                session.commit() 
                return True
            return False

    @staticmethod
    def obtener_ordenes_por_movil(movil):
        with Session() as session:
            ordenes = session.query(Orden_Trabajo).filter_by(movil=movil).all()
        return ordenes
    
    @staticmethod
    def obtener_por_id(orden_id):        
        with Session() as session:
            return session.query(Orden_Trabajo).filter_by(id=orden_id).first()
    
    @staticmethod
    def obtener_usuarios_con_ordenes():
        with Session() as session:
            return (
                session.query(Usuario, Orden_Trabajo).join(Orden_Trabajo, Usuario.id == Orden_Trabajo.id, isouter=True).all())
   
    
    