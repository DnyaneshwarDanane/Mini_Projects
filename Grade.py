students = {}

def show_menu():
    print("\n--- Student Grade Manager ---")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. View Report")
    print("4. Exit")

def add_student():
    name = input("Enter student name: ")
    if name in students:
        print("Student already exists.")
    else:
        students[name] = []
        print("Student added!")

def add_marks():
    name = input("Enter student name: ")
    if name not in students:
        print("Student not found.")
        return
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            students[name].append(marks)
            print("Marks added!")
        else:
            print("Marks must be between 0 and 100.")
    except:
        print("Invalid input.")

def view_report():
    if not students:
        print("No students yet.")
        return
    for name, marks in students.items():
        if marks:
            avg = sum(marks) / len(marks)
            print(f"{name}: Marks = {marks}, Average = {avg:.2f}")
        else:
            print(f"{name}: No marks recorded.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            add_marks()
        elif choice == "3":
            view_report()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

main()
