from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("500x200")
ventana.title("Adivina adivinador")
ventana.config(bg="white")

mayorOmenor = IntVar()



Lenguaje = bool


def calcularRTA(n1, n2):

    pivot = n1 / 9

    if mayorOmenor.get() == 1:
         d1 = (n2 - pivot) / 2
         d2 = (n2 + pivot) / 2
         rta = int(d1) * 10 + int(d2)
    
    if mayorOmenor.get() == 2:
         d1 = (n2 - pivot) / 2
         d2 = (n2 + pivot) / 2
         rta = int(d2) * 10 + int(d1)

    return rta


def asignarTexto(a, b):
    return a.config(text=b)
#Funciones cambios de estado. 
# #Español
def cambiarLenguaje():
    ventana.title("Adivina adivinador")
    btnIdiomaMsg.set("Español")
    # m = btnCalcMsg.get().split(" ", 1)[1]
    # m.join("Step ")
    # btnCalcMsg.set(m)
    match btnCalcMsg.get():
        case "Start":
            btnCalcMsg.set("Comenzar")
        case "Step 1":
            btnCalcMsg.set("Paso 1")
        case "Step 2":
            btnCalcMsg.set("Paso 2")
        case "Step 3":
            btnCalcMsg.set("Paso 3")
        case "Step 4":
            btnCalcMsg.set("Paso 4")
        case "Step 5":
            btnCalcMsg.set("Paso 5")
        case "Step 6":
            btnCalcMsg.set("Paso 6")
        case "Finish":
            btnCalcMsg.set("Finalizar")



#Ingles
def changeLang():
    # b = btnCalcMsg.get().split(" ", 1)[0]
    ventana.title("Guess Guesser")
    btnIdiomaMsg.set("English")
    match btnCalcMsg.get():
        case "Comenzar":
            btnCalcMsg.set("Start")
        case "Paso 1":
            btnCalcMsg.set("Step 1")
        case "Paso 2":
            btnCalcMsg.set("Step 2")
        case "Paso 3":
            btnCalcMsg.set("Step 3")
        case "Paso 4":
            btnCalcMsg.set("Step 4")
        case "Paso 5":
            btnCalcMsg.set("Step 5")
        case "Paso 6":
            btnCalcMsg.set("Step 6")
        case "Finalizar":
            btnCalcMsg.set("Finish")


#Se lee en que estado esta el boton idioma.
def cambiarIdiomabtn():
    if btnIdiomaMsg.get()  == "Español":
        changeLang()
    else:
        cambiarLenguaje()
        

#Se cambia paso. Se usa switch. python 3.10
def cambiarPaso():

    
    match btnCalcMsg.get():
        case "Comenzar":
            btnCalcMsg.set("Paso 1")
            calculo1()
        case "Paso 1":
            btnCalcMsg.set("Paso 2")
            calculo2()
        case "Paso 2":
            btnCalcMsg.set("Paso 3")
            calculo3()
        case "Paso 3":
            btnCalcMsg.set("Paso 4")
            calculo4()
        case "Paso 4":
            btnCalcMsg.set("Paso 5")
            calculo5()
        case "Paso 5":
            btnCalcMsg.set("Paso 6")
            calculo6()
        case "Paso 6":
            btnCalcMsg.set("Finalizar")
            calculo7()
        case "Finalizar":
            btnCalcMsg.set("Comenzar")
            calculo8()
            


        case "Start":
            btnCalcMsg.set("Step 1")
            calculo1()
        case "Step 1":
            btnCalcMsg.set("Step 2")
            calculo2()
        case "Step 2":
            btnCalcMsg.set("Step 3")
            calculo3()  
        case "Step 3":
            btnCalcMsg.set("Step 4")
            calculo4()
        case "Step 4":
            btnCalcMsg.set("Step 5")
            calculo5()
        case "Step 5":
            btnCalcMsg.set("Step 6")
            calculo6()
        case "Step 6":
            btnCalcMsg.set("Finish")
            calculo7()
        case "Finish":
            btnCalcMsg.set("Start")
            calculo8()

        
        
