students = []


def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def display_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("-------------------------")
        print("Roll No:", student["roll_no"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])


def search_student():
    print("\n--- Search Student ---")

    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def update_student():
    print("\n--- Update Student ---")

    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:

            print("Leave a field empty if you don't want to change it.")

            name = input("Enter new name: ")
            age = input("Enter new age: ")
            course = input("Enter new course: ")
            marks = input("Enter new marks: ")

            if name != "":
                student["name"] = name

            if age != "":
                student["age"] = int(age)

            if course != "":
                student["course"] = course

            if marks != "":
                student["marks"] = float(marks)

            print("Student updated successfully!")
            return

    print("Student not found.")


while True:

    print("\n==============================")
    print("     STUDENT MANAGEMENT")
    print("==============================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
