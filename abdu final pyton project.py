#**Python project**

# 1)	Build a program that:
# Displays a list of snacks and drinks with item numbers and prices. 
# Ask the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types "done".
# Finally prints a receipt showing: List of selected items with prices and total cost

menu = {
    1: ("Chips", 1.50),
    2: ("Soda", 2.00),
    3: ("Chocolate", 1.25),
    4: ("Water", 1.00),
    5: ("Cookies", 1.75)
}
cart = []
print("Menu:")
for num, item in menu.items():
    print(f"{num}. {item[0]} - ${item[1]:.2f}")
while True:
    choice = input("Select item number (or type 'done'): ").lower()
    if choice == "done":
        break
    if choice.isdigit() and int(choice) in menu:
        cart.append(menu[int(choice)])
        print(f"Added {menu[int(choice)][0]}")
    else:
        print("Invalid choice.")
print("\nReceipt:")
total = 0
for item, price in cart:
    print(f"{item} - ${price:.2f}")
    total += price
print(f"Total: ${total:.2f}")

# 2)	Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user "add" items by typing their names.
# For each valid item, asks for the quantity.
# Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total.

groceries = {
    "milk": 3.00,
    "bread": 2.50,
    "eggs": 4.00,
    "rice": 5.50,
    "apple": 0.75
}
cart = {}
while True:
    item = input("Enter item name (or 'checkout'): ").lower()
    if item == "checkout":
        break
    if item in groceries:
        qty = int(input("Quantity: "))
        cart[item] = cart.get(item, 0) + qty
    else:
        print("Item not available.")
print("\nFinal Bill:")
total = 0
for item, qty in cart.items():
    price = groceries[item]
    subtotal = price * qty
    total += subtotal
    print(f"{item} x{qty} = ${subtotal:.2f}")
print(f"Total: ${total:.2f}")

# 3)	Build a to-do list manager that
# Allows users to add tasks with priorities (e.g., "Buy milk - high").
# Lets them view the current list, delete tasks by number, and mark tasks as complete.
# Keeps looping until the user types "exit".
# Shows a summary at the end: number of completed tasks vs pending.

tasks = []
while True:
    print("\nOptions: add / view / delete / complete / exit")
    choice = input("Choose action: ").lower()
    if choice == "add":
        task = input("Enter task with priority: ")
        tasks.append({"task": task, "done": False})
    elif choice == "view":
        for i, t in enumerate(tasks, 1):
            status = "✔" if t["done"] else "✘"
            print(f"{i}. {t['task']} [{status}]")
    elif choice == "delete":
        num = int(input("Task number: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)
    elif choice == "complete":
        num = int(input("Task number: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True
    elif choice == "exit":
        break
completed = sum(t["done"] for t in tasks)
print(f"\nSummary: {completed} completed, {len(tasks)-completed} pending")

# 4)	 Movie Ticket Booking Simulation
# Simulate a movie theater booking system that:
# Shows a list of available movie titles, showtimes, and seat prices.
# Asks the user to choose a movie and number of tickets.
# Confirms total price and asks if they want to book another movie.
# Ends when they say "no" and displays total bookings and cost.

movies = {
    1: ("Avengers", "6PM", 10),
    2: ("Frozen", "4PM", 8),
    3: ("Batman", "9PM", 12)
}
total_cost = 0
total_tickets = 0
while True:
    print("\nMovies:")
    for num, info in movies.items():
        print(f"{num}. {info[0]} - {info[1]} - ${info[2]}")
    choice = int(input("Select movie number: "))
    tickets = int(input("Number of tickets: "))
    movie = movies[choice]
    cost = movie[2] * tickets
    print(f"Cost for {movie[0]}: ${cost}")
    total_cost += cost
    total_tickets += tickets
    again = input("Book another? (yes/no): ").lower()
    if again == "no":
        break
print(f"\nTotal tickets: {total_tickets}")
print(f"Total cost: ${total_cost}")

# 5)	Create a basic quiz game that:
# Contains a list of 5–10 questions stored in a dictionary 
# (or list of dictionaries [{}, {}] ).
# Ask the user each question and records their answers.
# At the end, displays:
# The user's score (e.g., 7/10)
# Correct answers for any questions they got wrong

questions = [
    {"q": "Capital of France?", "a": "paris"},
    {"q": "5 + 7 =", "a": "12"},
    {"q": "Color of sky?", "a": "blue"},
    {"q": "Water freezes at 0 degrees? (yes/no)", "a": "yes"},
    {"q": "Python is a snake or programming language?", "a": "programming language"}
]
score = 0
wrong = []
for q in questions:
    ans = input(q["q"] + " ").lower()
    if ans == q["a"]:
        score += 1
    else:
        wrong.append((q["q"], q["a"]))
print(f"\nScore: {score}/{len(questions)}")
if wrong:
    print("Review:")
    for q, a in wrong:
        print(f"{q} → Correct: {a}")