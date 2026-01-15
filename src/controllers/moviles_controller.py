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



class MovilController(FlaskController):
    
    
 @app.route('/login', methods=['POST'])
 def login():
    
    username = request.form.get('username')
    
    if username == "movil_1":
        return redirect(url_for('movil_liviano'))
    elif username == "movil_2":
        return redirect(url_for('movil_canasta'))
    elif username == "movil_3":
        return redirect(url_for('movil_subterraneo'))
    
    

  
 @app.route('/movil_liviano')
 def movil_liviano():
    ordenes = Orden_Trabajo.obtener_ordenes_por_movil("movil_1")
    ordenes_cerradas = Ordenes_Cerradas.obtener_datos_ordenes_cerradas()
    ids_cerrados = [orden.id_reporte for orden in ordenes_cerradas]
    return render_template('movil_liviano.html',titulo_pagina="Movil Liviano",ordenes=ordenes,ids_cerrados=ids_cerrados)


 @app.route('/movil_canasta')
 def movil_canasta():
    ordenes = Orden_Trabajo.obtener_ordenes_por_movil("movil_2")
    ordenes_cerradas = Ordenes_Cerradas.obtener_datos_ordenes_cerradas()
    ids_cerrados = [orden.id_reporte for orden in ordenes_cerradas]
    return render_template('movil_canasta.html', titulo_pagina="Movil Canasta", ordenes=ordenes, ids_cerrados=ids_cerrados)

 @app.route('/movil_subterraneo')
 def movil_subterraneo():
    ordenes = Orden_Trabajo.obtener_ordenes_por_movil("movil_3")
    ordenes_cerradas = Ordenes_Cerradas.obtener_datos_ordenes_cerradas()
    ids_cerrados = [orden.id_reporte for orden in ordenes_cerradas]
    return render_template('movil_subterraneo.html', titulo_pagina="Movil Subterraneo", ordenes=ordenes, ids_cerrados=ids_cerrados)


@app.route('/moviles_ordenes', methods=['POST'])
def moviles_ordenes():
    data = request.get_json()  
    if not data:
      return jsonify({"success": False, "error": "No se enviaron datos"}), 400

    orden_trabajo_id = data.get('usuario_id')
    movil_id = data.get('movil')

    if not orden_trabajo_id or not movil_id:
        return jsonify({"success": False, "error": "Datos incompletos"}), 400

    if Orden_Trabajo.asignar_movil(orden_trabajo_id, movil_id):
        return jsonify({"success": True, "message": "Movil asignado correctamente"})    
    return jsonify({"success": False, "error": "No se pudo asignar el móvil"}), 400