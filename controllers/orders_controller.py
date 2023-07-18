from flask import Blueprint, render_template
from models.orders_list import orders

order_blueprint= Blueprint("orders", __name__) 

@order_blueprint.route("/")
def index():
    return render_template("index.html", title= "My orders", orders_list= orders)
