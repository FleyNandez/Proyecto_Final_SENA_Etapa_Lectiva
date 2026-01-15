from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
import datetime
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 
from .mis_enums import TipoFallaEnum, LocalidadEnum, MovilEnum, EstadoOrdenEnum
from flask import jsonify
from sqlalchemy.orm import relationship
from src.modelos.orden_trabajo import Orden_Trabajo


class Ordenes_Cerradas(Base):
    __tablename__ = "Ordenes_Cerradas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_reporte = Column(Integer, ForeignKey('Orden_Trabajo.id'))    
    direccion_falla = Column(String(300), nullable=False)
    tipo_falla = Column(Enum(TipoFallaEnum), nullable=False)
    localidad = Column(Enum(LocalidadEnum), nullable=False)
    movil = Column(Enum(MovilEnum), nullable=False) 

    def __init__(self, id_reporte, direccion_falla, localidad, tipo_falla, movil):
        
        self.id_reporte = id_reporte        
        self.direccion_falla = direccion_falla
        self.localidad = localidad
        self.tipo_falla = tipo_falla        
        self.movil = movil
        
    

    @staticmethod
    def obtener_datos_ordenes_cerradas():
        with Session() as session:
            return session.query(Ordenes_Cerradas).all()
        
   
        
    @staticmethod
    def cerrar_ordenes(orden_trabajo_id):
     with Session() as session:
        orden = session.query(Orden_Trabajo).filter_by(id=orden_trabajo_id).first()

        if orden:
            orden_cerrada = Ordenes_Cerradas(
                id_reporte=orden.id,
                direccion_falla=orden.direccion_falla,
                localidad=orden.localidad,
                tipo_falla=orden.tipo_falla,
                movil=orden.movil
            )
            session.add(orden_cerrada)

            
            orden.estado = EstadoOrdenEnum.CERRADA
            session.commit()
            return True
        

    @staticmethod
    def buscar_por_radicado(radicado):
        with Session() as session:
            return session.query(Ordenes_Cerradas).filter_by(id_reporte=radicado).first()
        
    @staticmethod
    def eliminar_orden_cerrada(id):
        with Session() as session:
            orden_cerrada = session.query(Ordenes_Cerradas).get(id)
            session.delete(orden_cerrada)
            session.commit()
            return orden_cerrada
        
    
    




        



    
     
  
    

  
  