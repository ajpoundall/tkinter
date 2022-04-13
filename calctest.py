from decimal import Decimal, ROUND_HALF_UP

#data_sets, could have had multiple for the different currencys...could automate the switch depending on local variable
change_ava = {
    '£50': 50.00, 
    "£20":20.00,
    "£10":10.00,
    "£5":5.00,
    "£2":2.00,
    "£1":1.00,
    "50p": 0.50,
    "20p": 0.20,
    "10p": 0.10,
    "5p": 0.05,
    "2p": 0.02,
    "1p":0.01,

}

change_used = {

}

#functions

#rounding - this caught me out..a LOT
def round_decimal(x):
  return x.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

#find the required change
def change_required(product_price, cash_provided):
    x = product_price
    y = cash_provided
    if y > x:
        change_required = round_decimal(Decimal(y)-Decimal(x))
    elif y == 0:
        print ("No change required")
    else:
        return False
    return change_required

#sort the change 
def change_sorted(change_required, change_ava, change_used):
    change_required = change_required
    change_ava = change_ava
    change_used = change_used
    if change_required > 0:
        for x, y in change_ava.items():
            a = round_decimal(Decimal(change_required)) // round_decimal(Decimal(y)) #check how many times the remainder is divisible
            if a != 0 and change_required > 0:
                change_required = change_required - (a * Decimal(y))
                change_required = round_decimal(change_required)
                change_used [x] = int(a)
            else:
                change_required == change_required
    return change_used

def message_for_change(change, product_price, cash_provided, change_required):
    change_required = change_required
    product_price = product_price
    cash_provided = cash_provided
    change = change
    print( "Thank you for your custom. You paid us £"+str(cash_provided)+" for a product worth £"+str(product_price)+". \nYour overall change is £"+str(change_required))
    print ("This is made up of the following")
    for x, y in change.items():
        print (str(y)+" x "+ str(x))

"""
def user_input(product_price, cash_provided):
    product_price = product_price
    cash_provided = cash_provided
    while product_price <= 0:
        product_price = input("Enter the product price ") #accepts user input via console for product price
        if type(product_price) != float:
            print("Please enter a number")
            return False
        elif product_price > 0:
            return (product_price) 
        elif product_price < 0:
            print("Cannot have a negative product price") 
    while cash_provided == 0:
        cash_provided = input("Enter the cash provided ") #accepts user input via console for product price
        if type(cash_provided) != float:
            print("Please enter a number")
            return False
        elif cash_provided > 0:
            return (product_price) 
        elif cash_provided < 0:
            print("Cannot have a negative cash value") 
"""

#main 
product_price = 0
cash_provided = 0
product_price = float(input("What is the product price "))
cash_provided = float(input("How much cash was provided "))
change_required = change_required(product_price, cash_provided)
if change_required != False:
    change = change_sorted(change_required, change_ava, change_used)
    message = message_for_change(change, product_price, cash_provided, change_required)
else:
    print ("Sorry you do not have enough money please provdide the correct amount")