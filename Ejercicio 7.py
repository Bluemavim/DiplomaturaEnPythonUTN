from tkinter import *
import random
import  mysql.connector
from tkinter import messagebox
import re


root = Tk()
root.title("Tarea POO")

#Variables globales

e1= StringVar()
e2= StringVar()
e3= StringVar()
w_ancho= 20


#Funciones

def crearbd():
    try:
       mibase=   mysql.connector.connect(host="localhost", user="root", passwd="" )
       micursor=  mibase.cursor()
       micursor.execute("CREATE   DATABASE   basedeprueba1")
       micursor= mibase.cursor()
       micursor.executemicursor.execute("CREATE   TABLE   producto(   id   int(11)   NOT   NULL   PRIMARY   KEY  AUTO_INCREMENT,   titulo   VARCHAR(128)   COLLATE   utf8_spanish2_ci   NOT   NULL,   ruta varchar(128)   COLLATE   utf8_spanish2_ci   NOT   NULL,   descripcion   text   COLLATE utf8_spanish2_ci   NOT   NULL   )") 
       print( "Base de datos con tabla creada")
    except:
         print("Ya existe la base de datos")

def miconexion():
    mibase=   mysql.connector.connect(host="localhost", user="root", passwd="" )
    return mibase       


def alta():
    
    print("Nueva alta de datos")
    cadena= e1.get()
    patron= "^[A-Za-z]+(?:[ _-][A-Za-z]+)*$" 
    if (re.match(patron,cadena)):
        print(" Cadena valida")



        mibase = miconexion()
        print(mibase)
        micursor = mibase.cursor()
        sql = "INSERT INTO producto (titulo, ruta, descripcion) VALUES (%s, %s, %s)"
        datos = (e1.get(), e2.get(), e3.get())
        micursor.execute(sql, datos)
        mibase.commit()

    else:
        messagebox.showwarning(message="Caracteres no válidos", title= "Intente nuevamente")
        print("Cadena no valida")
   

           
def changecolor():
   global f
   f= random.choice(list(colores))
   root["bg"]=f

def entrada(text_var, ancho, row, col):    
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

#Lista de colores y botón de color
colores=["blanched almond", "Skyblue2", "coral1", "plum2", "misty rose", "IndianRed1", "ivory3", "lime green", "dodger blue"]
b = Button(root, text="Sorpresa", fg= "black", command=lambda:changecolor()). grid( row=4, column=8, padx=45,pady=2, sticky= SE)


#Botones
a = Button(root, text="Alta", fg= "black", command=lambda:alta()). grid( row=4, column=1, padx=5,pady=2, sticky= N)
c = Button(root, text="Crear BD", fg= "black", command=lambda:crearbd()). grid( row=4, column=3, padx=45,pady=2, sticky= SE)

mainloop() 

