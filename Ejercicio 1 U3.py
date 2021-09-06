from tkinter import *

root = Tk()
root.title("Tarea POO")

Label(root, text= "Ingrese sus datos", bg= "purple2", fg= "white").grid(row=0, column=0,columnspan=18, sticky= W+E+N+S)


Label(root, text="Título").grid(row=1, column=0, sticky= W)
Label(root, text="Ruta").grid(row=2, column=0, sticky= W)
Label(root, text="Descripción").grid(row=3, column=0, sticky= W)
e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)


a = Button(root, text="Alta", fg= "black"). grid( row=4, column=1, padx=5,pady=2, sticky= N)
b = Button(root, text="Sorpresa", fg= "black"). grid( row=4, column=8, padx=45,pady=2, sticky= SE)



mainloop() 

