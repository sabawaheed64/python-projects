contacts = {}

while True:
    print("\n===== Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact Added Successfully!")

    elif choice == "2":
        if contacts:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No Contacts Found.")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
