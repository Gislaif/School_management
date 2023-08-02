class Student:
    def __init__(self, first_name, last_name, class_name):
        self.first_name = first_name
        self.last_name = last_name
        self.class_name = class_name

class Teacher:
    def __init__(self, first_name, last_name, subject, classes_taught):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.classes_taught = classes_taught

class HomeroomTeacher:
    def __init__(self, first_name, last_name, class_lead):
        self.first_name = first_name
        self.last_name = last_name
        self.class_lead = class_lead

students_g = []
teachers_g = []
homeroom_teachers_g = []

# creating student
def create_student():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    class_name = input("Enter student's class name: ")
    student = Student(first_name, last_name, class_name)
    students_g.append(student)
    print("student created successfully!")

# creating a teahcer
def create_teacher():
    first_name = input("Enter teacher's first name: ")
    last_name = input("Enter teacher's last name: ")
    subject = input("Enter teacher's subject: ")
    classes_taught = []
    while True:
        class_name = input("Enter the class name the teacher teaches (or leave empty to finish): ")
        if not class_name:
            break
        classes_taught.append(class_name)
    teacher = Teacher(first_name, last_name, subject, classes_taught)
    teachers_g.append(teacher)

# creating a homeroom teacher
def create_homeroom_teacher():
    first_name = input("Enter homeroom teacher's first name: ")
    last_name = input("Enter homeroom teacher's last name: ")
    class_lead = input("Enter the class name the teacher leads: ")
    homeroom_teacher = HomeroomTeacher(first_name, last_name, class_lead)
    homeroom_teachers_g.append(homeroom_teacher)

# managing classes
def manage_class():
    class_name = input("Enter the class name to display: ")
    print("\nStudents in class", class_name, ":")
    for student in students_g:
        if student.class_name == class_name:
            print(student.first_name, student.last_name)

    print("\nHomeroom teacher for class", class_name, ":")
    for homeroom_teacher in homeroom_teachers_g:
        if homeroom_teacher.class_lead == class_name:
            print(homeroom_teacher.first_name, homeroom_teacher.last_name)

# managing students
def manage_student():
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    print("\nClasses attended by", first_name, last_name, ":")
    for student in students_g:
        if student.first_name == first_name and student.last_name == last_name:
            for teacher in teachers_g:
                if student.class_name in teacher.classes_taught:
                    print(student.class_name, "taught by", teacher.first_name, teacher.last_name)

# managing teachers
def manage_teacher():
    first_name = input("Enter teacher's first name: ")
    last_name = input("Enter teacher's last name: ")
    print("\nClasses taught by", first_name, last_name, ":")
    for teacher in teachers_g:
        if teacher.first_name == first_name and teacher.last_name == last_name:
            for class_name in teacher.classes_taught:
                print(class_name)

# managing homeroom teachers
def manage_homeroom_teacher():
    first_name = input("Enter homeroom teacher's first name: ")
    last_name = input("Enter homeroom teacher's last name: ")
    print("\nStudents led by", first_name, last_name, ":")
    for homeroom_teacher in homeroom_teachers_g:
        if homeroom_teacher.first_name == first_name and homeroom_teacher.last_name == last_name:
            for student in students_g:
                if student.class_name == homeroom_teacher.class_lead:
                    print(student.first_name, student.last_name)

def main():
    while True:
        print("\nAvailable commands: create, manage, end")
        command = input("Enter a command: ")

        if command == 'create':
            print("\nUser types: student, teacher, homeroom teacher, end")
            user_type = input("Enter a user type to create: ")

            if user_type == 'student':
                create_student()
            elif user_type == 'teacher':
                create_teacher()
            elif user_type == 'homeroom teacher':
                create_homeroom_teacher()
            elif user_type == 'end':
                continue
            else:
                print("Invalid user type. Please try again.")

        elif command == 'manage':
            print("\nOptions to manage: class, student, teacher, homeroom teacher, end")
            option = input("Enter an option to manage: ")

            if option == 'class':
                manage_class()
            elif option == 'student':
                manage_student()
            elif option == 'teacher':
                manage_teacher()
            elif option == 'homeroom teacher':
                manage_homeroom_teacher()
            elif option == 'end':
                continue
            else:
                print("Invalid option. Please try again.")

        elif command == 'end':
            print("Program terminated.")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()