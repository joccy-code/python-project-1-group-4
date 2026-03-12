#  1) Build a program that:
# Displays a list of snacks and drinks with item numbers and prices. 
# Ask the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types "done".
# Finally prints a receipt showing: List of selected items with prices and total cost

# Menu of items
menu = {
    1: ("Chips", 1.50),
    2: ("Chocolate Bar", 2.00),
    3: ("Cookies", 1.60),
    4: ("Soda", 1.25),
    5: ("Water", 1.00),
    6: ("Juice", 1.80)
}

# Display menu
print("Welcome to the Snack and Drink Shop!")
print("Here is our menu:\n")

for number, (item, price) in menu.items():
    print(f"{number}. {item} - ${price:.2f}")

print("\nType the item number to add it to your order.")
print('Type "done" when finished.\n')

selected_items = []
total_cost = 0.0

# User selection loop
while True:
    choice = input("Enter item number (or 'done'): ").strip().lower()

    if choice == "done":
        break

    if not choice.isdigit() or int(choice) not in menu:
        print("Invalid choice. Please enter a valid item number.")
        continue

    choice = int(choice)
    item, price = menu[choice]
    selected_items.append((item, price))
    total_cost += price
    print(f"Added {item} - ${price:.2f}")

# Print receipt
print("\n--- Receipt ---")
for item, price in selected_items:
    print(f"{item} - ${price:.2f}")

print(f"Total: ${total_cost:.2f}")
print("Thank you for your purchase!")



Output:

Welcome to the Snack and Drink Shop!
Here is our menu:

1. Chips - $1.50
2. Chocolate Bar - $2.00
3. Cookies - $1.60
4. Soda - $1.25
5. Water - $1.00
6. Juice - $1.80

Type the item number to add it to your order.
Type "done" when finished.

Enter item number (or 'done'): 1
Added Chips - $1.50
Enter item number (or 'done'): 4
Added Soda - $1.25
Enter item number (or 'done'): done

--- Receipt ---
Chips - $1.50
Soda - $1.25
Total: $2.75
Thank you for your purchase!



# 2) Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user "add" items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.

# Predefined grocery dictionary
groceries = {
    "apple": 0.99,
    "banana": 0.59,
    "milk": 3.49,
    "bread": 2.79,
    "eggs": 4.25,
    "rice": 5.99
}

cart = {}

print("Welcome to the Grocery Store!")
print("Available items:\n")

for item, price in groceries.items():
    print(f"- {item.capitalize()}: ${price:.2f}")

print('\nType the item name to add it to your cart.')
print('Type "checkout" when you are finished.\n')

# Main loop
while True:
    choice = input("Enter item name (or 'checkout'): ").strip().lower()

    if choice == "checkout":
        break

    if choice not in groceries:
        print("Item not found. Please enter a valid item name.")
        continue

    # Ask for quantity
    try:
        qty = int(input(f"How many {choice}s would you like? "))
        if qty <= 0:
            print("Quantity must be a positive number.")
            continue
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue

    # Add to cart
    if choice in cart:
        cart[choice] += qty
    else:
        cart[choice] = qty

    print(f"Added {qty} x {choice}(s) to your cart.\n")

# Print final bill
print("\n--- Final Bill ---")
total = 0

for item, qty in cart.items():
    price = groceries[item]
    subtotal = price * qty
    total += subtotal
    print(f"{item.capitalize()} (x{qty}) - ${subtotal:.2f}")

print(f"\nTotal: ${total:.2f}")
print("Thank you for shopping!")


Output:

Welcome to the Grocery Store!

Available items:

- Apple: $0.99
- Banana: $0.59
- Milk: $3.49
- Bread: $2.79
- Eggs: $4.25
- Rice: $5.99

Type the item name to add it to your cart.
Type "checkout" when you are finished.

Enter item name (or 'checkout'): bread
How many breads would you like? 1
Added 1 x bread(s) to your cart.

Enter item name (or 'checkout'): checkout

--- Final Bill ---
Bread (x1) - $2.79

Total: $2.79
Thank you for shopping!



# 3) Build a to-do list manager that
# Allows users to add tasks with priorities (e.g., "Buy milk - high").
# Lets them view the current list, delete tasks by number, and mark tasks as complete.
# Keeps looping until the user types "exit".
# Shows a summary at the end: number of completed tasks vs pending.

