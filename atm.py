print("===== ATM System =====")

balance = 10000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdrw Money")
print("4. Exit")

choice = input("Enter your choice: ")
 
if choice =="1":
    print("Your Balance is:", balance)

elif choice == "2":
    amount = int(input("Enter deposit amount: "))
    balance = balance + amount
    print("New Balance:", balance)

elif choice == "3":
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")           
elif choice == "4":
        print("Thank you for using ATM!")

else:
         print("Invalid Choice")