# # Error Handling
# try:
#     file = open("project 30/example.txt")
#     example_dict = {"key": "Rubel"}
#     print(example_dict["key"])
# except FileNotFoundError:
#     file = open("project 30/example.txt", mode="w")
#     file.write("Halalulliah")
# except KeyError as error_massage:
#     print(f"The key {error_massage} doesn't exits.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File closed Successfully")
#     raise KeyError ("I just made up an error")


# # Create my own error
# height = float(input("Height: "))
# weight = float(input("Weight: "))

# if height > 5:
#     raise ValueError("Human height should not more than 5 meters.")
# if weight > 2000:
#     raise ValueError("Human weight should not more than 2000 kg.")
# bmi = weight / height**2
# print(bmi)

# ----------------------- Practice Code ----------------------- #

# # 1. Use what you've learnt about exception handling to prevent the program from crashing.
# facebook_posts = [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]

# total_likes = 0
# # TODO: Catch the KeyError exception
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass


# print(total_likes)


# ----------------------- TO DO LIST TKINTER --------------------------- #
import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
import json

def add_task():
    selected_date = cal.get_date().strftime("%d/%m/%Y")
    task = entry_task.get()
    new_data = {
        selected_date : task
    }
    # Add your task handling logic here
    try:
        with open("project 30/practice_data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("project 30/practice_data.json", mode="w") as file:
            json.dump(new_data, file, indent=4)
    else: 
        data.update(new_data)
        with open("project 30/practice_data.json", mode="w") as file:
            json.dump(data, file, indent=4)
    finally:
        entry_task.delete(0,END)

# Create the main window
root = tk.Tk()
root.minsize(width=500, height=500)
root.title("To-Do List")

# Date Entry
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)

# Task Entry
entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)
entry_task.focus()

# Button to add task
btn_add_task = tk.Button(root, text="Add Task", command=add_task)
btn_add_task.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()


