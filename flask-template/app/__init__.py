from os import path, environ
from flask import Flask, render_template, g, Blueprint
from flask_session import Session
from config import config
from app import db
from app.resources import issue
from app.resources import user
from app.resources import auth
from app.resources.api.issue import issue_api
from app.helpers import handler
from app.helpers import auth as helper_auth


def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    app.debug = True

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Configure db
    db.init_app(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )

    # Rutas de Consultas
    app.add_url_rule("/consultas", "issue_index", issue.index)
    app.add_url_rule("/consultas", "issue_create", issue.create, methods=["POST"])
    app.add_url_rule("/consultas/nueva", "issue_new", issue.new)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("mapa.html")
    
    @app.route("/mapa", methods=["GET", "POST"])
    def mapa():
        return render_template("mapa.html")
    
    @app.route("/resumen", methods=["GET", "POST"])
    def resumen():
        return render_template("resumen.html")
    
    @app.route("/paises", methods=["GET", "POST"])
    def paises():
        return render_template("paises.html")
    
    @app.route("/predicciones", methods=["GET", "POST"])
    def predicciones():
        return render_template("predicciones.html")

    @app.route("/data_mapa", methods=["GET", "POST"])
    def data_mapa():
        return render_template("data_mapa.html")

    # Rutas de API-REST (usando Blueprints)
    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(issue_api)

    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500

    # Retornar la instancia de app configurada
    return app
