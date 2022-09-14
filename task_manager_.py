import math
from datetime import date

#------------------------------------------------LOGIN------------------------------------------------#

print("\n------------------------------------------------------------------------------\n")

#Open users.txt file as a read-only file, where the handle is positioned at the beginning of the file. This is also the default mode in which a file is opened.

user_list = open("users.txt", "r+")

#Use the readlines() function to read through each line in the file
#This returns each line as a list item

find_user = user_list.readlines()

#Set empty lists for users and passwords so that we can index each element
#This allows for the computer to search through each user and password
#Set an empty variable that stores which user has logged in

users = []
passwords = []
user_name  = ""

#Use a for for loop to run through each element of the file 
#For each line in the users.txt file use the split()function to split strings into a list 
#Set the position for users in the list as[0]
#Set the positin for the passwords in the list as [1]
#Use the append() function to add each username and password to the users and passwords list

for line in find_user:
    line = line.split(", ")
    username = line[0]
    password = line[1].replace("\n", "")
    users.append(username)
    passwords.append(password)

#Use a loop to run through the input of each user
#Set a variable for the input username and user password
#Use an if statement to determine if the username is in the users.txt file
#If the input username is in the users.txt file, then we set the index for the password to be the same as the username

while True:

    user_name = input("\nPlease enter your username:\n\n")

    if user_name in users:
        password_index = users.index(user_name)

#If username and password match to one of the lines in the users.txt file, allow them in and break the loop
        user_password = input("\n\nPlease enter your password:\n\n")
        
        if  user_password == passwords[password_index]:
            print("\n\nWelcome to Task Manager, " + user_name)
            break

#If the password is entered incorrectly, request password again and let them in if it's correct

        else:
            print("\nYou have entered an incorrect password.")
            user_password = input("\n\nPlease enter your password again:\n\n")

            if  user_password == passwords[password_index]:
                print("\n\nWelcome to Task Manager, " + user_name)
                break
            

#If the username is incorrect, request username again

    else:
        print("\nYou have entered an incorrect username.")
    
#Close the users.txt file using the close() function

user_list.close()

#------------------------------------------------MENU-------------------------------------------------------------#

#Use a loop to present the menu to the user
#Use the lower()function to convert inputs to lowercase

print("\n------------------------------------------------------------------------------\n")

while True:
    
    menu = input('''\n\nSelect one of the following Options below:\n
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - View my task
                    s - View statistics
                    e - Exit
                    \n\n''').lower()

#------------------------------------------------REGISTER USER---------------------------------------------------#

#Use an if statement if the user selects 'r'
#Set a condition that the username has to be admin in order to register a new user

    if menu == 'r' and user_name == "admin":

#Open the users.txt file in 'a' mode, where the handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

        user_list = open("users.txt", "a")

#Use a loop to get the information for the new user

        while True:

            new_user_name = input("\n\nPlease enter the new username that you wish to add:\n\n").lower()
            new_user_password = input("\n\nPlease enter their password:\n\n")
            confirm_password = input("\n\nPlease confirm password:\n\n")

#If the passwords do not match, request confirmation again

            if new_user_password != confirm_password:
                print("\n\nThe passwords do not match. Please try again.\n\n")

#If the passwords match, add the new user information to the users.txt file
#Use the format{} function to write the user information with the same format as previous users

            elif new_user_password == confirm_password:

                print("\n\nThank you!\n\n")
                print(new_user_name + " has been added to your database.\n\n")
                new_user = f"{new_user_name}, {new_user_password}\n"
                user_list.write(new_user)

#If username isn't admin, prompt to choose another option from the menu 

            else:
                print("\nSorry, you do not have access to register new users!\n")
                print("\nPlease choose another option from the menu below.\n")

#Close the file  and break the loop
                
            user_list.close()

#------------------------------------------------ADD TASK-------------------------------------------------------#

#If user selects 'a' to add a task
#Open the tasks.txt file in 'a' mode where the handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

    elif menu == 'a':

#Set new input variables for each task element
#Use the date() function to pull today's date
#For the due date set it in the same format as the current date

        new_task = open("tasks.txt", "a")
        assign_task = input("\n\nPlease assign a username to the task:\n\n")
        title_task = input("\n\nPlease confirm the title of the task:\n\n")
        description = input("\n\nPlease write a description of the task:\n\n")
        current_date = date.today()
        due_date = input("\n\nPlease enter the due date for this task (format YYYY-MM-DD):\n\n")
        task_completion = input("\n\nPlease confirm if the task is completed or not (Yes or No):\n\n")

#Write the new task onto the tasks.txt file using the format{} function 

        new_task.write(f"{assign_task}, {title_task}, {description}, {current_date}, {due_date}, {task_completion}\n")

        print("\n\nThank you, your task has been added to 'tasks.txt'\n\n")
        # print("\nPlease choose another option from the menu below.\n")--------ask sash how to go back to menu

