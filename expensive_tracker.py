expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter Expense Amount: "))
        expenses.append(amount)
        print("Expense Added Successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No Expenses Found!")
        else:
            print("\nExpenses:")
            for expense in expenses:
                print(expense)

    elif choice == "3":
        total = sum(expenses)
        print("Total Expenses:", total)

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
