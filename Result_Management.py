student_set = set()

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    roll = input("Enter Roll No: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    student = (roll, name, course, branch, marks)
    student_set.add(student)
    print("Student details stored successfully!")

def search_recursive(student_list, roll):
    if not student_list:
        return None
    
    student = student_list[0]
    if student[0] == roll:
        return student
    
    return search_recursive(student_list[1:], roll)

def show_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll No to search: ")
    
    student_list = list(student_set)
    student = search_recursive(student_list, roll)
    
    if student:
        print("\nStudent Details Found:")
        print("Roll No:", student[0])
        print("Name   :", student[1])
        print("Course :", student[2])
        print("Branch :", student[3])
        print("Marks  :", student[4])
    else:
        print("Student not found!")

def menu():
    print("\n--- Menu ---")
    print("1. Add Student")
    print("2. Search Student by Roll No")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        add_student()
        menu()
    elif choice == '2':
        show_student()
        menu()
    elif choice == '3':
        print("Exiting program.")
    else:
        print("Invalid choice! Please try again.")
        menu()

menu()
