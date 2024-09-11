from app.models.inventory import Inventory
from app.extensions import db

def get_all_inventory(): #Retrieve all inventory from db
    return Inventory.query.all() #excute the query

def add_inventory(data): #Adds a new inventory item to the database
    try:
        new_inventory = Inventory(**data) #Create a new inventory object using the data provided, ** is for unpack the dict into columns type
        db.session.add(new_inventory) #adds the new product to the database
        db.session.commit()  #commit the transaction
    except Exception as e:
        db.session.rollback() #if an exception occurs it will remains the consistent of the db
        raise e

def update_inventory(id, data): 
    try:
        inventory = Inventory.query.get(id) #Fetches the inventory item with the specified id
        if inventory:
            for key, value in data.items(): 
                setattr(inventory, key, value) #Updates the attributes of the inventory object based on the provided data
            db.session.commit() #commit the transaction
    except Exception as e:
        db.session.rollback()
        raise e

def delete_inventory(id):
    try:
        inventory = Inventory.query.get(id) #Fetches the inventory item with the specified id
        if inventory:
            db.session.delete(inventory) # Marks the prodcut for deletion
            db.session.commit() #commit the transaction
    except Exception as e:
        db.session.rollback()
        raise e
