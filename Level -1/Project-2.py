# To-Do List Application 

import os
if not os.path.exists('list_data.txt'):
    with open("list_data.txt",'w') as f:
        pass
print("Welcome!")
while True:
    print("\nThese are your choices-")
    print("1. Show Task\n2. Add Task\n3. Delete Task\n4. Exit Console\n")
    user_input = input("Enter the choice: ").strip()
    if not user_input.isnumeric():
        print("Please Enter valid input!")
        continue
    if user_input=='1':
        with open('list_data.txt','r') as f:
            data = [task.strip() for task in f if task.strip()]
            if not data:
                print("No data found!")
                continue
            print(f"These are your Tasks-")
            for i,task in enumerate(data,start=1):
                print(f"{i}. {task}")
    elif user_input=='2':
        date = ""
        data =""
        while True:
            date = input("Enter Date: ").strip()
            if date=="":
                print("Please Enter date!")
                continue
            break
        while True:
            data = input("Enter Task: ").strip()
            if data=="":
                print("Please Enter Task!")
                continue
            break
        data = f"{date}: {data}\n"
        with open('list_data.txt','a') as f:
            f.writelines(data)
        print("Your task has been successfully added!")
    elif user_input=='3':
        task_no = ""
        while True:
            task_no = input("Enter the Task no you want to remove: ")
            if not task_no.isnumeric():
                print("Please Enter valid Task no.!")
                continue
            break
        with open('list_data.txt','r') as f:
            lines = f.readlines()
        rem_task = lines.pop(int(task_no)-1)
        with open("list_data.txt",'w') as f:
            f.writelines(lines)
        print(f"your task no {task_no} has been successfully removed from the list")
    elif user_input=='4':
        print("Thankyou!")
        print("Console has been shut down!")
        break