def asd():
    pass


def calculo1():
    if Lenguaje != True:
        asignarTexto(textUsuario, "Necesito que pienses... Un numero de 2 cifras no iguales.")
    else:
        asignarTexto(textUsuario, "Think of a two-digit number (not equal).")

def calculo2():
    if Lenguaje != True:
        asignarTexto(textUsuario, "Inverti el orden de las cifras.")
    else:
        asignarTexto(textUsuario, "Now reverse the order of the figures.")


def calculo3():
    if Lenguaje != True:
        asignarTexto(textUsuario, "¿El nuevo número es mayor o menor que el primero?")
    else:
        asignarTexto(textUsuario, "Is the new number higher or lower than the first")

    RadioMenor.grid()
    RadioMayor.grid()

    
def calculo4():


        if Lenguaje != True:
            asignarTexto(textUsuario, "Entonces, restá el número que pensaste del nuevo número?")
        else:
            asignarTexto(textUsuario, "So, subtract the number you thought first from the new number.")

        RadioMenor.grid_remove()
        RadioMayor.grid_remove()

    
def calculo5():


    asignarTexto(textUsuario, "Ahora sumá las cifras del número que pensaste al principio")
def calculo6():
    asignarTexto(textUsuario, "Decime los números que obtuviste")
    inNumero1.grid()
    inNumero2.grid()
def calculo7(): #Calculo final.
    asignarTexto(textUsuario, "El numero es...")   
    inNumero1.grid_remove()
    inNumero2.grid_remove()
    lblResultado.grid()
    numR=calcularRTA(int(inNumero1.get()), int(inNumero2.get()))
    asignarTexto(lblResultado, f"¡{numR}!")
def calculo8():
    asignarTexto(textUsuario, "Necesito que pienses... Un numero de 2 cifras no iguales.")
    asignarTexto(lblResultado, "")



btnIdiomaMsg = StringVar()
btnCalcMsg = StringVar()
btnIdiomaMsg.set("Español")
btnCalcMsg.set("Comenzar")

if btnCalcMsg.get() == "Español":
    Lenguaje == True
else:
    Lenguaje == False

#-------------------------------

#imagen
# img = PhotoImage("./download.png")
# imglbl = Label(ventana, img)
# imglbl.pack()


#Frame
programFrame = Frame (ventana, bg="white")
programFrame.pack()

#Botones
btnIdioma = Button(programFrame, textvariable=btnIdiomaMsg, command= cambiarIdiomabtn)
btnIdioma.grid(sticky="nsew")

btnIngresar = Button(programFrame, textvariable=btnCalcMsg, command=cambiarPaso)
btnIngresar.grid()

#Input
inNumero1 = Entry(programFrame)
#Al hacer click, se borra el texto
inNumero1.bind("<Button-1>", lambda e: inNumero1.delete(0, END))
inNumero1.insert(0, "Primer numero")

inNumero2 = Entry(programFrame)
#Al hacer click, se borra el texto
inNumero2.bind("<Button-1>", lambda e: inNumero2.delete(0, END))
inNumero2.insert(0, "Segundo Numero")

#RadioButton
RadioMayor = Radiobutton(programFrame, variable=mayorOmenor, text="Mayor", value=1)
RadioMenor = Radiobutton(programFrame, variable=mayorOmenor, text="Menor", value=2)

#Label
textUsuario=Label(programFrame, text="Bienvenido, voy a adivinar el numero que pienses c:")
textUsuario.grid()
lblResultado=Label(programFrame, text="El numero que pensaste es ...")

# if btnIdiomaMsg.get()  == "Español":
#         Lenguaje = True
# else:
#     Lenguaje = False


ventana.mainloop()