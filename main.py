def display_menu():
    text = """
     
                  Welcome to our emulated hemisproject project\n

Please choose your role in the following options:

                    1. Admin
                    2. Teacher
                    3. Student 
                    0. Exit Program\n"""
    print(text)
    role = input("Your role >>>>>>>>>>: ")
    print('\n')
    return role


def auth_menu():
    while True:

        role = display_menu()

        if role == '1':

            text = """
                                    Have you logged in before?\n
                                    1. Yes
                                    2. No \n
            """
            print(text)
            input_logged = input('Enter your reponse >>> ')

            if (input_logged == '1') or (input_logged == 'Y') or (input_logged == 'Yes') or (input_logged == 'yes') or (
                    input_logged == 'y') or (input_logged == 'YES'):
                from admin import Admin
                admin_object = Admin()
                login_username = input("Enter your login username >>>> ")
                login_password = input("Enter your login password >>>> ")
                print('\n')
                admin_object.admin_login(login_username, login_password)

            elif (input_logged == '2') or (input_logged == 'N') or (input_logged == 'No') or (input_logged == 'no') or (
                    input_logged == 'n') or (input_logged == 'NO'):
                print("We couldn\'t find you details. It seems You Are Not An Admin)")
            else:
                return auth_menu()

        elif role == '2':

            text = """
                    Have you logged in before?\n
                    1. Yes
                    2. No \n
                        """
            print(text)
            input_logged = input('Enter your reponse >>> ')

            if (input_logged == '1') or (input_logged == 'Y') or (input_logged == 'Yes') or (input_logged == 'yes') or (
                    input_logged == 'y') or (input_logged == 'YES'):
                from teacher import Teacher
                teacher_object = Teacher()
                login_username = input("Enter your login username >>>> ")
                login_password = input("Enter your login password >>>> ")
                print('\n')
                teacher_object.teacher_login(login_username, login_password)

            elif (input_logged == '2') or (input_logged == 'N') or (input_logged == 'No') or (input_logged == 'no') or (
                    input_logged == 'n') or (input_logged == 'NO'):
                from admin import Admin
                admin_object = Admin()
                print(f"       To Get Your Login details from Admin!\n")
                print(f"       Please Enter Your Full Name!\n")
                first_name = input("Enter your first name >>>> ")
                last_name = input("Enter your last name >>>> ")
                print('\n')
                username, password, fullname = admin_object.give_teacher_details(first_name, last_name)
                if username is not None or password is not None or fullname is not None:
                    print(f"        Dear {fullname}, you are now logged in!\n")
                    print(f"        Here are your login details for Hemis: ")
                    print('\n')
                    print(f"                       Login_UserName: {username}\n")
                    print(f"                       Login_Password: {password}")
                else:
                    continue
            elif input_logged == '0':
                exit()

            return auth_menu()

        elif role == '3':
            text = """
                    Have you logged in before?\n
                    1. Yes
                    2. No \n
                                    """
            print(text)
            input_logged = input('Enter your reponse >>> ')
            print('\n')

            if (input_logged == '1') or (input_logged == 'Y') or (input_logged == 'Yes') or (input_logged == 'yes') or (
                    input_logged == 'y') or (input_logged == 'YES'):
                from student import Student
                student_object = Student()
                login_username = input("Enter your login username >>>> ")
                login_password = input("Enter your login password >>>> ")
                print('\n')
                student_object.student_login(login_username, login_password)

            elif (input_logged == '2') or (input_logged == 'N') or (input_logged == 'No') or (input_logged == 'no') or (
                    input_logged == 'n') or (input_logged == 'NO'):
                from admin import Admin
                admin_object = Admin()
                print(f"       To Get Your Login details from Admin!\n")
                print(f"       Please Enter Your Full Name!\n")
                first_name = input("Enter your first name >>>> ")
                last_name = input("Enter your last name >>>> ")
                print('\n')

                username, password, fullname = admin_object.give_student_detail(first_name, last_name)
                if username is not None or password is not None or fullname is not None:
                    print(f"        Dear {fullname}, you are now logged in!\n")
                    print(f"        Here are you login details for Hemis: ")
                    print('\n')
                    print(f"                       Login_UserName: {username}\n")
                    print(f"                       Login_Password: {password}")

                continue
            else:

                return auth_menu()
        else:
            print("You Have Selected Non Existed Role")


if __name__ == '__main__':
    auth_menu()
