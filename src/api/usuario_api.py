from flask_restful import Resource
from flask import request
from flask_cors import cross_origin

from src.modelos.mis_enums import EstadoOrdenEnum, MovilEnum, LocalidadEnum,TipoFallaEnum, TipoDocumentoEnum
from src.modelos.usuario import Usuario
from src.modelos.orden_trabajo import Orden_Trabajo

class UsuarioApi(Resource):
    @cross_origin
    def post(self):
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        tipo_documento = request.json['tipo_documento']
        numero_documento = request.json['numero_documento']
        direccion_falla = request.json['direccion_falla']
        localidad = request.json['localidad']
        email = request.json['email']
        celular = request.json['celular']
        tipo_falla = request.json['tipo_falla']       
                              
        usuario = Usuario (nombre,apellido,tipo_documento,numero_documento,direccion_falla,localidad,email,celular,tipo_falla)
        Usuario.agregar_datos_usuario(usuario)
