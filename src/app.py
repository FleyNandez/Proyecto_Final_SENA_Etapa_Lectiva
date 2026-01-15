from flask import Flask, render_template
from flask_controller import FlaskControllerRegister
from src.modelos import Base, engine, session
from src.modelos.usuario import Usuario
from src.modelos.contratista import Contratista
from src.modelos.orden_trabajo import Orden_Trabajo
from src.modelos.movil import Movil
from src.modelos.ordenes_cerradas import Ordenes_Cerradas
from src.modelos.mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from flask import request, redirect, url_for, jsonify
import datetime
from flask_login import LoginManager
from flask_cors import CORS



app =Flask(__name__)

cors = CORS(app) 
app.config['CORS_HEADERS'] = 'Content-Type'

Base.metadata.create_all(engine)

register = FlaskControllerRegister(app)
register.register_package('src.controllers')

if __name__ == '__main__':
    app.run(debug=True) 
    
