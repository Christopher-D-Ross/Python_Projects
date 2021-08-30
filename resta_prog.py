class Beast:
    def __init__(self, customer = {}, menu = {"chicken": 10, "broccoli": 5, "carrots": 4, "tea": 3} , items = [], funds = 0, total_price = 0, served = False):
        self.customer = customer
        self.menu = menu
        self.items = items
        self.total_price = total_price
        self.served = served
        self.funds = funds

    def add_funds(self, x):
        self.funds += x
    
    def add_customer_name(self, name):
        self.customer["name"] = name

    def add_customer_email(self, email):
        self.customer["email"] = email

    def add_customer_phone(self, phone):
        self.customer["phone"] = phone

    def print_menu(self):
            print(list(self.menu))

    def add_items(self, item):
        self.items.append(item)
        

    def remove_items(self, item):
        self.items.remove(item)

    def change_item_price(self):
        self.menu[menu_item] = "price"

    def get_total_price(self):
            self.total_price += self.menu[item]["price"]

chris_order = Beast()

chris_order.add_customer_name("Christopher Ross")
chris_order.add_customer_email("ross758@gmail.com")
chris_order.add_customer_phone("227-222-7777")
chris_order.add_items("carrots")
chris_order.add_items("tea")
chris_order.add_funds(20)
chris_order.print_menu()

print(chris_order.customer)
print(chris_order.items)
print(chris_order.funds)
print(chris_order.menu)
print(chris_order.total_price)