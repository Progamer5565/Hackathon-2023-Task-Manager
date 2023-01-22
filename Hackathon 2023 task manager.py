import tkinter as tk
from datetime import datetime

tasks = {}

def start_task(task_name):
    tasks[task_name] = datetime.now()
    print(f"Started task {task_name} at {tasks[task_name]}")

def stop_task(task_name):
    end_time = datetime.now()
    duration = end_time - tasks[task_name]
    print(f"Stopped task {task_name} at {end_time}")
    print(f"Duration: {duration}")

def create_gui():
    root = tk.Tk()
    root.title("Task Tracker")

    # input for task B)
    task_label = tk.Label(root, text="Task Name:")
    task_label.grid(row=0, column=0)
    task_entry = tk.Entry(root)
    task_entry.grid(row=0, column=1)

    # Start And Stop B)
    start_button = tk.Button(root, text="Start", command=lambda: start_task(task_entry.get()))
    start_button.grid(row=1, column=0)
    stop_button = tk.Button(root, text="Stop", command=lambda: stop_task(task_entry.get()))
    stop_button.grid(row=1, column=1)

    root.mainloop()

create_gui()
