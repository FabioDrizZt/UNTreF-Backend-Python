from flask import Blueprint

general_bp = Blueprint("general_bp", __name__)


@general_bp.route("/")
def hello_world():
    """Endpoint de bienvenida"""
    return "Bienvenidos a Flask!!"


@general_bp.route("/saludo/")
def saludoAnonimo():
    return "¡Hola, usuario!"


@general_bp.route("/saludo/<nombre>")
def saludo(nombre="usuario"):
    """Endpoint de saludo personalizado"""
    return f"¡Hola, {nombre}!"
