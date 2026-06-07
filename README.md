Task Adder

A beginner-friendly Python project that demonstrates how to save tasks to a file using functions and file handling.

📌 Description

This program:

Takes a task as input from the user
Checks if the task is empty
Saves the task into a file named task.txt
Displays a success message after saving

🧠 Concepts Used

Functions
User Input
String Methods
strip()
Conditional Statements (if)
File Handling
with open()
Append Mode ('a')

💻 Code

def add_task():

    task = input("Enter the task :")

    if task.strip() == "":
        print("The task can't be empty")
        return

    with open("task.txt", "a") as file:
        file.write(task + "\n")
        print("Added successfully")

add_task()

▶️ Example Output

Enter the task : Learn Python
Added successfully
Enter the task :
The task can't be empty

🎯 Learning Outcome

By building this project, you will learn:

How to create functions
How to take user input
How to validate input
How to save data into files
Basic file handling in Python
