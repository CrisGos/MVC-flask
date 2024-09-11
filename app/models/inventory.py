from app.extensions import db
# This class represents teh database in Flask (however a good practice is to call the tables in plural, but the docuemnt asks for 'inventory)
class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    mac_address = db.Column(db.String(250), nullable=False)
    serial_number = db.Column(db.Integer, nullable=False)
    manufacturer = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
