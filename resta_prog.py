class Beast:
    def __init__(self, customer = {},menu ={"chicken": 10, "broccoli": 5, "carrots": 4, "tea": 3} , items = [], total_price = 0, served = False):
        self.customer = customer
        self.menu = menu
        self.items = items
        self.total_price = total_price
        self.served = served
    
    def add_customer_name(self, name):
        self.customer["name"] = name

    def add_items(self, item):
        self.items.append(item)

    def get_total_price(self):
        index = 0
        while index < len(self.items):
            self.total_price += self.item[index]["price"]
            index += 1