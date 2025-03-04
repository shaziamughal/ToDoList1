import tkinter as tk
from tkinter import messagebox

# File to store tasks
TASKS_FILE = "tasks.txt"

# Create main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Create frame for task list
frame = tk.Frame(root)
frame.pack(pady=10)

# Listbox to display tasks
task_listbox = tk.Listbox(frame, width=40, height=10, font=("Arial", 14))
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Entry field for new tasks
task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Functions for task management
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = task_listbox.curselection()
        task_listbox.delete(selected_task)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to remove!")

def save_tasks():
    """Saves tasks to a file"""
    with open(TASKS_FILE, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    """Loads tasks from a file at startup"""
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass  # If file doesn't exist, ignore error

def clear_tasks():
    """Clears all tasks from the list"""
    task_listbox.delete(0, tk.END)
    save_tasks()

# Buttons
add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=12)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, width=12)
remove_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks, width=12)
clear_button.pack(side=tk.LEFT, padx=5)

# Load tasks on startup
load_tasks()

# Run the application
root.mainloop()