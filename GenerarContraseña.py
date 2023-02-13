import random
from tkinter import *
from tkinter import messagebox as MessageBox

raiz= Tk()
raiz.geometry("450x420")
raiz.resizable(0,0)
raiz.title("Generador de contraseñas")
raiz['bg'] = '#83aeab'

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
        MessageBox.showerror("Error",  " Debes colocar un tamaño de contraseña valido, \n puede tener hasta 24 caracteres. ")


        

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

cuadroTamaño = Label ( raiz, text="Cantidad \n caracteres:  ").place(x=10, y=70) 
#cuadroTamaño.grid( row = 0, column = 0 , pady = 30 , padx = 10)


cuadroSimbolos = Label ( raiz, text="Simbolos a usar \n (opcional):  ").place(x=10, y=125) 
#cuadroSimbolos.grid( row = 1, column = 0 , sticky ="" , pady = 30 , padx = 10)




milabel=Label(raiz, text="Especifica los campos", fg="red" ,bg="white", font=("Arial 18", 15),bd="2px").place(x=130, y=5)

#los entry
cuadroEntradaTamaño=Entry(raiz, textvariable=tamañoContraseña, width= 10, font='Arial 15', fg='Grey').place(x=130, y=70) 

cuadroEntradaSimbolos=Entry(raiz, textvariable= capturaSimbolos, width= 25, font='Arial 15', fg='Grey').place(x=130, y=135) 
cuadroRespuesta=Entry(raiz, textvariable= contraseñaGenerada, width= 30, font='Arial 18', fg='Grey').place(x=24, y=330) 


#botones
botonGenerar=Button(raiz, text="Generar contraseña", command= lambda:mostrarContraseña()).place(x=160, y=380) 


Check1 = Checkbutton(raiz, text = "Usar mayusculas", variable= hayMayusculas, onvalue = 1, offvalue = 0, height=0, width = 0, font='Arial 12', fg="red").place(x=130, y=210) 
Check2 = Checkbutton(raiz, text = " Usar números   ", variable= hayEnteros, onvalue = 1, offvalue = 0, height=0, width = 0, font='Arial 12', fg="red").place(x=130, y=280)

raiz.mainloop()
