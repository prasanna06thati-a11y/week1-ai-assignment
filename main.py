from datetime import datetime

name = input("Enter your name: ")

print(f"\nHello, {name}!")

while True:
    print("\n===== MENU =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = "Study for 25 minutes and take a 5-minute break."
        print(result)

    elif choice == "2":
        result = "Success comes from consistency."
        print(result)

    elif choice == "3":
        result = str(datetime.now())
        print(result)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        result = "Invalid Choice"
        print(result)

    with open("output.txt", "a") as file:
        file.write(result + "\n")