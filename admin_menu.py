from main import auth_menu


def Admin_Menu():
    print('\n')
    text = """    
                   This Is The Admin Menu!
    
    1. Add A Student                 5. Add A Groups
    2. Delete A Student              6. Delete A Groups
    3. Update A Student              7. Update A Groups
    4. Show All Students             8. Show All Groups
  
    9. Add A Teacher                 13. Add A Subject
    10. Delete A Teacher             14. Delete A Subject
    11. Update A Teacher             15. Update A Subject
    12. Show All Teachers            16. Show All Subjects 
    
                    17. Show all lessons 

                        0. Exit"""
    print(text)
    choice = input('Enter your choice>>>> ')
    print('\n')

    while True:
        if choice == '1':

            first_name = input("Enter Student's first name: ")
            last_name = input("Enter Student's last_name: ")
            username = input("Enter Student's username: ")
            password = input("Enter Student's password: ")
            from admin import Admin
            admin_object = Admin()
            admin_object.student_create(first_name, last_name, username, password)

        elif choice == '2':

            from admin import Admin
            admin_object = Admin()
            username = input("Enter Student's username: ")
            password = input("Enter Student's password: ")
            admin_object.delete_student(username, password)


        elif choice == '9':

            first_name = input("Enter Teacher's first name: ")
            last_name = input("Enter Teacher's last_name: ")
            username = input("Enter Teacher's username: ")
            password = input("Enter Teacher's password: ")
            from admin import Admin
            admin_object = Admin()
            admin_object.create_teacher(first_name, last_name, username, password)

        elif choice == '4':

            from admin import Admin
            admin_object = Admin()
            admin_object.show_students()

        elif choice == '12':

            from admin import Admin
            admin_object = Admin()
            admin_object.show_teachers()

        elif choice == '3':
            print(f"                        Sorry, This Function Is Not Implemented\n")

        elif choice == '5':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '6':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '7':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '8':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '10':
            from admin import Admin
            admin_object = Admin()
            username = input("Enter Teacher's username: ")
            password = input("Enter Teacher's password: ")
            admin_object.delete_teacher(username, password)


        elif choice == '11':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '13':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '14':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '15':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '16':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '17':
            print("                         Sorry, This Function Is Not Implemented\n")

        elif choice == '0':
            return auth_menu()

        return Admin_Menu(), print(f"You Have Selected Non Existed Option!\n")


