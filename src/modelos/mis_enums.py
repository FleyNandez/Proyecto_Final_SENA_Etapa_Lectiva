from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum 

Base = declarative_base()

class TipoDocumentoEnum(PyEnum):
    CC = "cedula ciudadania"
    CE = "cedula extranjera"

class LocalidadEnum(PyEnum):
    localidad_1 = "Usaquén"
    localidad_2 = "Chapinero"
    localidad_3 = "Santa Fe"
    localidad_4 = "San Cristóbal"
    localidad_5 = "Usme"
    localidad_6 = "Tunjuelito"
    localidad_7 = "Bosa"
    localidad_8 = "Kennedy"
    localidad_9 = "Fontibón"
    localidad_10 = "Engativá"
    localidad_11 = "Suba"
    localidad_12 = "Barrios Unidos"
    localidad_13 = "Teusaquillo"
    localidad_14 = "Mártires"
    localidad_15 = "Antonio Nariño"
    localidad_16 = "Puente Aranda"
    localidad_17 = "Candelaria"
    localidad_18 = "Rafael Uribe"
    localidad_19 = "Ciudad Bolívar"
    localidad_20 = "Sumapaz"

class TipoFallaEnum(PyEnum):
    falla_1 = "luminaria apagada"
    falla_2 = "luminaria hurtada"
    falla_3 = "sector sin alumbrado"
    falla_4 = "cables sueltos"
    falla_5 = "poste en mal estado"
    falla_6 = "Solicitud luminaria nueva"
    
    
class MovilEnum(PyEnum):
    movil_1 = "Liviano-Fleyder Hernandez"
    movil_2 = "Canasta-Jimmy Otalora"
    movil_3 = "Subterraneo-Fabian Lopez" 
    
class EstadoOrdenEnum(PyEnum):
    PENDIENTE = "PENDIENTE"
    ASIGNADA = "ASIGNADA"
    CERRADA = "CERRADA"
    