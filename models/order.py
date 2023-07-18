class Order:
    def __init__(self, customer_name, order_date, beer_type, quantity, description):
        self.customer_name = customer_name
        self.order_date = order_date
        self.beer_type = beer_type
        self.quantity = quantity
        self.description = description