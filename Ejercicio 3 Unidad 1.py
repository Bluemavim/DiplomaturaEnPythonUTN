from tkinter import *
import random
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = "6"
b = random.randrange(50,100)
c = int(a)+ b
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()
