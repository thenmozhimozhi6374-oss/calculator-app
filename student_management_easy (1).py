# Student Management System - Thenmozhi K

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        mark = input("Enter mark: ")
        students.append({"name": name, "mark": mark})
        print("Student added!")

    elif choice == "2":
        if students == []:
            print("No students!")
        else:
            for s in students:
                print(f"Name: {s['name']} | Mark: {s['mark']}")

    elif choice == "3":
        print("Bye!")
        break
