#3) write a program that shows to do list and allows the user to select a task. The program should then display the details of the selected task.
# display to do list to the user
# define the to do list with tasks and their details
To_do_list = {
    "1": {"task": "Buy groceries", "details": "Milk, Eggs, Bread, and Fruits"},
    "2": {"task": "Clean the house", "details": "Vacuum, Dust, and Mop the floors"},
    "3": {"task": "Finish homework", "details": "Complete math and science assignments"},
    "4": {"task": "Exercise", "details": "Go for a 30-minute run and do strength training"},
    "5": {"task": "Call family", "details": "Catch up with parents and siblings"},
    "6": {"task": "Pay bills", "details": "Electricity, Water, and Internet"},
    "7": {"task": "Read a book", "details": "Read at least 20 pages of a novel"},
    "8": {"task": "Cook dinner", "details": "Prepare a healthy meal with vegetables and protein"},
    "9": {"task": "Organize workspace", "details": "Declutter desk and organize files"},
    "10": {"task": "Plan weekend trip", "details": "Research destinations and make reservations"}
}
print("Welcome to your To-Do List!")
print("Please select a task from the list below:")      
To_do_list = []
priorities = ["high", "medium", "low"]
while True:
    task = input("Enter a task (or type 'done' to finish): ")
    if task.lower() == "done":
        break
    priority = input("Enter the priority (high, medium, low): ")
    if priority.lower() in priorities:
        To_do_list.append((task, priority.lower()))
        To_do_list.sort(key=lambda x: priorities.index(x[1]))
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
To_do_list.sort(key=lambda x: priorities.index(x[1]))
print("\nTo-Do List:")
for task, priority in To_do_list:
    print(f"{task} - {priority}")
    print("\nEnter the task you have completed (or type 'done' to finish): ")
while True:    
    completed_task = input()
    if completed_task.lower() == "done":
        break
    for task in To_do_list:
        if task[0].lower() == completed_task.lower():
            To_do_list.remove(task)
            print(f"Task '{completed_task}' marked as completed and removed from the list.")
            break
print("\nUpdated To-Do List:")
for task, priority in To_do_list:
    print(f"{task} - {priority}")