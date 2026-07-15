while True:
    print("\n===== File Manager =====")
    print("1. Create File")
    print("2. Read File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        filename = input("Enter file name: ")
        text = input("Enter text: ")

        file = open(filename, "w")
        file.write(text)
        file.close()

        print("File Created Successfully!")

    elif choice == "2":
        filename = input("Enter file name: ")

        try:
            file = open(filename, "r")
            print("\nFile Content:")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("File Not Found!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
