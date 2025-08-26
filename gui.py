import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Hello", "Hello World!")

root = tk.Tk()
root.title("My Gui")
root.geometry("300x200")
root.geometry("300x200")

button=tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=20)
root.mainloop()