#Close the file and break the loop

        new_task.close()
        break

#------------------------------------------------VIEW TASKS-----------------------------------------------------#

#If the user selects the 'va' option to view all tasks
#Open the tasks.txt file as read only, where the handle is positioned at the beginning of the file. This is also the default mode in which a file is opened.

    elif menu == 'va':

#Set empty list variables for each task element so that we can index them
#Use the readlines() function to read through each line in the file

        view_tasks = open("tasks.txt", "r")
        find_task = view_tasks.readlines()
        assign_task = []
        title_task = []
        description = []
        current_date = []
        due_date = []
        task_completion = []

#Use a for loop to run through each element of the file
#For each line in the tasks.txt file use the split()function to split strings into a list 
#Set the positions for each task element 

        for lines in find_task:

            lines = lines.split(", ")
            assign_task = lines[0]
            title_task = lines[1]
            description = lines[2]
            current_date = lines[3]
            due_date = lines[4]
            task_completion = lines[5]

#Print out the tasks in the requested format, using indexing
#Convert each element to a string so that the print function works

            print("\n------------------------------------------------------------------------------\n")

            print("Task:\t\t\t\t" + str(title_task))

            print("Assigned to:\t\t\t" + str(assign_task))

            print("Date assigned:\t\t\t" + str(current_date))

            print("Due Date:\t\t\t" + str(due_date))

            print("Task complete?\t\t\t" + str(task_completion))

            print("Task Description:\n" + str(description))

            print("\n------------------------------------------------------------------------------\n")
            
            
#Close file and break menu loop

            view_tasks.close()   

#------------------------------------------------VIEW MY TASK(S)----------------------------------------------#

#If the user selects 'vm' to view my task(s)
#Open both users.txt and tasks.txt file as read only, where the handle is positioned at the beginning of the file. This is also the default mode in which a file is opened.
#Use readlines() function to read through each line in the files 

    elif menu == 'vm':

        username_find = open("users.txt", "r")
        find_users = username_find.readlines()
        view_user_task = open("tasks.txt", "r")

#Set empty list variables for users and tasks for indexing purposes 

        users = []
        tasks  = []

#Get username from user

        input_username = input("\n\nPlease enter your username:\n\n")

        #If username is incorrect, prompt accordingly

#For each line in the users.txt file use the split()function to split strings into a list 
#Set users element as position [0]

        for line in find_users:
            line = line.split(", ")
            username = line[0]

#If username is incorrect, prompt accordingly

        if input_username != users:

                print("\nYou have entered an incorrect username.\n")
                input_username = input("\nPlease enter your username again:\n")

#For each line in the tasks.txt file use the split()function to split strings into a list 
#Set tasks element as position [0], matching with the user position

        for line in view_user_task:
            split_data = line.split(", ")
            if input_username == split_data[0]:
        
#Print in the requested format, using indexing 
#Convert each element to a string so that the print function works

                print("\n------------------------------------------------------------------------------\n")

                print("Task:\t\t\t\t" + split_data[1])

                print("Assigned to:\t\t\t" + split_data[0])

                print("Date assigned:\t\t\t" + split_data[3])

                print("Due Date:\t\t\t" + split_data[4])

                print("Task complete?\t\t\t" + split_data[5])

                print("Task Description:\n" + split_data[2] + "\n")
                

        print("\n------------------------------------------------------------------------------\n")

#Close file and break menu loop
        
        view_user_task.close()

#------------------------------------------------STATISTICS-------------------------------------------------#

#Open both users.txt and tasks.txt file as read only, where the handle is positioned at the beginning of the file. This is also the default mode in which a file is opened.

    elif menu == 's' and user_name == "admin":

        print("\nWelcome, Admin!\n")
        usernames = open("users.txt", "r")
        tasks = open("tasks.txt", "r")

#Set counter to 0 for each file

        tasks_num = 0
        users_num = 0

#For each line in the tasks file, count in increments of 1
#Print using the format function

        for line in tasks:
            tasks_num += 1
        print("\n------------------------------------------------------------------------------\n")

        print (f"\nTotal number of tasks:\t\t\t {tasks_num}")

#For each line in the usernames file, count in increments of 1
#Print using the format function

        for line in usernames:
            users_num += 1
        print (f"\nTotal number of users:\t\t\t {users_num}\n")

        print("\n------------------------------------------------------------------------------\n")

#Close each file and break the menu loop

        usernames.close()
        tasks.close()
        break

#------------------------------------------------EXIT------------------------------------------------------#

#If  user selects 'e' to exit 
#Say goodbye

    elif menu == 'e':
        
        print('Goodbye!!!')
        exit()

#If user selects invalid menu  choice, restart loop

    else:
        print("\nYou have made a wrong choice, please try again.")
