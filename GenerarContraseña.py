import random
from tkinter import *
from tkinter import messagebox as MessageBox

raiz= Tk()
raiz.geometry("450x420")
raiz.resizable(0,0)
raiz.title("Generador de contraseñas")

capturaSimbolos= StringVar()
tamañoContraseña = StringVar()
contraseñaGenerada = StringVar()
hayMayusculas= IntVar()
hayEnteros = IntVar()

# las bases para armar la contraseña con numeros en mayuscula y ninuscula
letrasminuscula = "abcdefghijklmnopqrstwxyz"
letrasmayus = letrasminuscula.upper()
numeros = "0123456789"



def mostrarContraseña():
    try:
        stringSimbolos = "".join(list ( capturaSimbolos.get()))

        base = añadirMayusculasSiHayIndicacion() + añadirNumerosSiHayIndicacion() + letrasminuscula + stringSimbolos

        muestra = random.sample(base, int ( tamañoContraseña.get()))
        password = "".join(muestra) 
        contraseñaGenerada.set(password)

    except ValueError:
        MessageBox.showerror("Error",  " Debes colocar un tamaño de contraseña valido, \n puede tener hasta 58 caracteres. ")


        

def añadirMayusculasSiHayIndicacion():
    global letrasmayus
    if (int(hayMayusculas.get() ) == 1):
        return letrasmayus
    else:
        return ""


def añadirNumerosSiHayIndicacion():
    global numeros
    if( int (hayEnteros.get()) == 1):
        return numeros
    else:
        return ""





#los labels 
cuadroSimbolos = Label ( raiz, text="Simbolos a usar (opcional):  ")
cuadroSimbolos.grid( row = 1, column = 0 , sticky ="" , pady = 30 , padx = 10)


cuadroTamaño = Label ( raiz, text="Tamaño contraseña:  ")
cuadroTamaño.grid( row = 0, column = 0 , pady = 30 , padx = 10)

#los entry
cuadroEntradaSimbolos=Entry(raiz, textvariable= capturaSimbolos, width= 40).place(x=170, y=115) 
cuadroEntradaTamaño=Entry(raiz, textvariable=tamañoContraseña, width= 10 ).place(x=170, y=30) 

cuadroRespuesta=Entry(raiz, textvariable= contraseñaGenerada, width= 50).place(x=90, y=310) 


#botones
botonGenerar=Button(raiz, text="Generar contraseña", command= lambda:mostrarContraseña()).place(x=160, y=360) 

C1 = Checkbutton(raiz, text = "Usar mayusculas", variable= hayMayusculas, onvalue = 1, offvalue = 0, height=5, width = 20).place(x=145, y=150) 
C2 = Checkbutton(raiz, text = "Usar números ", variable= hayEnteros, onvalue = 1, offvalue = 0, height=5, width = 20).place(x=145, y=210)

raiz.mainloop()
