import json
from admin_menu import Admin_Menu
from main import auth_menu

file_path = '../hemisproject/data/teachers.json'


class Admin:

    def __init__(self):
        pass

    def admin_login(self, login_username, login_password):

        with open('../hemisproject/data/admins.json', 'r') as json_file:
            admin_data = json.load(json_file)

        is_login = False
        for admin in admin_data['admin_users']:
            if login_username == admin['login_username'] and login_password == admin['login_password']:
                is_login = True
                break

        if is_login:
            print('\n')
            print("                  You Have Logged In Successfully")
            print('\n')

            return Admin_Menu()
        else:
            print(f"                We couldn\'t find you details")
            return auth_menu()

    def admin_log_out(self):
        pass

    def show_lesson_table(self):
        pass

    def create_subject(self):
        pass

    def read_subject(self):
        pass

    def update_subject(self):
        pass

    def delete_subject(self):
        pass

    def give_teacher_details(self, first_name, last_name):

        with open(file_path, 'r') as read_file:
            teacher_data = json.load(read_file)

        fullname = first_name + " " + last_name
        teacher_found = False

        for teacher in teacher_data['teacher_users']:
            if first_name == teacher["first_name"] and last_name == teacher["last_name"]:
                print('Teacher Found!\n')
                full_name = teacher['first_name'] + ' ' + teacher['last_name']
                login_password = teacher['login_password']
                login_username = teacher['login_username']
                teacher_found = True

                break

        if not teacher_found:
            print(f"Dear {fullname}, We couldn't find your login details. "
                  f"Please try again or ask Admin to give your details!\n")
            return None, None, None

        return login_username, login_password, full_name

    def create_teacher(self, first_name, last_name, username, password):

        with open('../hemisproject/data/teachers.json', 'r') as read_file:
            teacher_data = json.load(read_file)

            teacher_found = False
            for teacher in teacher_data["teacher_users"]:

                if username == teacher["login_username"] and password == teacher["login_password"]:
                    teacher_found = True
                    print(f"Login Password and UserName Already Existed!"
                          f"Please Choose Another Username And Password.\n")
                    break
            if not teacher_found:

                teacher_file = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "login_username": username,
                    "login_password": password
                }

                file_path = '../hemisproject/data/teachers.json'
                teacher_data['teacher_users'].append(teacher_file)
                with open(file_path, 'w') as write_file:
                    json.dump(teacher_data, write_file, indent=4)

            else:
                print("Please Use Another Login Password and Username\n")
                return Admin_Menu()

    def show_teachers(self):

        with open(file_path, 'r') as read_file:
            teacher_data = json.load(read_file)

            id_num = 1
            for student in teacher_data["teacher_users"]:
                print(f"""
                        Teacher ID: {id_num}
                        Teacher Name: {student['first_name']}
                        Teacher Surname: {student['last_name']}
                        Teacher Username: {student['login_username']}
                        Teacher Password: {student['login_password']}""")
                id_num += 1

    def update_teacher(self):
        pass

    def delete_teacher(self, username, password):

        with open(file_path, 'r') as read_file:
            teacher_data = json.load(read_file)

        teacher_removed = False
        for teacher in teacher_data["teacher_users"]:
            if teacher['login_username'] == username and teacher['login_password'] == password:
                teacher_data['teacher_users'].remove(teacher)
                full_name = teacher['first_name'] + " " + teacher['last_name']
                teacher_removed = True
                break

        if teacher_removed:
            with open(file_path, 'w') as write_file:
                json.dump(teacher_data, write_file, indent=4)
            print(f"{full_name} has been removed!")
        else:
            print("This teacher is not in the list!")
            return Admin_Menu()

    def give_student_detail(self, first_name, last_name):

        with open('../hemisproject/data/students.json', 'r') as read_file:
            student_data = json.load(read_file)

        fullname = first_name + " " + last_name
        student_found = False
        student_details = list()

        for student in student_data['student_users']:
            if first_name == student["first_name"] and last_name == student["last_name"]:
                print('Student Found!\n')
                full_name = student['first_name'] + ' ' + student['last_name']
                login_password = student['login_password']
                login_username = student['login_username']
                student_found = True

                break

        if not student_found:
            print(f"Dear {fullname}, We couldn't find your login details. "
                  f"Please try again or ask Admin to give your details!\n")
            return None, None, None

        return login_username, login_password, full_name

    def student_create(self, first_name, last_name, username, password):

        with open('../hemisproject/data/students.json', 'r') as read_file:
            student_data = json.load(read_file)

            student_found = False
            for student in student_data["student_users"]:

                if username == student["login_username"] and password == student["login_password"]:
                    student_found = True
                    print(f"Login Password and UserName Already Existed!"
                          f"Please Choose Another Username And Password.\n")
                    break
            if not student_found:

                student_file = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "login_username": username,
                    "login_password": password
                }

                file_path = '../hemisproject/data/students.json'
                student_data['student_users'].append(student_file)
                with open(file_path, 'w') as write_file:
                    json.dump(student_data, write_file, indent=4)

            else:
                print("Please Use Another Login Password and Username\n")
                return Admin_Menu()

    def show_students(self):

        with open('../hemisproject/data/students.json', 'r') as read_file:
            student_data = json.load(read_file)

            number = 1
            for student in student_data["student_users"]:
                print(f"""
                        Student ID: {number}
                        Student Name: {student['first_name']}
                        Student Surname: {student['last_name']}
                        Student Username: {student['login_username']}
                        Student Password: {student['login_password']}""")
                number += 1

    def update_student(self):
        pass

    def delete_student(self, username, password):

        with open('../hemisproject/data/students.json', 'r') as read_file:
            student_data = json.load(read_file)

        student_removed = False
        for student in student_data["student_users"]:
            if student['login_username'] == username and student['login_password'] == password:
                student_data['student_users'].remove(student)
                full_name = student['first_name'] + " " + student['last_name']
                student_removed = True
                break

        if student_removed:
            with open('../hemisproject/data/students.json', 'w') as write_file:
                json.dump(student_data, write_file, indent=4)
            print(f" {full_name} has been removed!")

        else:
            print("This student is not in the list!")
            return Admin_Menu()
