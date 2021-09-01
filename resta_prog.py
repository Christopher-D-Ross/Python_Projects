class Beast:
    dinner_menu = {"chicken": 20, "broccoli": 10, "carrots": 8, "kale": 10}

    def __init__(self, customers = {}, menu = {} , cust_order = [], funds = 0, total_price = 0, served = False):
        self.customers = customers
        self.menu = menu
        self.cust_order = cust_order
        self.total_price = total_price
        self.served = served
        self.funds = funds
   
    #Welcome Method
    #This method will take in customer information and print the menu afterwards.
    def welcome_cust(self):
        wel_cust = {}
        wel_cust["name"] = input("May I have your name, please?")
        wel_cust["email"] = input("Your email?")
        wel_cust["phone"] = input("Lastly your phone number.")
        self.add_customer(wel_cust["name"], wel_cust["email"], wel_cust["phone"])
        self.print_menu()
        self.add_funds()
        self.add_to_cust_order()

    #Add funds to a Beast prepaid card
    def add_funds(self):
        fund_cust = input("Would you like to add funds to your Beast prepaid card?")
        if fund_cust == "yes" or fund_cust == "Yes":
            x = input("How much would you like to add?")
            self.funds += float(x)
            print("You now have $",self.funds, " on your Beast prepaid card.")
        else:
            print("Cash or debit is fine then.")
    
    #This method will run with the welcoming of every new customer
    def add_customer(self, name, email, phone):
        customer = {"name": name, "email": email, "phone": phone}
        self.customers[name] = customer
        print(self.customers)
   
    #Menu Methods
    def print_menu(self):
            print("Here's our menu:")
            print(Beast.dinner_menu)

    #This method can also be used to update the price of existing items.
    def add_items_to_dinner_menu(self, item, price):
        self.dinner_menu[item] = price

    def remove_items_from_dinner_menu(self, item):
        del self.dinner_menu[item]

    #Customer Order
    def add_to_cust_order(self):
        cust_item = input("Please choose an item on the menu to add to your order by entering that item.")
        if cust_item == "chicken" or cust_item == "Chicken":
            self.cust_order.append("chicken")
            self.total_price += 20
            print("You ordered", self.cust_order,"and your current total is $",self.total_price,".")
        if cust_item == "broccoli" or cust_item == "Broccoli":
            self.cust_order.append("broccoli")
            self.total_price += 10
            print("You ordered", self.cust_order,"and your current total is $",self.total_price,".")
        if cust_item == "carrots" or cust_item == "Carrots":
            self.cust_order.append("carrots")
            self.total_price += 8
            print("You ordered", self.cust_order,"and your current total is $",self.total_price,".")
        if cust_item == "kale" or cust_item == "Kale":
            self.cust_order.append("kale")
            self.total_price += 10
            print("You ordered", self.cust_order,"and your current total is $",self.total_price,".")

    #Pricing methods
    def change_item_price(self, existing_item, price):
        self.dinner_menu[existing_item] = price

    def get_total_price(self,item):
            self.total_price += self.menu[item]["price"]

set_1 = Beast()

set_1.welcome_cust()
#set_1.add_items_to_dinner_menu("cashews", "8")
#print(Beast.dinner_menu)
#set_1.add_funds()
#set_1.remove_items_from_dinner_menu("chicken")
#set_1.change_item_price("broccoli", "15")
#print(Beast.dinner_menu)
#set_1.add_to_cust_order()