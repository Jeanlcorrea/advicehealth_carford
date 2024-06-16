from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from app.swagger import swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_pyfile('config.py')

    SWAGGER_URL = '/api-docs'
    API_URL = '/static/swagger.json'

    @app.route('/static/swagger.json')
    def serve_swagger():
        return swagger()

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "CarFord | Docs"
        }
    )

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes.owners_routes import car_owners_bp
    from app.routes.cars_routes import cars_bp

    app.register_blueprint(swaggerui_blueprint)
    app.register_blueprint(car_owners_bp)
    app.register_blueprint(cars_bp)

    return app
