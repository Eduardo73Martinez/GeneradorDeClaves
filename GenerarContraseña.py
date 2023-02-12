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


# las bases para armar la contraseña con numeros en mayuscula y ninuscula
letrasminuscula = "abcdefghijklmnopqrstwxyz"
letrasmayus = letrasminuscula.upper()
numeros = "0123456789"



def mostrarContraseña():
    try:
        stringSimbolos = "".join(list ( capturaSimbolos.get()))

        base = letrasmayus + letrasminuscula + numeros + stringSimbolos

        muestra = random.sample(base, int ( tamañoContraseña.get()))
        password = "".join(muestra) 
        contraseñaGenerada.set(password)
        
    except ValueError:
        MessageBox.showerror("Error",  "Debes colocar un tamaño de contraseña valido \n puede tener hasta 58 caracteres. ")






#los labels 
cuadroSimbolos = Label ( raiz, text="Simbolos a usar:  ")
cuadroSimbolos.grid( row = 0, column = 0 , sticky ="" , pady = 30 , padx = 10)


cuadroTamaño = Label ( raiz, text="tamaño de la contraseña:  ")
cuadroTamaño.grid( row = 1, column = 0 , pady = 30 , padx = 10)

#los entry
cuadroEntradaSimbolos=Entry(raiz, textvariable= capturaSimbolos, width= 40).place(x=170, y=30) 
cuadroEntradaTamaño=Entry(raiz, textvariable=tamañoContraseña, width= 10 ).place(x=170, y=115) 

cuadroRespuesta=Entry(raiz, textvariable= contraseñaGenerada, width= 50).place(x=90, y=250) 


#botones
botonGenerar=Button(raiz, text="Generar Contraseña", command= lambda:mostrarContraseña()).place(x=200, y=340) 



raiz.mainloop()
