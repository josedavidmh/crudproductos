from flask import Flask
from flask import jsonify,request,abort
from flask_cors import CORS
from flasgger import Swagger, swag_from
from app.models import Product, db
from app.controller import productos_bp
from app.common import Config
##from config import Config

app = Flask(__name__)
CORS(app) # Habilita el acceso de recursos a dominios externos
swagger=Swagger(app)

##app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Configurar la aplicación usando las credenciales de la clase Config
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    
@app.route("/")
def index():
    return 'Ve a <a href="/graphql">/graphql</a> para acceder a GraphiQL y probar la API GraphQL.'

app.register_blueprint(productos_bp)

if __name__=='__main__':
    app.run('0.0.0.0', debug=True, port="5001")