from tkinter import *

window = Tk()
window.title("Q-Flow Login")
window.geometry("300x200")

username_label = Label(window, text="Username:")
username_label.pack(pady=20)

username_entry = Entry(window)
username_entry.pack()

password_label = Label(window, text="Password:")
password_label.pack(pady=10)

password_entry = Entry(window, show="*")
password_entry.pack()

def login_clicked():
  username = username_entry.get()
  password = password_entry.get()
  print(f"Username: {username}, Password: {password}")  # Replace with your login logic

login_button = Button(window, text="Login", command=login_clicked)
login_button.pack(pady=10)

window.mainloop()
