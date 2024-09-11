from flask import Blueprint, render_template, request, redirect, url_for
from app.models.inventory import Inventory
from app.services.inventoryService import get_all_inventory, add_inventory, update_inventory, delete_inventory
from app.utils.forms import ProductForm
from app.extensions import db

#Dffine the blueprint (Blueprint sis an object to organize and handle routes)
inventory_bp = Blueprint('inventory_bp', __name__)

@inventory_bp.route('/') #Difine a new route to inventory (GET)
def index():
    inventories = get_all_inventory() #this function retrieves all inventory items
    return render_template('index.html', inventories=inventories) #will render the index template

@inventory_bp.route('/add', methods=['POST']) # will define a new route and a http request called POST, to create a new item into the db
def add():
    data = request.form.to_dict() #converts the data from the form into a dict
    add_inventory(data) # it will add the item to the database
    return redirect(url_for('inventory_bp.index')) # it will return the index with the new item

@inventory_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    inventory = Inventory.query.get_or_404(id)
    form = ProductForm(obj=inventory)  #Initialize form with inventory data

    if form.validate_on_submit():  # checkk if the form was submitted and validated
        form.populate_obj(inventory)  # Update the inventory object with form data
        db.session.commit()  # Save changes to the database
        return redirect(url_for('inventory_bp.index'))  # Redirect to the index page

    return render_template('edit.html', form=form)  # Render edit form

@inventory_bp.route('/delete/<int:id>', methods=['POST']) #Dwfines a new route for deleting an existing item
def delete(id):
    delete_inventory(id) #Function to delete an item from the db
    return redirect(url_for('inventory_bp.index')) # WIll render the index page
