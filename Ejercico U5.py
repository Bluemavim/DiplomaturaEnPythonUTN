from tkinter import *
import random

root = Tk()
root.title("Tarea POO")

#Variables globales

e1= StringVar()
e2= StringVar()
e3= StringVar()
w_ancho= 20


#Funciones

 
entry = []
def mostrarentrada():
    diccionario= {"Título": e1.get(), "Ruta": e2.get(), "Descripción": e3.get()}
    entry.append(diccionario)
    print(len(entry)-1)
    for i in range(len(entry)):
        print(entry[i])
    refresh()
        
def refresh():
    e1.set(" ")
    e2.set(" ")
    e3.set(" ")
              
def changecolor():
   global f
   f= random.choice(list(colores))
   root["bg"]=f

def entrada(text_var, ancho, row, col):    #Honestamente, esto me rompió el cráneo. Todavia no entiendo muy bien a qué apunta. Me ayudó la clase.
   entrada = Entry(root, textvariable=text_var, width=ancho)
   entrada.grid(row=row, column=col)
   return entrada

#Layout

titulo1 = Label(root, text= "Ingrese sus datos", bg= "purple2", fg= "white").grid(row=0, column=0,columnspan=18, sticky= W+E+N+S)

Label(root, text="Título").grid(row=1, column=0, sticky= W)
Label(root, text="Ruta").grid(row=2, column=0, sticky= W)
Label(root, text="Descripción").grid(row=3, column=0, sticky= W)

entrada(e1,20,1,1)
entrada(e2,20,2,1)
entrada(e3,20,3,1)


#Lista de colores
colores=["blanched almond", "Skyblue2", "coral1", "plum2", "misty rose", "IndianRed1", "ivory3", "lime green", "dodger blue"]   

#Botones
a = Button(root, text="Alta", fg= "black", command=mostrarentrada). grid( row=4, column=1, padx=5,pady=2, sticky= N)
b = Button(root, text="Sorpresa", fg= "black", command=changecolor). grid( row=4, column=8, padx=45,pady=2, sticky= SE)


mainloop() 
