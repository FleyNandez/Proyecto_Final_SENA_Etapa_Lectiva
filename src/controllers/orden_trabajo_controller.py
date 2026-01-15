from src.app import app 
from flask import render_template, request, redirect, url_for, jsonify
from flask_controller import FlaskController
from src.modelos.usuario import Usuario
from src.modelos.contratista import Contratista
from src.modelos.orden_trabajo import Orden_Trabajo
from src.modelos.movil import Movil
from src.modelos.ordenes_cerradas import Ordenes_Cerradas
from src.modelos.mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from src.modelos import Base, engine, session


class Orden_TrabajoController(FlaskController):
    

 @app.route('/orden_trabajo')
 def ordenes():      
   usuarios_con_ordenes = Orden_Trabajo.obtener_usuarios_con_ordenes() 
   return render_template('orden_trabajo.html', titulo_pagina="ORDEN TRABAJO", usuarios_con_ordenes=usuarios_con_ordenes)
 
     
@app.route('/cerrar_orden', methods=['POST'])
def cerrar_orden():   
    data = request.get_json()
    
    if not data or 'orden_id' not in data:
        return jsonify({"success": False, "error": "Datos incompletos"}), 400

    orden_id = data['orden_id']
    orden = Orden_Trabajo.obtener_por_id(orden_id)

    if orden and Ordenes_Cerradas.cerrar_ordenes(orden.id):
        return jsonify({"success": True, "message": "Orden cerrada correctamente"})

    return jsonify({"success": False, "error": "No se pudo cerrar la orden"}), 400
 
@app.route('/ordenes_finalizadas')
def ordenes_finalizadas():
    ordenes_cerradas = Ordenes_Cerradas.obtener_datos_ordenes_cerradas()  
    return render_template('ordenes_finalizadas.html', titulo_pagina="Ordenes Finalizadas", ordenes=ordenes_cerradas)


 
@app.route('/consultar_solicitud', methods=['POST'])
def consultar_solicitud():
    radicado = request.form.get('radicado')

    if not radicado:
        return redirect(url_for('consultar')) 

    orden_cerrada = Ordenes_Cerradas.buscar_por_radicado(radicado)

    if orden_cerrada:
        return render_template('solicitud_atendida.html')
    else:
        return render_template('solicitud_en_curso.html')

@app.route('/eliminar_orden_cerrada/<id>')
def eliminar_orden_cerrada(id):
    Ordenes_Cerradas.eliminar_orden_cerrada(id)
    ordenes_cerradas = Ordenes_Cerradas.obtener_datos_ordenes_cerradas()    
    return render_template('ordenes_finalizadas.html', titulo_pagina="Ordenes Finalizadas", ordenes=ordenes_cerradas)
