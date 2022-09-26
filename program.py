from tkinter import *

ventana = Tk()
ventana.geometry("300x300")


def changeLang():
    b = btnCalcMsg.get()
    c = b.split(" ", 1)[0]
    print(c)
    
        

def cambiarIdiomabtn():
    if btnIdiomaMsg.get()  == "Español":
        btnIdiomaMsg.set("English")
        changeLang()
    else:
        btnIdiomaMsg.set("Español")

def cambiarPaso():
    match btnCalcMsg.get():
        case "Paso 1":
            btnCalcMsg.set("Paso 2")
        case "Paso 2":
            btnCalcMsg.set("Paso 3")
        case "Paso 3":
            btnCalcMsg.set("Paso 4")
        case "Paso 4":
            btnCalcMsg.set("Paso 1")
        #ingles
        case "Step 1":
            btnCalcMsg.set("Step 2")
        case "Step 2":
            btnCalcMsg.set("Step 3")
        case "Step 3":
            btnCalcMsg.set("Step 4")
        case "Step 4":
            btnCalcMsg.set("Step 1")

        
        


def calculo1():
    pass
def calculo2():
    pass
def calculo3():
    pass
def calculo4():
    pass


btnIdiomaMsg = StringVar()
btnCalcMsg = StringVar()
btnIdiomaMsg.set("Español")
btnCalcMsg.set("Paso 1")


#Frame
programFrame = Frame (ventana)
programFrame.pack()

#Botones
btnIdioma = Button(programFrame, textvariable=btnIdiomaMsg, command= cambiarIdiomabtn)
btnIdioma.pack()

btnIngresar = Button(programFrame, textvariable=btnCalcMsg, command=cambiarPaso)
btnIngresar.pack()

#Input
inNumero = Entry(programFrame)
    #Al hacer click, se borra el texto
inNumero.bind("<Button-1>", lambda e: inNumero.delete(0, END))
inNumero.insert(0, "prueba")
inNumero.pack()

ventana.mainloop()