from flask import Flask
from server.extensions import db, migrate, jwt, bcrypt
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    # Import and register blueprints/controllers here if needed
    
    return app

app = create_app()