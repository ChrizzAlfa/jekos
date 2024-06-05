from tkinter import *
from tkinter import font
from subprocess import call
from PIL import Image, ImageTk


def btn_clicked():
    print("Button Clicked")

def moveW(prop):
    with open("current_kos.txt", "w") as f:
        f.write(prop)

    window.destroy()
    call(["python", "kos_details.py"])

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

background_img = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_home\\bg_home.png")
background = canvas.create_image(
    507.0, 386.0,
    image = background_img)

canvas.create_text(
    95.5, 100.0,
    text = "All Kos",
    fill = "#ffffff",
    font = (font.Font(family = "MontserratRoman", size = 20, weight= "bold")))

canvas.create_text(
    64.5, 75.5,
    text = "Home",
    fill = "#ffffff",
    font = ("MontserratRoman-Regular", int(10.0)))

canvas.create_text(
    803.5, 339.0,
    text = "Campur",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(15.0)))

canvas.create_text(
    513.5, 548.0,
    text = "Campur",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(15.0)))

canvas.create_text(
    224.5, 339.0,
    text = "Putra",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(15.0)))

canvas.create_text(
    809.5, 548.0,
    text = "Putra",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(15.0)))

canvas.create_text(
    516.5, 339.0,
    text = "Putri",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(15.0)))

canvas.create_text(
    227.5, 548.0,
    text = "Putri",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(15.0)))

img_0 = Image.open(f"C:\\Users\\alfar\\Personal\\jekos\\img_kos\\kos_hemngker.png")
resize_image = img_0.resize((238, 150))
img0 = ImageTk.PhotoImage(resize_image)
kos0 = canvas.create_image(149, 240, image = img0)

b0 = Button(
    text = "Kos Hemngker",
    font = "MontserratRoman-Bold",
    foreground = "#FFFFFF",
    bg = "#076585",
    command = lambda:
    [print(b0.cget("text")), moveW(b0.cget("text"))],
    relief = "flat")
b0.place(
    x = 30, y = 290,
    width = 238,
    height = 35)

img_1 = Image.open(f"C:\\Users\\alfar\\Personal\\jekos\\img_kos\\kos_gulag.png")
resize_image = img_1.resize((238, 150))
img1 = ImageTk.PhotoImage(resize_image)
kos1 = canvas.create_image(440, 240, image = img1)

b1 = Button(
    text = "Kos Gulag",
    font = "MontserratRoman-Bold",
    foreground = "#FFFFFF",
    bg = "#076585",
    command = lambda:
    [print(b1.cget("text")), moveW(b1.cget("text"))],
    relief = "flat")
b1.place(
    x = 321, y = 290,
    width = 238,
    height = 35)

img_2 = Image.open(f"C:\\Users\\alfar\\Personal\\jekos\\img_kos\\kos_hobby.png")
resize_image = img_2.resize((238, 150))
img2 = ImageTk.PhotoImage(resize_image)
kos2 = canvas.create_image(727, 240, image = img2)

b2 = Button(
    text = "Kos Hobby",
    font = "MontserratRoman-Bold",
    foreground = "#FFFFFF",
    bg = "#076585",
    command = lambda:
    [print(b2.cget("text")), moveW(b2.cget("text"))],
    relief = "flat")
b2.place(
    x = 608, y = 290,
    width = 238,
    height = 35)

img_3 = Image.open(f"C:\\Users\\alfar\\Personal\\jekos\\img_kos\\kos_batman.png")
resize_image = img_3.resize((238, 150))
img3 = ImageTk.PhotoImage(resize_image)
kos3 = canvas.create_image(152, 240 + 200, image = img3)

b3 = Button(
    text = "Kos Batman",
    font = "MontserratRoman-Bold",
    foreground = "#FFFFFF",
    bg = "#076585",
    command = lambda:
    [print(b3.cget("text")), moveW(b3.cget("text"))],
    relief = "flat")    
b3.place(
    x = 33, y = 496,
    width = 238,
    height = 35)

img_4 = Image.open(f"C:\\Users\\alfar\\Personal\\jekos\\img_kos\\kos_dababy.png")
resize_image = img_4.resize((238, 150))
img4 = ImageTk.PhotoImage(resize_image)
kos4 = canvas.create_image(152 + 286, 240 + 200, image = img4)

b4 = Button(
    text = "Kos DaBaby",
    font = "MontserratRoman-Bold",
    foreground = "#FFFFFF",
    bg = "#076585",
    command = lambda:
    [print(b4.cget("text")), moveW(b4.cget("text"))],
    relief = "flat")
b4.place(
    x = 319, y = 496,
    width = 238,
    height = 35)

img_5 = Image.open(f"C:\\Users\\alfar\\Personal\\jekos\\img_kos\\kos_ohio.png")
resize_image = img_5.resize((238, 150))
img5 = ImageTk.PhotoImage(resize_image)
kos5 = canvas.create_image(441 + 286, 240 + 200, image = img5)

b5 = Button(
    text = "Kos Ohio",
    font = "MontserratRoman-Bold",
    foreground = "#FFFFFF",
    bg = "#076585",
    command = lambda:
    [print(b1.cget("text")), moveW(b5.cget("text"))],
    relief = "flat")
b5.place(
    x = 608, y = 496,
    width = 238,
    height = 35)

# Next page button
img6 = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_home\\img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b6.place(
    x = 942, y = 523,
    width = 7,
    height = 15)

# Previous page button
img7 = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_home\\img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b7.place(
    x = 912, y = 523,
    width = 7,
    height = 15)

# Profile button
img8 = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_home\\img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    bg = "#076585",
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b8.place(
    x = 910, y = 71,
    width = 40,
    height = 40)

# Upload kos button
img9 = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_home\\img9.png")
b9 = Button(
    image = img9,
    bg = "#076585",
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
b9.place(
    x = 736, y = 72,
    width = 110,
    height = 38)

with open("current_client.txt") as f:
    client = f.readline()

if client.split()[-1] == "0":
    b8.destroy()
    b9.destroy()

    canvas.create_text(
    770, 90,
    text = client.split()[0],
    fill = "#ffffff",
    font = (font.Font(family = "MontserratRoman", size = 20, weight= "bold")))
else:
    print("This is an admin")

window.resizable(False, False)
window.mainloop()