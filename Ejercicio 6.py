from tkinter import *
import random
import   mysql.connector 

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

def alta():
    print( "Nueva alta de datos")
    mibase = miconexion()
    print(mibase)
    micursor = mibase.cursor()
    sql=    "INSERT   INTO   producto   (titulo,   ruta,   descripcion)   VALUES   (%s,   %s,   %s)"

    d1= e1.get()
    d2= e2.get()
    d3= e3.get()
    datos= (d1, d2, d3)
    micursor.execute(sql, datos)
    mibase.commit()
    

def miconexion():
    mibase=   mysql.connector.connect(host="localhost", user="root", passwd="" )
    return mibase       

 
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
a = Button(root, text="Alta", fg= "black", command=lambda:mostrarentrada()). grid( row=4, column=1, padx=5,pady=2, sticky= N)
b = Button(root, text="Sorpresa", fg= "black", command=lambda:changecolor()). grid( row=4, column=8, padx=45,pady=2, sticky= SE)
b = Button(root, text="Crear BD", fg= "black", command=lambda:crearbd()). grid( row=4, column=3, padx=45,pady=2, sticky= SE)

mainloop() 
