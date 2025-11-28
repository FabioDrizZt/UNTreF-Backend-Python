from flask import Blueprint, render_template, jsonify

productos_bp = Blueprint('general', __name__)

@productos_bp.route("/productos")
def productos():
    """Endpoint de listado de productos"""
    lista_productos = ["iPhone", "MacBook Pro", "iPad"]
    return render_template("productos.html", productos=lista_productos)

@productos_bp.route("/api/lista_productos")
def lista_productos():
    """Endpoint de listado de productos"""
    lista_productos = ["iPhone", "MacBook Pro", "iPad"]
    return jsonify(lista_productos), 200

@productos_bp.route("/api/lista_dict_productos")
def lista_dict_productos():
    """Endpoint de listado de productos"""
    try:
        """ {"nombre": "iPhone", "precio": 1000},
            {"nombre": "MacBook Pro", "precio": 5000},
            {"nombre": "iPad", "precio": 2000}, """
        lista_productos = [
            
        ]
        if not lista_productos:
            return jsonify(error="No se encontraron productos"), 404
        return jsonify(lista_productos), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
