from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() #THis instance will intereact with the db
migrate = Migrate() #This instance will allow to use migrate and in general db commands
