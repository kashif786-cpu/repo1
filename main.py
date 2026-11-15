
class Student:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)



students = []



def add_student():
    roll_no = int(input("Enter roll number: "))

    
    for student in students:
        if student.roll_no == roll_no:
            print("Roll number already exists!")
            return

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    student = Student(roll_no, name, age, marks)
    students.append(student)

    print("Student added successfully!")



def view_students():
    if len(students) == 0:
        print("No students found!")
    else:
        for student in students:
            student.display()



def search_student():
    roll = int(input("Enter roll number to search: "))

    for student in students:
        if student.roll_no == roll:
            print("Student found!")
            student.display()
            return

    print("Student not found!")



def delete_student():
    roll = int(input("Enter roll number to delete: "))

    for student in students:
        if student.roll_no == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")



def update_student():
    roll = int(input("Enter roll number: "))

    for student in students:
        if student.roll_no == roll:
            new_marks = float(input("Enter new marks: "))
            student.marks = new_marks

            print("Marks updated successfully!")
            return

    print("Student not found!")



while True:
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")

