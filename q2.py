# 2)	Write a program that:
# •	Has a predefined dictionary of groceries with prices.
# •	Lets the user "add" items by typing their names.
# •	For each valid item, asks for the quantity.
# •	Keeps adding to the cart until the user types "checkout".
# •	Displays a final bill: each item, quantity, subtotal, and total.

groceries = {
    "apple": 0.5,
    "banana": 0.3,
    "milk": 2.0,
    "bread": 1.5,
    "eggs": 3.0
}

cart = {}

print("Welcome to the Grocery Store!")
print("Available items:")
for item, price in groceries.items():
    print(f"{item} - ${price}")

while True:
    item = input("\nEnter item name (or type 'checkout' to finish): ").lower()

    if item == "checkout":
        break

    if item in groceries:
        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Item not found in store.")

# Display final bill
print("\n----- Final Bill -----")
total = 0

for item, quantity in cart.items():
    price = groceries[item]
    subtotal = price * quantity
    total += subtotal
    print(f"{item} x{quantity} @ ${price:.2f} = ${subtotal:.2f}")

print("----------------------")
print(f"Total: ${total:.2f}")
print("Thank you for shopping!")