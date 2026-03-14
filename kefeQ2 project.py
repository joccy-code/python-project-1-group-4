# #2) Write a program that shows predefined grocery items and allows the user to select an item. The program should then display the price of the selected item.
Grocery_menu ={
     "Apple": {"name": "Apple", "price": 3.50},
     "Banana": {"name": "Banana", "price": 0.52},
     "Bread": {"name": "Bread", "price": 2.00},
     "Milk": {"name": "Milk", "price": 3.50},
     "Eggs": {"name": "Eggs", "price": 2.50},
     "Cheese": {"name": "Cheese", "price": 3.00},
     "Chicken": {"name": "Chicken", "price": 5.00},
     "Rice": {"name": "Rice", "price": 4.00},
     "Pasta": {"name": "Pasta", "price": 2.25},
     "Tomatoes": {"name": "Tomatoes", "price": 0.85}
}
print("Welcome to the Grocery Menu!")
print("Please select an item from the menu below:")
for key, item in Grocery_menu.items():
    print(f"{key}. {item['name']} - ${item['price']:.2f}")
while True:
    selection = input("Enter the name of the item you want to select (or 'exit' to quit): ")
    if selection.lower() == 'exit':
        calculate_total = input("Would you like to calculate the total cost of your selected items? (y/n): ")
        if calculate_total.lower() == 'y':
            total = sum(item['price'] for item in Grocery_menu.values())
            print(f"The subtotal cost of your selected items is: ${total:.2f}")
            tax = total * 0.07  # Assuming a tax rate of 7%
            total_with_tax = total + tax
            print(f"Total with tax: ${total_with_tax:.2f}")
        print("Thank you for visiting! Goodbye!")
        break
    elif selection in Grocery_menu:
        selected_item = Grocery_menu[selection]
        print(f"You selected {selected_item['name']} which costs ${selected_item['price']:.2f}.")
    else:
        print("Invalid selection. Please try again.")