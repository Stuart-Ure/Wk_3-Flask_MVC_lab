from flask import Blueprint, render_template
from models.orders_list import orders

order_blueprint= Blueprint("orders", __name__) 

@order_blueprint.route("/orders/")
def index():
    return render_template("index.html", title= "Stuarts Beer Shop - orders", orders_list= orders)


@order_blueprint.route("/orders/<int:index>")
def display_order(index):
    if index < len(orders):
        order = orders[index]
        return render_template("order.html", order=order)
    else:
        return "Order not found"