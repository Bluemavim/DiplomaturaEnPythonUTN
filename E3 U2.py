from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
D = { 'identificador': 5, 'nombre': "Mariana", 'apellido': "Avio", 'telefono': 1515212115} 
a = list(D.keys())
oracion1= "Los elementos del diccionario son " + str(len(a)) + "."
oracion2= "Las claves del diccionario son " + a[0] + ", " + a[1] + ", " +  a[2] + " y " +  a[3] + "."
tx= oracion1 + " " + oracion2
var = IntVar()
e.config(textvariable=var)
var.set(tx)
mainloop()


