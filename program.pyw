from tkinter import *

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Adivina adivinador")


def asignarTexto(a, b):
    return a.config(text=b)
#Funciones cambios de estado. 
# #Español
def cambiarLenguaje():
    ventana.title("Adivina adivinador")
    btnIdiomaMsg.set("Español")
    m = btnCalcMsg.get().split(" ", 1)[1]
    m.join("Step ")
    btnCalcMsg.set(m)

#Ingles
def changeLang():
    # b = btnCalcMsg.get().split(" ", 1)[0]
    msg = btnIdiomaMsg.get()
    ventana.title("Guess Guesser")
    btnIdiomaMsg.set("English")


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
            calculo2()
        case "Paso 1":
            btnCalcMsg.set("Paso 2")
            calculo3()
        case "Paso 2":
            btnCalcMsg.set("Paso 3")
            calculo4()
        case "Paso 3":
            btnCalcMsg.set("Paso 4")
            calculo5()
        case "Paso 4":
            btnCalcMsg.set("Paso 5")
            calculo6()
        case "Paso 5":
            btnCalcMsg.set("Paso 6")
        case "Paso 6":
            btnCalcMsg.set("Comenzar")
            asignarTexto(lblResultado, f"¡{numR}!")
            


        case "Paso x":
            btnCalcMsg.set("Paso -x")
        #ingles
        case "Start":
            btnCalcMsg.set("Step 1")
        case "Step 1":
            btnCalcMsg.set("Step 2")
        case "Step 2":
            btnCalcMsg.set("Step 3")
        case "Step 3":
            btnCalcMsg.set("Step 4")
        case "Step 4":
            btnCalcMsg.set("Step 1")

        
        


def calculo2():
    asignarTexto(textUsuario, "Inverti el orden de las cifras.")
    
def calculo3():
    asignarTexto(textUsuario, "¿El nuevo número es mayor o menor que el primero?")
def calculo4():
    asignarTexto(textUsuario, "Entonces, restá el número que pensaste del nuevo número")
def calculo5():
    asignarTexto(textUsuario, "Ahora sumá las cifras del número que pensaste al principio")
def calculo6():
    asignarTexto(textUsuario, "Decime los números que obtuviste")
    inNumero1.pack()
    inNumero2.pack()
def calculo7():
    num1Cuenta = inNumero1.get()
    num2Cuenta = inNumero2.get()
    inNumero1.pack_forget()
    inNumero2.pack_forget()
    numR = num1Cuenta
    lblResultado.pack()




btnIdiomaMsg = StringVar()
btnCalcMsg = StringVar()
btnIdiomaMsg.set("Español")
btnCalcMsg.set("Comenzar")


#Frame
programFrame = Frame (ventana)
programFrame.pack()

#Botones
btnIdioma = Button(programFrame, textvariable=btnIdiomaMsg, command= cambiarIdiomabtn)
btnIdioma.pack()

btnIngresar = Button(programFrame, textvariable=btnCalcMsg, command=cambiarPaso)
btnIngresar.pack()

#Input
inNumero1 = Entry(programFrame)
#Al hacer click, se borra el texto
inNumero1.bind("<Button-1>", lambda e: inNumero1.delete(0, END))
inNumero1.insert(0, "prueba")

inNumero2 = Entry(programFrame)
#Al hacer click, se borra el texto
inNumero2.bind("<Button-1>", lambda e: inNumero2.delete(0, END))
inNumero2.insert(0, "prueba")


#Label
textUsuario=Label(programFrame, text="Necesito que pienses... Un numero de 2 cifras no iguales.")
textUsuario.pack()
lblResultado=Label(programFrame, text="El numero que pensaste es ...")


ventana.mainloop()