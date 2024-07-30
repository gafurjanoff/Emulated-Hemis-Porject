import json
from student_menu import Student_Menu
from main import auth_menu
class Student:
    def __init__(self):
        pass

    def student_login(self, login_username, login_password):
        with open('../hemisproject/data/students.json', 'r') as json_file:
            student_data = json.load(json_file)

        is_login = False
        for student in student_data['student_users']:
            if login_username == student['login_username'] and login_password == student['login_password']:
                is_login = True
                break

        if is_login:

            print("You Have Logged In Successfully")
            return Student_Menu()
        else:
            return auth_menu()

    def show_lessons(self):
        pass

    def show_grades(self):
        pass

    def show_subjects(self):
        pass

    def show_subjects_grades(self):
        pass
