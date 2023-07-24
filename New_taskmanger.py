#=== Reg_user Function ===#
# Is called when the user selects ‘r’ to register a user.
from datetime import datetime

def reg_user () :
    # This while loop is checking if the username entered by the user is not a duplicate.
    while True: 
        new_user = input("Please enter a username: ")
        if new_user in user_data: 
            print(f"\nThis Username already in use! Please try again.\n")
           
        else :
            print(f"Thank you {new_user}!\n")
            break

    # This is a while loop that will run until the password is confirmed.
    new_passwd = input("Please enter a password: ")
    passwd_confirm = input("Please confirm your password: ") 

    while new_passwd != passwd_confirm :                        
        print("Incorrect Password ")
        passwd_confirm = input("Please confirm your password: ")
        
    else:
            print(f"""\nPassword Confirmed! {new_user} has been registered!
Please find the Menu below to perfom futher actions.\n""") 

    # Open the file user.txt with the "r+" access modifier to read and apply changes to user.txt file.
    with open("user.txt","r+") as f_users :
        logins = f_users.readlines()
        f_users.write(f"\n{new_user}, {passwd_confirm}")    


#=== Add_task Function ===#
# Is called when a user selects ‘a’ to add a new task.
def add_task () : 
        assigned_user = input("\nPlease enter the username you would like to assign a task to: ")
        task_title = input("Please enter the title of the task you would like to assign: ")
        task_description = input("Please enter a brief desciption of the task: ")
        task_due = input("Please enter the task due date e.g(10 Feb 2013): ")
        current_date = input("Please enter the current date e.g(10 Feb 2013): ")
        print(f"""\nTask: {task_title} - has sucessfully been assigned to: {assigned_user}!
Please find the Menu below to perfom futher actions.\n""")

        # Opening the tasks.txt file and writing the information to the file.
        with open("tasks.txt","r+") as f_users :
            logins = f_users.readlines()
            f_users.write(f"\n{assigned_user}, {task_title}, {task_description}, {task_due}, {current_date}, No ")


#=== View_all Function ===#
# Is called when users type ‘va’ to view all the tasks listed in ‘tasks.txt’.
def view_all () :
        # This is opening the tasks.txt file and reading the data in the file.
        with open("tasks.txt","r") as task_files :
            for data in task_files :
                tasks_list = data.strip("\n").split(", ")
                print(f'''\nTask:\t\t\t\t {tasks_list[1]}
Assigned To:\t\t\t {tasks_list[0]}
Date Assigned:\t\t\t {tasks_list[3]}
Due Date:\t\t\t {tasks_list[4]}
Task Complete?\t\t\t {tasks_list[5]}
Task Description:\t\t {tasks_list[2]}\n''')


#=== View_mine Function ===#
# Is called when users type ‘vm’ to view all the tasks that have been assigned to them.
def view_mine () :
        # This is creating a dictionary that will store the task number and the task details.
        task_counter = 0
        task_dictionary = {}

        with open("tasks.txt","r") as task_files :
            task_flag = True
            for data in task_files :
                tasks_list = data.strip("\n").split(", ")
                task_counter += 1
                task_dictionary[task_counter] = tasks_list
                if tasks_list[0] == loggedin_name:
                    task_flag = False
                    print(f'''\nTask:\t\t\t\t {tasks_list[1]}
Assigned To:\t\t\t {tasks_list[0]}
Task Number:\t\t\t {task_counter}
Date Assigned:\t\t\t {tasks_list[3]}
Due Date:\t\t\t {tasks_list[4]}
Task Complete?\t\t\t {tasks_list[5]}
Task Description:\t\t {tasks_list[2]}\n''')

            if task_flag:
                print("\nYou Currently have no tasks assigned to you. Please check again later.\n")

        # This is a while loop that is asking the user to select a task number from the list of tasks that are assigned to them.
        while True :
            select_task = int(input("\nPlease enter the Task Number of the task you would like to select or else input ‘-1’ to return to the main menu.\n: "))
            if select_task == -1:
                break
            else:
                temp_list = task_dictionary[select_task]
                option_menu = input("""\nPlease Select an option from the menu below: 
To Mark your selected task as complete enter:\t'm'
To Edit your selected task please enter:\t'e'\n
: """).lower()

                # This is a menu that is displayed to the user to select one of the options to perform a task.
                if option_menu == 'm':
                    if temp_list[5] == "Yes" :
                        print("\nThis task has already been marked as complete.")
                    else:
                        temp_list[5] = "Yes"
                        print("\nYour selected task has been markerd as complete! ")
            
                elif option_menu == 'e' :
                    if temp_list[5] == "Yes" :
                        print("\nThis task cannot be edited as it has already been completed.\n")
                        
                    else:
                        username_edit = input("Please enter the new username you would like to edit the selected task to: ")
                        temp_list[0] = username_edit
                        date_edit = input("Please ennter the new due date you would like to edit the selected task to: ")
                        temp_list[4] = date_edit

        with open("tasks.txt", "w") as write_file:
            # [write_file.write(", ".join(x)+ "\n") for x in task_dictionary.values()]
            # This is a list comprehension that is writing the values of the task_dictionary to the tasks.txt file.
            for line in task_dictionary.values():
                string_line = ", ".join(line) + "\n"
                write_file.write(string_line)   



