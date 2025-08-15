import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "todo.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a new task
def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete selected task
def delete_task():
    try:
        index = listbox.curselection()[0]
        task = tasks.pop(index)
        save_tasks(tasks)
        listbox.delete(index)
        messagebox.showinfo("Deleted", f"Task '{task}' deleted!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")
root.resizable(False, False)

tasks = load_tasks()

# Entry for new task
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

# Add & Delete buttons
button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

# Listbox for tasks
listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12), selectbackground="lightblue")
listbox.pack(pady=10)

# Load existing tasks into Listbox
for task in tasks:
    listbox.insert(tk.END, task)

root.mainloop()
