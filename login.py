from tkinter import *
from tkinter import messagebox
from subprocess import call
from tkinter import font


def userCheck(user, code):
  # Read the lines  
  for line in open("user_data.txt","r").readlines():
      # Split on the space, and store the results in a list of two strings
      login_info = line.split()
      if user == login_info[0] and code == login_info[1]:
          print("Correct credentials!")
          with open("current_client.txt", "w") as f:
            f.write(f"{login_info[0]} 0")
          return True
  messagebox.showerror("Invalid", "Incorrect credentials.")
  return False

def user_clicked():
    user = username.get()
    code = password.get()

    if userCheck(user, code):
        window.destroy()
        call(["python", "home.py"])

def adminCheck(user, code):
  # Read the lines  
  for line in open("admin_data.txt","r").readlines():
      # Split on the space, and store the results in a list of two strings
      login_info = line.split()
      if user == login_info[0] and code == login_info[1]:
          print("Correct credentials!")
          with open("current_client.txt", "w") as f:
            f.write(f"{login_info[0]} 1")
          return True
  messagebox.showerror("Invalid", "Incorrect credentials.")
  return False

def admin_clicked():
    user = username.get()
    code = password.get()

    if adminCheck(user, code):
        window.destroy()
        call(["python", "home.py"])

window = Tk()
window.title("JEKOS")

window.geometry("1000x600")
window.configure(bg = "#252525")
canvas = Canvas(
    window,
    bg = "#252525",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

#Background Image
background_img = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_login\\bg_login.png")
background = canvas.create_image(
    639.5, 397.0,
    image = background_img)

#Username Textbox
username_img = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_login\\img_username.png")
username_bg = canvas.create_image(
    750.0, 228.5,
    image = username_img)

username = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

username.place(
    x = 663.0, y = 206,
    width = 174.0,
    height = 43)

user = username.get()

#Password Textbox
password_img = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_login\\img_password.png")
password_bg = canvas.create_image(
    750.0, 311.5,
    image = password_img)

password = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

password.place(
    x = 663.0, y = 289,
    width = 174.0,
    height = 43)

#Sign up Button
signup_btn = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_login\\btn_signup.png")
signup = Button(
    image = signup_btn,
    borderwidth = 0,
    highlightthickness = 0,
    # command = btn_clicked,
    relief = "flat")

signup.place(
    x = 150, y = 500,
    width = 200,
    height = 46)

# User Login Button
login_user = Button(
    text = "USER",
    font = "MontserratRoman-Bold",
    foreground = "#FFFFFF",
    bg = "#076585",
    command = user_clicked,
    relief = "flat")

login_user.place(
    x = 650, y = 372,
    width = 200,
    height = 46)

# Admin login button
login_admin= Button(
    text = "ADMIN",
    font = "MontserratRoman-Bold",
    foreground = "#FFFFFF",
    bg = "#076585",
    command = admin_clicked,
    relief = "flat")

login_admin.place(
    x = 650, y = 455,
    width = 200,
    height = 46)

canvas.create_text(
    750.0, 130.0,
    text = "LOGIN",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(24.0)))

canvas.create_text(
    700.0, 191.0,
    text = "Username",
    fill = "#ffffff",
    font = ("MontserratRoman-Regular", int(15.0)))

canvas.create_text(
    700.0, 274.0,
    text = "Password",
    fill = "#ffffff",
    font = ("MontserratRoman-Regular", int(15.0)))

window.resizable(False, False)
window.mainloop()