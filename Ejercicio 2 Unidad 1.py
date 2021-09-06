from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
a = "9"
b = 2
c = a + str(b)
var = IntVar()
e.config(textvariable=var)
var.set(c)
mainloop()
