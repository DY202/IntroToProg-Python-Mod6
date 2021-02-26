# --------------------------------------------------------------------------------------#
# Title: Assignment 06
# Description: Working with functions in a class,
#                When the program starts, load each "row" of data
#                in "ToDoList.TXT" INTO A python dictionary.
#                Add the each dictionary "ro" to a python list "table"
# ChangeLog (Who, When ,What)
# RRoot, 1.1.2030. Created started script
# RRoot, 1.1.2030, Added code to complete assignment 5
# Deborah Yenubari, 2.22.2021, Modifies code to complete assignment 6
# ----------------------------------------------------------------------------------------#


# Data-----------------------------------------------------------------------------------#
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary{Task, Priority}
lstTable = []  # A list that acts as a "table"of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user Task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing ---------------------------------------------------------------------------#
class Processor:
    """ Performs processing tasks """

    @staticmethod
    def read_data_from_file(strFileName, list_of_rows):
        """ Reads data from a file into a list of dictionary rows
        :param strFileName: (string)with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """

        list_of_rows.clear()
        file = open("ToDoFile.txt", "r")
        for line in file:
            data = line.split(",")
            dicRow = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_rows.append(dicRow)
        file.close()
        print("Success!")
        return list_of_rows

    @staticmethod
    def add_data_to_list(strTask, strPriority, list_of_rows):
        strTask = input("Enter a task to add: ")
        strPriority = input("Enter its priority level: ")
        #  task = strTask
        #  priority = strPriority
        dicRow = {"Task": strTask.strip(), "Priority": strPriority.strip()}
        list_of_rows.append(dicRow)
        print("Success!")
        return list_of_rows

    @staticmethod
    def remove_data_from_list(strTask, list_of_rows):
        strTask = input("Enter a Task to delete: ").strip()
        for dicRow in list_of_rows:
            if dicRow["Task"] == strTask:
                list_of_rows.remove(dicRow)
                print("Success!")
                return list_of_rows

    @staticmethod
    def write_data_to_file(strFileName, list_of_rows):
        file = open("ToDoFile.txt", "a")
        for dicRow in list_of_rows:
            file.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        file.close()
        list_of_rows.append(dicRow)
        print("Data saved to file!")
        return list_of_rows


# Presentation (Input/Output)-----------------------------------------------------------#
class IO:
    """Performs Input and Output tasks"""

    @staticmethod
    def print_menu_Tasks():
        """ Displays a menu of choices to the user
        :return: nothing
        """
        print("""
        Menu of Options
        1. Add a New Task
        2. Remove an existing Task
        3. Save Data to File
        4. Reload Data from File
        5. Exit Program
        """)

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform?( 1 to 5)-")).strip()
        print("-------------------------------------------------\n")
        return choice

    @staticmethod
    def print_current_Tasks_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("**********The current Tasks TO DO are:**********")
        for row in list_of_rows:
            print(row["Task"] + "(" + row["Priority"] + ")")
            print("***************************************")
            print()

    @staticmethod
    def input_yes_no_choice(message):
        """Gets a yes or no choice from the user
        :return:string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing
        :param optional_message: An optional message you want to display
        :return:nothing
        """
        print(optional_message)
        input("Press the [Enter] key to continue.")

    # @staticmethod
    # def input_new_task_and_priority():
    #     pass
    #     #  strTask = input("Enter a task to add: ")
    #     #  strPriority = input("Enter its priority level: ")
    #     return strTask, strPriority

    # @staticmethod
    # def input_task_to_remove():
    #     pass
    #     # strTask = input("Enter a Task to delete: ").strip()
    #     return strTask


# Main Body of Script------------------------------------------------#
# Step 1 - When the program starts, Load data from ToDoFile.txt
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.print_current_Tasks_list(lstTable)  # Show current data in the list/Table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == "1":  # Add a new Task
        #  IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask, strPriority, lstTable)  # Add Code here
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == "2":  # Remove an existing Task
        #  IO.input_task_to_remove()
        Processor.remove_data_from_list(strTask, lstTable)  # Add Code here
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == "3":  # Save Data to File
        strChoice = IO. input_yes_no_choice("Save this Data to File? (y/n) -")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)  # Add Code here
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue(strStatus)
        continue  # Add code here

    elif strChoice == "4":  # Reload Data from File
        print("Warning : Unsaved Data will be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.read_data_from_file(strFileName, lstTable)  # Add code here
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled")
        continue  # to show the menu

    elif strChoice == "5":  # Exit the program
        print("Goodbye")
        break  # Exit


