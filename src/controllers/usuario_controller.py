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



class UsuarioController(FlaskController):
    

 @app.route('/generar_reporte', methods = ['POST', 'GET'])
 def generar_reporte():       
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        tipo_documento = request.form.get('tipo_documento')
        numero_documento = request.form.get('numero_documento')
        direccion_falla = request.form.get('direccion_falla')
        localidad = request.form.get('localidad')
        email = request.form.get('email')
        celular = request.form.get('celular')
        tipo_falla = request.form.get('tipo_falla')       
                              
        usuario = Usuario (nombre,apellido,tipo_documento,numero_documento,direccion_falla,localidad,email,celular,tipo_falla)
        Usuario.agregar_datos_usuario(usuario)
        session.add(usuario)
        session.commit()
                      
        orden_trabajo = Orden_Trabajo(id=usuario.id, direccion_falla=direccion_falla, localidad=localidad, tipo_falla=tipo_falla)
        session.add(orden_trabajo)
        session.commit()
        
        return redirect(url_for('registro_exitoso', id=usuario.id))
    return render_template('generar_reportes.html', titulo_pagina = "GENERAR REPORTE")

