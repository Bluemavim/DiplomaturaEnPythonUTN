from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
frutas = ["papaya", "melón", "sandía", "frambuesa", "mora", "piña", "uva"]
var = IntVar()
e.config(textvariable=var)
var.set(frutas[2])
mainloop()
