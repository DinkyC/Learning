'''Purpose'''

# This functon takes an user input as to what the customer might want to eat and out puts the corresponding dollar price
# The user is prompted until they break out of the function using control D


menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def order():
    while True:
        try:
            order1 = input("Item: ")
            if order1 in menu:
                print(f"${menu[order1]}")
        except EOFError:
            print()
            break
order()


    