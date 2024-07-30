import json
from teacher_menu import Teacher_Menu
from main import auth_menu


class Teacher:

    def __init__(self):
        pass

    def teacher_login(self, login_username, login_password):

        with open('../hemisproject/data/teachers.json', 'r') as json_file:
            teacher_data = json.load(json_file)

        is_login = False
        for user in teacher_data['teacher_users']:
            if login_username == user['login_username'] and login_password == user['login_password']:
                is_login = True
                break

        if is_login:

            print("You Have Logged In Successfully\n")
            return Teacher_Menu()

        else:
            return auth_menu()

    def logout(self):
        pass

    def show_active_lessons(self):
        pass

    def start_lesson(self, lesson_id):
        pass

    def grade_student(self, student_id, grade):
        pass

    def show_ended_lessons(self):
        pass

