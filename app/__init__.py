from flask import Flask
from .extensions import db, migrate
from .routes.inventoryRoutes import inventory_bp

def create_app(): #This funciont will set up and return a Fllsk App
    app = Flask(__name__) #new Flask instance
    app.config.from_object('app.config.Config') #Loading  setting from config file

    # Initialize SQLAlchemy
    db.init_app(app)
    # Initialize migrate to use bash command flask db miugrate
    migrate.init_app(app, db)

    # Register Blueprint
    app.register_blueprint(inventory_bp)

    return app

