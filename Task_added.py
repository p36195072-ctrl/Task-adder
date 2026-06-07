def add_task():

    task = input("Enter the task :")

    if task.strip() == "" :
        print("The task can't be emety")
        return

    with open("task.txt" , "a") as file:
        file.write(task + "\n")
        print("Added successfully")

add_task()