# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Jay VanderZanden, 2/19/2026, Finished Script
# ------------------------------------------------------------------------------------------ #

# TODO: Import the json
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)

    # From the Original file but not needed
    # for row in file.readlines():
    #     # Transform the data from the file
    #     student_data = row.split(',')
    #     student_data = [student_data[0], student_data[1], student_data[2].strip()]
    # Load it into our collection (list of lists)
    # students.append(student_data)
    
except FileNotFoundError as e:
    print("File not found!")
    print(f"Error: {e}" )
except Exception as e:
    print("General error!")
    print(f"Error: {e}")
finally:
    # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()




# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")

            # Checks if there is a number in with the name
            if not student_first_name.isalpha():

                # Raises a value error as the only error here we wish to trap is value related
                raise ValueError("Student first name must be alphabetical")
            student_last_name = input("Enter the student's last name: ")

            # Checks if there is a number in with the name
            if not student_last_name.isalpha():

                # Raises a value error as the only error here we wish to trap is value related
                raise ValueError("Student last name must be alphabetical")

            #adds student information to the dictionary variable
            course_name = input("Please enter the name of the course: ")

            # creates keys and assigns input variables to their respective keys
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}

            #adds the dictionary to the list variable
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            print(e)
            print(type(e))  # Print the type of the exception object
        except Exception as e:
            print(f"Error: {e}")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'Student {student["FirstName"]}'
                  f' {student["LastName"]} is enrolled in {student["CourseName"]}')

            # From the Original file but not needed
            # print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:

        #   Opens the file
            file = open(FILE_NAME, "w")

        #   Puts the list of dictionaries into the json file
            json.dump(students, file, indent=2)

        # If the file can't be found, this block will run
        except FileNotFoundError as e:
            print("File not found!")
            print(f"Error: {e}" )

        # If an error other than a File Not Found error happens, this block will run
        except Exception as e:
            print("General error!")
            print(f"Error: {e}")

        # Check if a file object exists and is still open
        finally:
            if file is not None and file.closed == False:
                file.close()

        # Print statement saying which information is being saved to the file
        print("The following data was saved to file!")
        for student in students:
            print(f'Student {student["FirstName"]}'
                  f' {student["LastName"]} is enrolled in {student["CourseName"]}')

            # From the Original File
            # print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
