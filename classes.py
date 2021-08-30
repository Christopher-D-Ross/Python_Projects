#class Pizza:
#    def __init__(self, size = "medium",crust = "thin", sauce = "tomato"):
#        self.size = size
#        self.crust = crust
#        self.sauce = sauce

#chris_pizza = Pizza()

#print(chris_pizza())


class Car:
    def __init__(self, make, model, color, current_speed = 0):
        self.make = make
        self.model = model
        self.color = color 
        self.current_speed = current_speed 

    def increase_speed(self, speed_increase):
        self.current_speed += speed_increase

    def decrease_speed(self, speed_decrease):
        self.current_speed -= speed_decrease

chris_car = Car("Ford", "Mustang", "Grey")

chris_car.increase_speed(20)

print(chris_car.increase_speed)

class Order:
    def __init__(self, is_delivery, customer = {}, items = [], total_price = 0, fulfilled = False):
        self.is_delivery = is_delivery
        self.customer = customer
        self.items = items
        self.total_price = total_price
        self.fulfilled = fulfilled
    
    def add_customer_name(self, name):
        self.customer["name"] = name

    def add_items(self, item):
        self.items.append(item)

    def get_total_price(self):
        index = 0
        while index < len(self.items):
            self.total_price += self.item[index]["price"]
            index += 1
        


new_order = Order(True)

new_order.add_customer_name("Chris")
new_order.add_items({"name":"Pizza", "price": 10 })
new_order.add_items({"name": "Salad", "price": 20})

print(new_order.customer)