# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions & classes
# with structured error handling
# Change Log: (Who, When, What)
#   IB,5/20/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json


MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''

FILE_NAME: str = 'Enrollments.json'

menu_choice: str = ''  # Hold the choice made by the user.
students: list = []  # a table of student data


class FileProcessor:
    """
    This class manages user input and output
    IB, 5/21/2024, Created Class
    IB, 5/22/2024, Updated CLass
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        # Extract the data from the file

        file = None

        try:
            file = open(file_name, "r")
            student_data += json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed is False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # Write data to the file

        file = None

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed is False:
                file.close()


class IO:
    """
    This class manages user input and output
    IB, 5/21/2024, Created Class
    IB, 5/22/2024, Updated Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        # Displays a custom error message

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        print()
        print(menu)
        print()
        return menu_choice

    @staticmethod
    def input_menu_choice():
        # Present the menu of choices

        global menu_choice
        menu_choice = input("Please enter your choice: ")

        try:
            if menu_choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list) -> None:
        # Present the current data

        for student in student_data:
            print(f"{student['FirstName']} {student['LastName']} {student['CourseName']}")

    @staticmethod
    def input_student_data(student_data: list):
        # Input user data

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("THere was a non-specific error!", e)
        return student_data


students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:

    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)

    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break

    else:
        print()
        print("Please select a valid option")
        print()
        continue

print("Program Ended")


