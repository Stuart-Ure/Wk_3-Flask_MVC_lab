from flask import Flask
from controllers.orders_controller import order_blueprint

app = Flask(__name__)
app.register_blueprint(order_blueprint)

@app.route('/')
def index():
    return "<h1>Stuart's Beer House!</h1>"