tasks = []

while True:
    print("\n--- TO‑DO LIST MANAGER ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task complete")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task description: ")
        priority = input("Enter priority (high/medium/low): ")
        tasks.append({"task": task, "priority": priority, "completed": False})
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nCurrent Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✓" if t["completed"] else "✗"
                print(f"{i}. {t['task']} - {t['priority']} - {status}")

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted.")
        else:
            print("Invalid number.")

    elif choice == "4":
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked complete!")
        else:
            print("Invalid number.")

    elif choice == "5":
        break

    else:
        print("Invalid option. Try again.")

# Summary
completed = sum(1 for t in tasks if t["completed"])
pending = len(tasks) - completed

print("\n--- SUMMARY ---")
print(f"Completed tasks: {completed}")
print(f"Pending tasks: {pending}")

Output:
--- TO‑DO LIST MANAGER ---
1. Add task
2. View tasks
3. Delete task
4. Mark task complete
5. Exit
Choose an option: 1 
Enter task description: Add task
Enter priority (high/medium/low): medium
Task added!

--- TO‑DO LIST MANAGER ---
1. Add task
2. View tasks
3. Delete task
4. Mark task complete
5. Exit
Choose an option: 5

--- SUMMARY ---
Completed tasks: 0
Pending tasks: 1


       
# 4) Movie Ticket Booking Simulation
# Simulate a movie theater booking system that:
# Shows a list of available movie titles, showtimes, and seat prices.
# Asks the user to choose a movie and number of tickets.
# Confirms total price and asks if they want to book another movie.
# Ends when they say "no" and displays total bookings and cost.

movies = {
    "1": {"title": "Avengers", "time": "5:00 PM", "price": 12},
    "2": {"title": "Batman", "time": "7:30 PM", "price": 10},
    "3": {"title": "Frozen", "time": "3:00 PM", "price": 8}
}

total_tickets = 0
total_cost = 0

while True:
    print("\n--- MOVIE LIST ---")
    for key, m in movies.items():
        print(f"{key}. {m['title']} - {m['time']} - ${m['price']}")

    choice = input("Choose a movie number: ")

    if choice not in movies:
        print("Invalid choice.")
        continue

    tickets = int(input("How many tickets? "))
    price = tickets * movies[choice]["price"]

    print(f"Total price: ${price}")
    confirm = input("Book another movie? (yes/no): ").lower()

    total_tickets += tickets
    total_cost += price

    if confirm == "no":
        break

print("\n--- BOOKING SUMMARY ---")
print(f"Total tickets booked: {total_tickets}")
print(f"Total cost: ${total_cost}")

Output:
--- MOVIE LIST ---
1. Avengers - 5:00 PM - $12
2. Batman - 7:30 PM - $10
3. Frozen - 3:00 PM - $8
Choose a movie number: 2
How many tickets? 3
Total price: $30
Book another movie? (yes/no): no

--- BOOKING SUMMARY ---
Total tickets booked: 3
Total cost: $30


# 5) Create a basic quiz game that:
# Contains a list of 5–10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
# Ask the user each question and records their answers.
# At the end, displays:
# The user's score (e.g., 7/10)
# Correct answers for any questions they got wrong

questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "Who wrote 'Harry Potter'?": "J.K. Rowling",
    "What planet is known as the Red Planet?": "Mars",
    "What gas do plants breathe in?": "Carbon dioxide"
}

score = 0
wrong_answers = {}

for q, correct in questions.items():
    print("\n" + q)
    answer = input("Your answer: ")

    if answer.strip().lower() == correct.lower():
        score += 1
    else:
        wrong_answers[q] = correct

print("\n--- QUIZ RESULTS ---")
print(f"Your score: {score}/{len(questions)}")

if wrong_answers:
    print("\nCorrect answers for the ones you missed:")
    for q, ans in wrong_answers.items():
        print(f"{q} -> {ans}")

Output:

What is the capital of France?
Your answer: Paris

What is 5 + 7?
Your answer: 12

Who wrote 'Harry Potter'?
Your answer: J.K. Rowling

What planet is known as the Red Planet?
Your answer: Mars

What gas do plants breathe in?
Your answer: Carbon dioxide

--- QUIZ RESULTS ---
Your score: 5/5



