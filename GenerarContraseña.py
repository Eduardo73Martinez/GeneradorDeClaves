import random
from tkinter import *
from tkinter import messagebox as MessageBox

raiz= Tk()
raiz.geometry("450x420")
raiz.resizable(0,0)
raiz.title("Generador de contraseñas")
#raiz['bg'] = '#83aeab'

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
    """Describe una contraseña al azar con las cadenas capturadas  y dependiendo de si esta activados los check de
    los números y las mayusculas las agrega a la base para generarla, genera una diferente cada vez que se ejecuta la funcion.

    Requeriments:
        - ninguno.
    Returns:
        Str: una cadena de caracteres.
    """
    try:
        stringSimbolos = "".join(list ( capturaSimbolos.get()))

        base = añadirMayusculasSiHayIndicacion() + añadirNumerosSiHayIndicacion() + letrasminuscula + stringSimbolos

        muestra = random.sample(base, int ( tamañoContraseña.get()))
        password = "".join(muestra) 
        contraseñaGenerada.set(password)

    except ValueError:
        mensajeDeErrorPorEntradasInvalidas()


def mensajeDeErrorPorEntradasInvalidas():
    """Describe un mensaje de erro si no hay entrada de tamaño o si el tamaño pedido es mayor a la base que tenemos
    genera una alerta de campos invalidos.

    Args:
        
    Requeriments:
        - ninguno.
    Returns:
        Str: devuelve un mensaje de error o de advertencia.
    """
    if( hayMayusculaActivada() and not hayNumerosActivado()  ):
        return MessageBox.showwarning("Atencion", "Debes colocar una contraseña menor a {}  caracteres".format(49 + len(capturaSimbolos.get())))

    elif (  not hayMayusculaActivada() and  hayNumerosActivado() ):
        return MessageBox.showwarning("Atencion", "Debes colocar una contraseña menor a {} caracteres".format(35 + len(capturaSimbolos.get())))

    elif ( not hayMayusculaActivada() and not hayNumerosActivado() ):
        return MessageBox.showwarning("Atencion",  " Debes colocar un tamaño de contraseña valido, \n puede tener hasta {} caracteres. ".format(24 + len(capturaSimbolos.get())))
    
    else:
        return MessageBox.showerror("Error ",  " Debes colocar un tamaño de contraseña valido, \n puede tener hasta {} caracteres. ".format(58 + len(capturaSimbolos.get())))

def añadirMayusculasSiHayIndicacion():
    """Describe el abecedario completo en mayuscula si el check esta prendido. si no esta prendido describe un string vacío.

    Requeriments:
        - ninguno.

    Returns:
        Str: el abecedario en mayuscula si el check esta prendido.
    """
    global letrasmayus
    if (hayMayusculaActivada()):
        return letrasmayus
    else:
        return ""


def añadirNumerosSiHayIndicacion():
    """Describe un string de números si el check de números esta activado. En caso contrario devuelve un string vacío.

    Requeriments:
        -ninguno.

    Returns:
        str: un string con numeros del 0 al 9.
    """
    global numeros
    if( hayNumerosActivado()):
        return numeros
    else:
        return ""

def hayNumerosActivado():
    """Indica si el check de números esta activado.

    Returns:
        bool: True si está activado el check en la ventana False en caso contrario.
    """
    return  int (hayEnteros.get()) == 1


def hayMayusculaActivada():
    """Indica si el check de mayúsculas de está activado.

    Returns:
        bool: True si está activado el check en la ventana False en caso contrario.
    """
    return int(hayMayusculas.get() ) == 1


def limpiarCuadroRespuesta():
    """Setea la contraseña generada con un string vacío.

    """
    return contraseñaGenerada.set("")

def limpiarCampos():
    """setea todos los campos de la ventana con un string vacío en aquellos que son de tipo StringVar y
    con un 0 aquellos que son de tipo IntVar.
    """
    contraseñaGenerada.set("")
    capturaSimbolos.set ("")
    hayMayusculas.set( 0)
    hayEnteros.set (0)
    tamañoContraseña.set("")

    
#los labels 

cuadroTamaño = Label ( raiz, text="Cantidad \n caracteres:  ").place(x=10, y=65) 
#cuadroTamaño.grid( row = 0, column = 0 , pady = 30 , padx = 10)


cuadroSimbolos = Label ( raiz, text="Simbolos a usar \n (opcional):  ").place(x=10, y=125) 
#cuadroSimbolos.grid( row = 1, column = 0 , sticky ="" , pady = 30 , padx = 10)



milabel=Label(raiz, text="Crea tu contraseña", fg="black" ,bg="white", font=("Arial 18", 15),bd="2px").place(x=130, y=5)

#los entry
cuadroEntradaTamaño=Entry(raiz, textvariable=tamañoContraseña, width= 10, font='Arial 15', fg='Grey').place(x=130, y=70) 

cuadroEntradaSimbolos=Entry(raiz, textvariable= capturaSimbolos, width= 25, font='Arial 15', fg='Grey').place(x=130, y=135) 
cuadroRespuesta=Entry(raiz, textvariable= contraseñaGenerada, width= 30, font='Arial 18', fg='Grey').place(x=24, y=330) 


#botones
botonGenerar=Button(raiz, text="Generar contraseña", command= mostrarContraseña).place(x=150, y=380) 
botonLimpiar=Button(raiz, text="Borrar contraseña", command= limpiarCuadroRespuesta).place(x=290, y=380) 
botonLimpiarTodos=Button(raiz, text="Limpiar campos", command= limpiarCampos).place(x=30, y=380) 

#check button
Check1 = Checkbutton(raiz, text = "Usar mayúsculas", variable= hayMayusculas, onvalue = 1, offvalue = 0, height=0, width = 0, font='Arial 12', fg="black").place(x=130, y=210) 
Check2 = Checkbutton(raiz, text = " Usar números   ", variable= hayEnteros, onvalue = 1, offvalue = 0, height=0, width = 0, font='Arial 12', fg="black").place(x=130, y=280)

raiz.mainloop()