#==== Generate Reports ====#
# When the user chooses to generate reports, two text files, called task_overview.txt and user_overview.txt, should be generated.

def gen_report () :
#==== Task Overview ====#
    # This is creating a variable that will store data from tasks.txt file
    total_task = 0
    complete_task = 0
    incomplete_task = 0
    overdue_tasks = 0 
    
    # Opening the tasks.txt file and reading the data in the file.
    with open ("tasks.txt", "r") as read_task :  
            for data in read_task :
                task_list = data.strip("\n").split(", ")
                total_task += 1

               # Checking if the task is complete or not.
                if task_list[5].strip() == 'Yes' :
                        complete_task += 1
                
                elif task_list[5].strip() == 'No' :
                        incomplete_task += 1

                # Converting the date from the tasks.txt file to a datetime object.
                converted_due_date = datetime.strptime(task_list[3], "%d %b %Y")
                current_date = datetime.today()

                # Checking if the current date is greater than the due date and if the task is incomplete.
                if current_date > converted_due_date and task_list[5] == "No":
                        overdue_tasks += 1
                
                # Calculating the percentage of incomplete tasks and overdue tasks.
                percentage_incomplete = (incomplete_task / total_task) * 100
                percentage_overdue = (overdue_tasks / total_task) * 100

    # This is opening the task_overview.txt file and writing the statistics of the tasks.txt file to the task_overview.txt file.
    with open ("task_overview.txt","w") as report_file : 
        report_file.write(f"""Total number of tasks: {total_task}
Total number of complete_tasks: {complete_task}
Total number of incomplete tasks: {incomplete_task}
Total number of incomplete task and overdue tasks: {overdue_tasks}
Percentage of incomplete tasks: {percentage_incomplete}%
Percentage of overdue tasks: {percentage_overdue}%""")



#===== User Overview =====#
    total_users = 0
    # Opening the user.txt and tasks.txt files and reading the lines in the files.
    with open ("user.txt", "r") as read_users :  
        with open ('tasks.txt', 'r') as read_task :
            read_users_list = read_users.readlines()
            read_tasks_list = read_task.readlines()

            # The above code is calculating the total number of users and tasks.
            output_statement = f"Total number of registered users:\t{len(read_users_list)}\n"\
                               f"Total number of tasks:\t\t\t\t{len(read_tasks_list)}"

            # Reading the users_list.txt file and splitting the data into a list.
            for data in read_users_list :
                user_list = data.strip("\n").split(", ")
                total_users += 1
                total_task_forUser = 0
                complete_task_perecentage = 0
                incomplete_task_percentage = 0
                user_percentage_complete = 0
                user_percentage_incomplete = 0
                overdue_task_percentage = 0
                user_percentage_overdue = 0

                # Reading the file and counting the number of tasks for each user.
                for task_data in read_tasks_list :
                    user_task = task_data.strip("\n").split(", ")  
                    if user_list[0] == user_task[0] :
                        total_task_forUser += 1


