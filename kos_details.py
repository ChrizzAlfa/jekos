from tkinter import *
from PIL import Image, ImageTk
from subprocess import call
import webbrowser

def kosCheck():
    for line in open("admin_data.txt","r").readlines():
        # Split on the space, and store the results in a list of two strings
        kos_info = line.split(";")
        with open("current_kos.txt") as g:
            kos = g.readline()
        if kos == kos_info[1]:
            return kos_info
    return False

def callback(url):
   webbrowser.open_new_tab(url)


def btn_clicked():
    print("Please Contact the Owner")

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

background_img = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_details\\bg_details.png")
background = canvas.create_image(
    558.5, 256.5,
    image = background_img)

# Rent Button
rent_btn = PhotoImage(file = f"C:\\Users\\alfar\\Personal\\jekos\\recource_details\\btn_rent.png")
rent = Button(
    image = rent_btn,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")
rent.place(
    x = 735, y = 490,
    width = 170,
    height = 45)

back = Button(
    text = "HOME",
    font = "MontserratRoman-Bold",
    foreground = "#000000",
    bg = "#FFFFFF",
    command = lambda:
    [window.destroy()
    ,call(["python", "home.py"])],
    relief = "flat")
back.place(
    x = 100, y = 496,
    width = 100,
    height = 45)

# Variables
owner = kosCheck()[0].split()
kos_name = kosCheck()[1]
imgkos_name = kos_name.replace(" ", "_").lower()
lokasi = kosCheck()[2]
link_kos = kosCheck()[3]
harga = kosCheck()[4]
other = kosCheck()[5]
phone = kosCheck()[6].replace("\n", "")

img_kos = Image.open(f"C:\\Users\\alfar\\Personal\\jekos\\img_kos\\{imgkos_name}.png")
resize_image = img_kos.resize((238, 150))
imgkos = ImageTk.PhotoImage(resize_image)
kos = canvas.create_image(300, 200, image = imgkos)

canvas.create_text(
    610.0, 131.0,
    text = kos_name,
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(24.0)))

canvas.create_text(
    610.0, 161.0,
    text = f"{harga}/Month",
    fill = "#ffffff",
    font = ("MontserratRoman-Regular", int(20.0)))

canvas.create_text(
    600.0, 217.0,
    text = "Lokasi",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(24.0)))

link = Label(window, text = lokasi,font=("MontserratRoman-Regular", 13), fg = "#000000", cursor="hand2")
link.place(x = 490, y = 240)
link.bind("<Button-1>", lambda e: callback(link_kos))

canvas.create_text(
    210.0, 390.0,
    text = "DESCRIPTION",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(24.0)))

canvas.create_text(
    830.0, 390.0,
    text = "OWNER",
    fill = "#ffffff",
    font = ("MontserratRoman-Bold", int(24.0)))

canvas.create_text(
    355, 450,
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nMorbi ac maximus est. Vestibulum sit amet cursus magna,\nu faucibus tellus. Quisque id luctus metus.",
    fill = "#ffffff",
    font = ("MontserratRoman-Regular", int(15.0)))

canvas.create_text(
    820.0, 442.0,
    text = phone,
    fill = "#ffffff",
    font = ("MontserratRoman-Regular", int(15.0)))

canvas.create_text(
    880.0, 420.0,
    text = owner[0],
    fill = "#ffffff",
    font = ("MontserratRoman-Regular", int(15.0)))

canvas.create_text(
    830.0, 462.0,
    text = other,
    fill = "#ffffff",
    font = ("MontserratRoman-Regular", int(15.0)))

window.resizable(False, False)
window.mainloop()
