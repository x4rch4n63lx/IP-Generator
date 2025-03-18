# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 3/18/2025 - 1:40AM
# Script Purpose : A graphical user interface (GUI) program that allows users to 
#                  log in with credentials and generate random IP addresses.
# Description    : 
#                  This script creates a simple yet sleek Tkinter-based application.
#                  Users must log in using a username and password ("root" for both)
#                  before accessing the IP generator. Upon successful login, users
#                  can generate random IPv4 addresses with a single click.
#                  
# Features       : 
#                  - Dark mode for reduced eye strain
#                  - User authentication with username and password
#                  - Clean and user-friendly post-login interface
#                  - Random IP generation and display
#                  
# Requirements   : 
#                  - Python 3.x
#                  - tkinter module (comes pre-installed with Python)
#                  - No additional dependencies required
#                  
# ===================================================================================

import tkinter as tk
from tkinter import messagebox
import random


def style_widget(widget, fg_color="#ffffff", bg_color="#2b2b2b", font=("Arial", 12), justify=None):
    widget.config(fg=fg_color, bg=bg_color, font=font)
    if justify:  
        widget.config(justify=justify)


# Function to verify login
def login():
    if username_entry.get() == "root" and password_entry.get() == "root":
        messagebox.showinfo("Login Successful", "Welcome!")
        root.title("IP Generator")  
        switch_frame(generator_frame)  
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def generate_ip():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    ip_label.config(text=f"{ip}")


def switch_frame(frame):
    frame.tkraise()  


root = tk.Tk()
root.title("IP Generator with Login")
root.geometry("400x300")
root.configure(bg="#2b2b2b")  

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

login_frame = tk.Frame(root, bg="#2b2b2b")

login_label = tk.Label(login_frame, text="Login", font=("Arial", 16, "bold"))
style_widget(login_label)
login_label.pack(pady=20)

username_label = tk.Label(login_frame, text="Username:")
style_widget(username_label)
username_label.pack()

username_entry = tk.Entry(login_frame, font=("Arial", 12), bg="#3c3c3c", fg="#ffffff", insertbackground="#ffffff", justify="center")
username_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Password:")
style_widget(password_label)
password_label.pack()

password_entry = tk.Entry(login_frame, font=("Arial", 12), bg="#3c3c3c", fg="#ffffff", show="*", insertbackground="#ffffff", justify="center")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", command=login, font=("Arial", 12), bg="#4caf50", fg="#ffffff")
login_button.pack(pady=20)

generator_frame = tk.Frame(root, bg="#2b2b2b")

generator_label = tk.Label(generator_frame, text="Welcome to the IP Generator", font=("Arial", 16, "bold"))
style_widget(generator_label)
generator_label.pack(pady=15)

instruction_label = tk.Label(generator_frame, text="Click the button to generate a random IP address:", font=("Arial", 12))
style_widget(instruction_label)
instruction_label.pack(pady=10)

generate_button = tk.Button(generator_frame, text="Generate IP", command=generate_ip, font=("Arial", 12), bg="#2196f3", fg="#ffffff")
generate_button.pack(pady=15)

ip_label_frame = tk.Frame(generator_frame, bg="#3c3c3c", padx=10, pady=10)  # Add a bordered section
ip_label_frame.pack(pady=20)

ip_label = tk.Label(ip_label_frame, text="Generated IP will appear here", font=("Arial", 14, "bold"), fg="#4caf50", bg="#3c3c3c")
ip_label.pack()

for frame in (login_frame, generator_frame):
    frame.grid(row=0, column=0, sticky="nsew")
switch_frame(login_frame)

root.mainloop()