#==== Percentage Calculations ====#
                        # Checking if the user has completed the task or not. 
                        if user_task[5].strip("\n").strip() == 'Yes' :
                            complete_task_perecentage += 1
                        
                        elif user_task[5].strip("\n").strip() == 'No' :
                            incomplete_task_percentage += 1

                            #Converting the due date into a date format that can be compared to the current date.
                            converted_due_date = datetime.strptime(user_task[3], "%d %b %Y")
                            current_date = datetime.today()
                            # print(converted_due_date)
                            # Checking if the current date is greater than the due date and if the task is incomplete.
                            if current_date > converted_due_date:
                                overdue_task_percentage += 1
                    
                # Calculating the percentage of incomplete tasks and overdue tasks.
                if total_task_forUser != 0:
                    
                    user_percentage_complete = (complete_task_perecentage / total_task_forUser) * 100
                    user_percentage_incomplete = (incomplete_task_percentage / total_task_forUser) * 100
                    user_percentage_overdue = (overdue_task_percentage / total_task_forUser ) * 100


                output_statement += f"\n\nTasks for {user_list[0]}:\n"\
                                    f"Tasks assigned to user: {(total_task_forUser)}\n"\
                                    f"Total percentage of the tasks completed assigned to user : {user_percentage_complete}\n"\
                                    f"Total percentage of the tasks incompleted assigned to user: {user_percentage_incomplete}\n"\
                                    f"Total percentage of the tasks overdue assigned to user: {round(user_percentage_overdue, 2)}"
        
            print("\nReport Generated! Please find the Menu below to perfom futher actions.\n")

            with open("user_overview.txt", "w") as write_file:
                write_file.write(output_statement)


#==== Dispaly Statistics ====#
# Provide The admin user with a menu option that displays The total number of tasks and the total number of users.
# Create a variable that acts as a counter intialized to zero.
def display_stats () :

    with open ("task_overview.txt", "r") as user_overview_file :  
        with open ('user_overview.txt', 'r') as task_overview_file :
            display_users_overview = user_overview_file.read()
            display_tasks_overview = task_overview_file.read()
            print(display_users_overview)
            print(display_tasks_overview)



#=== Open File ===#
# Reading the user.txt file and storing the data in a dictionary.
user_data = {}  
with open("user.txt","r") as f_users :
    logins = f_users.readlines()

    # Reading the user.txt file and storing the data in a dictionary.
    for data in logins:
        datalist = data.strip("\n").split(", ")
        user_data[datalist[0]] = datalist[1]



#==== Login Section ====#
# This section of the program is checking if the username and password entered by the user is valid.
# Create a Global variable to store the usernames of the users when they login.
loggedin_name = ""
username_input = None     

# This while loop is checking if the username and password entered by the user is valid.
while True: 
    username_input = input("Please enter your username: ")
    if username_input in user_data: 
        print(f"Thank you {username_input}!")
        loggedin_name = username_input
        break
    else:
        print("Invalid username! ")

while True:
    password_input = input("Please enter your password: ")
    if password_input == user_data[username_input]: 
        print(f"Thank you {username_input}! \n ")
        break
    else:
	    print("Invalid password! ")



#==== Menu Section ====#
# This is a menu that is displayed to the user to select one of the options to perform a task.
# Use an if statement to validate that only, the applicable menu is shown for the appropriate user.
while True:
    if loggedin_name == "admin" :
        menu = input('''Select one of the following Options below:
r  - Registering a user
a  - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display Statistics.
e  - Exit
: ''').lower()

    else:
        menu = input('''Select one of the following Options below:
a  - Adding a task
va - View all tasks
vm - View my task
e  - Exit
: ''').lower()



# Menu that allows the user to select from a list of options.
    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
    
    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr' :
        gen_report()
    
    elif menu == 'ds' :
        display_stats()
        
#==== Exit Section ====#
# This block of code will allow the user to exit the menu.
# Create a default for any invalid entries the user might enter in the menu.
    elif menu == 'e':
        print('\nGoodbye!!!\n')
        exit()

    else:
        print("\nInvalid Entry! Please read the menu carefully and Try again\n")