from flask import jsonify
from .general_routes import general_bp
from .products_routes import productos_bp
from .actor_routes import actor_bp


def register_routes(app):
    app.register_blueprint(general_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(actor_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        """Manejador de error 404"""
        return jsonify(error="Recurso no encontrado"), 404
