from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
frutas= ["papaya", "uva"]
a= "Deberías tomar un jugo de "
b= " y "
c= "."
d= a+ frutas[0] + b + frutas[1]+c
var = IntVar()
e.config(textvariable=var)
var.set(d)
mainloop()

