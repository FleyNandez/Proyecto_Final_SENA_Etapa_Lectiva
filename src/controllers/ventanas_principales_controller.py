from src.app import app 
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.modelos.usuario import Usuario
from src.modelos.contratista import Contratista
from src.modelos.orden_trabajo import Orden_Trabajo
from src.modelos.movil import Movil
from src.modelos.ordenes_cerradas import Ordenes_Cerradas
from src.modelos.mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from src.modelos import Base, engine, session



class Ventanas_PrincipalesController(FlaskController):
    
    
   @app.route('/registro_exitoso')
   def registro_exitoso():
    id = request.args.get('id')
    return render_template('solicitud_registrada_con_exito.html', titulo_pagina = "REGISTRO EXITOSO", id=id)

   @app.route('/consultar')
   def consultar():
       return render_template('consultar.html', titulo_pagina = "CONSULTAR")

   @app.route('/solicitud_en_curso')
   def solicitud_en_curso():
       return render_template('solicitud_en_curso.html', titulo_pagina = "SOLICITUD EN CURSO")

   @app.route('/quienes_somos') 
   def quienes_somos ():
       return render_template('quienes_somos.html', titulo_pagina = "QUIENES SOMOS")

   @app.route('/MOD')
   def MOD ():
       return render_template('MOD.html', titulo_pagina = "MOD")

   @app.route('/contratista')
   def contratista():
       return render_template('contratista.html', titulo_pagina = "contratista")

   @app.route('/moviles')
   def moviles():
       return render_template('moviles.html', titulo_pagina = "moviles")    
   
