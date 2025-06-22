from flask import Flask, jsonify
from flask_migrate import Migrate
from .models import db, jwt, init_app
from .controllers import api

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
    
    init_app(app)
    Migrate(app, db)
    
    app.register_blueprint(api, url_prefix='/api')
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"message": "Resource not found"}), 404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"message": "Internal server error"}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)