
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pingtest
import scan


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"C:\Users\DOUSSAIN\Desktop\figma\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


thePing = "92 ms"
ports = "Waiting"

window = Tk()

window.geometry("679x396")
window.configure(bg="#1F1F1F")


canvas = Canvas(
    window,
    bg="#1F1F1F",
    height=396,
    width=679,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# title
canvas.create_text(
    275.0,
    30.0,
    anchor="nw",
    text="Sema Os",
    fill="#FFFFFF",
    font=("Inter Bold", 30 * -1)
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (
        setTheOpenPorts(scan.scan_ports("127.0.0.1"))
    ),
    relief="flat"
)
button_1.place(
    x=307.0,
    y=302.0,
    width=64.0,
    height=24.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: (
        setThePing(pingtest.ping("google.fr"))
    ),
    relief="flat"
)
button_2.place(
    x=206.0,
    y=150.0,
    width=64.0,
    height=24.0
)

ping_text = canvas.create_text(
    206.0,
    115.0,
    anchor="nw",
    text=thePing,
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=389.0,
    y=150.0,
    width=64.0,
    height=24.0
)

canvas.create_text(
    371.0,
    115.0,
    anchor="nw",
    text="300 mbps",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

open_ports_text = canvas.create_text(
    339.0,
    256.0,
    text=ports,
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)


def setThePing(ping):
    canvas.itemconfigure(ping_text, text=ping + ' ms')


def setTheOpenPorts(ports):
    print(ports)
    canvas.itemconfigure(open_ports_text, text=ports)


window.resizable(False, False)
window.mainloop()
