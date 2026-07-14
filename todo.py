tasks = []

while True:
    print("\n----- TO-DO LIST-----")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Exit ")

    choice = input("Enter your choice:")
    
    if choice == "1":
        new_task = input("Enter task:")
        tasks.append(new_task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for i in range(len(tasks)):
                print(i + 1,"-", tasks[i])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

