wallet = 100
eat_stuff = ["1_chicken", "2_broccoli", "3_carrots", "4_cashews"]
prices = [60, 30, 30, 40]

# Didn't need it after all
"""bird = eat_stuff[0]
flora = eat_stuff[1]
orange = eat_stuff[2]
t_best = eat_stuff[3]"""

food_prices = zip(eat_stuff, prices)
menu = list(food_prices)
print(menu)

customer = input("Please choose an item on the menu by entering the number to the left of that item.")
if len(customer) > 0 and customer == "1":
    print("Thank you for choosing the chicken!! Your balance after payment will be", wallet - prices[0], "dollars.")
    wallet -= 60
elif customer == "2":
    print("Thank you for choosing the broccoli!! Your balance after payment will be", wallet - prices[1], "dollars.")
    wallet -= 30
elif customer == "3":
    print("Thank you for choosing the carrots!! Your balance after payment will be", wallet - prices[2], "dollars.")
    wallet -= 30
elif customer == "4":
    print("Thank you for choosing the cashews!! Your balance after payment will be", wallet - prices[3], "dollars.")
    wallet -= 40
else:
    print("You have chosen not to eat.")
while wallet >= 30:
    seconds = input("Would you like more greedy? Enter yes or no.")
    if seconds == "yes" and wallet > 30:
        customer_2 = input("Please choose an item on the menu by entering the number to the left of that item.")
    else:
        print("You have either chosen not to eat or do not have sufficient funds. Have a nice day.")
    if seconds == "yes" and customer_2 == "1":
        print("Thank you for choosing the chicken!! Your balance after payment will be", wallet - prices[0],
                  "dollars.")
        wallet -= 60
    elif customer_2 == "2":
        print("Thank you for choosing the broccoli!! Your balance after payment will be", wallet - prices[1],
                  "dollars.")
        wallet -= 30
    elif customer_2 == "3":
        print("Thank you for choosing the carrots!! Your balance after payment will be", wallet - prices[2],
                  "dollars.")
        wallet -= 30
    elif customer_2 == "4":
        print("Thank you for choosing the cashews!! Your balance after payment will be", wallet - prices[3],
                  "dollars.")
        wallet -= 40
else:
    print("You have either chosen not to eat or do not have sufficient funds to continue eating. Have a nice day.")