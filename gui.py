
# SOLVER
# Created by Ramazan AYDINLI

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# main window

root = tk.Tk()

# name of the the window
root.title("Solver")

# opening size assigned as fullscreen
root.state("zoomed")

# restriction of the smallest size of the window
root.minsize(width=1024, height=768)

# Bg color
main_color="#252526"
root.config(bg=main_color)

# user name needed for reaching desktop
current_user = os.getlogin()
desktop_path = "C:\\Users\\{}\\Desktop".format(current_user)

#Changing Icon from tkinter to specific one
icon_path="provide icon_location here!!!!"
ico = Image.open(icon_path)
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Open picture function and related settings
def open_fn():
    global img_chosen
    root.filename = filedialog.askopenfilename(
        initialdir=desktop_path,title="Select A File",
        filetypes=(("png files", ".png"),
                   ("jpg files", ".jpg")))
    img_chosen = ImageTk.PhotoImage(Image.open(root.filename).resize((800,900)))
    tk.Label(image=img_chosen).place(x=100, y=100)

# Defining button icon path
photo_icon_path="provide photo icon path here!!!!! "
add_photo_icon = tk.PhotoImage(file=photo_icon_path)

#Open File Widget (Button)
img_button=tk.Button(root, text="Open File", image=add_photo_icon, command=open_fn).place(x=0, y=400)
img_button_label = tk.Label(text="Image 1").place(x=15, y=475)

# Output Text Box
output_text = tk.Label(text="Output text will be here",font="Helvetica",
                       height=50,width=75, wraplength= 400).place(x=1000, y=100)

root.mainloop()