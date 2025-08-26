import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        self.task = []
        self.load_tasks()

        self.create_widgets()
        self.update_task_list()
        
    def create_widgets(self):
        title_label = tk.Label(
            self.root,
            text="My Todo List",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=10)

        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=40,
            relief='solid',
            bd=1
        )
        self.task_entry.pack(side='left', padx=(0, 10))
        self.task_entry.bind('<Return>', lambda e: self.add_task())

        add_button = tk.Button(
            input_frame,
            text="Add Task",
            command=self.add_task,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 12, "bold"),
            relief='flat',
            padx=20
        )
        add_button.pack(side='right')

        list_frame = tk.Frame(self.root, bg='#f0f0f0')
        list_frame.pack(pady=10, padx=20, fill='both', expand=True)

        listbox_frame = tk.frame = tk.Frame(list_frame, bg='#f0f0f0')
        listbox_frame.pack(fill='both', expand=True)

        self.task_listbox = tk.Listbox(
            listbox_frame,
            font=("Arial", 11),
            selectmode='single',
            relief='solid',
            bd=1,
            height=15,
        )

        scrollbar = tk.Scrollbar(listbox_frame, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10, padx=20)

        complete_button = tk.Button(
            button_frame,
            text="Mark as Complete",
            command=self.complete_task,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 12, "bold"),
            relief='flat',
            padx=15
        )
        complete_button.pack(side='left', padx=5)

        delete_button = tk.Button(
            button_frame,
            text="Delete Task",
            command=self.delete_task,
            bg='#f44336',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='flat',
            padx=15
        )
        delete_button.pack(side='left', padx=5)

        clear_button = tk.Button(
            button_frame,
            text="Clear All",
            command=self.clear_all,
            bg='#ff9800',
            fg='white',
            font=("Arial", 10, "bold"),
            relief='flat',
            padx=15
        )
        clear_button.pack(side='left', padx=5)

        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666666'
        )
        self.status_label.pack(pady=5)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
