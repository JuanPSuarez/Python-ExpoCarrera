from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Adivina, adiviniador")



programaFr = Frame(ventana).pack()

lang = StringVar()
lang.set("Español")
#Messages.
    #Texto principal y texto botones.
class msj:
    if lang.get() == "Español":
        msg0 = "Bienvenido, voy a adivinar el numero que pienses c:"
        msg1 = "Necesito que pienses... Un numero de 2 cifras no iguales."
        msg2 = "Inverti el orden de las cifras."
        msg3 = "¿El nuevo número es mayor o menor que el primero?."
        msg4 = "Entonces, restá el número que pensaste del nuevo número?."
        msg5 = "Ahora sumá las cifras del número que pensaste al principio."
        msg6 = "Decime los números que obtuviste."
        msg7 = "El numero es..."

        bmsg0 = "Comenzar"
        bmsg1 = "Siguiente"
        bmsg2 = "Calcular"
        bmsg3 = "Finalizar"

        msgBRadioMay = "Mayor"
        msgBRadioMen = "Menor"
    else:
        msg0 = "Welcome..."
        msg1 = "Think of a two-digit number (not equal)."
        msg2 = "Now reverse the order of the figures."
        msg3 = "Is the new number higher or lower than the first?."
        msg4 = "So, subtract the number you thought first from the new number."
        msg5 = "ow add the numbers of the number you thought at the beginning."
        msg6 = "Type the numbers you got ."
        msg7 = "The number is...."

        bmsg0 = "Start"
        bmsg1 = "Next"
        bmsg2 = "Calculate"
        bmsg3 = "Finish"

        msgBRadioMay = "Major"
        msgBRadioMen = "Minor"

#Sets
txtPrincipalVar = StringVar()
txtPrincipalVar.set(msj.msg0)

txtResultadoVar = StringVar()
txtResultadoVar.set("")

BotonRadioMenor = StringVar()
BotonRadioMenor.set(msj.msgBRadioMay)
BotonRadioMayor = StringVar()
BotonRadioMayor.set(msj.msgBRadioMen)

radioVar = StringVar()
radioVar.set(" ")

btnVar = StringVar()
btnVar.set(msj.bmsg0)




#Funciones

def calcularRTA(n1, n2):

    n1  = int(n1)
    n2 = int(n2)
    pivot = n1 / 9
    if radioVar.get() == 1:
        d1 = (n2 - pivot) / 2
        d2 = (n2 + pivot) / 2
        res = int(d1) * 10 + int(d2)

    
    else:
        radioVar.get() == 2
        d1 = (n2 - pivot) / 2
        d2 = (n2 + pivot) / 2
        res = int(d2) * 10 + int(d1)
    return res



def states ():
    msg = txtPrincipalVar.get()
    match msg:
        case msj.msg0:
            txtPrincipalVar.set(msj.msg1)
            btnVar.set(msj.bmsg1)
        case msj.msg1:
            txtPrincipalVar.set(msj.msg2)
        case msj.msg2:
            txtPrincipalVar.set(msj.msg3)
            radioMayor.pack()
            radioMenor.pack()
        case msj.msg3:
            try:
                int(radioVar.get())
                txtPrincipalVar.set(msj.msg4)
                radioMayor.pack_forget()
                radioMenor.pack_forget()
            except ValueError:
                messagebox.showerror(title="Opcion inválida.", message="Seleccione si es mayor o menor.")
        case msj.msg4:
            txtPrincipalVar.set(msj.msg5)
        case msj.msg5:
            txtPrincipalVar.set(msj.msg6)
            btnVar.set(msj.bmsg2)
            num1Form.pack()
            num2Form.pack()   
        case msj.msg6:
            try:
                int(num1Form.get()) and int(num2Form.get())
                txtPrincipalVar.set(msj.msg7)
                btnVar.set(msj.bmsg3)
                num1Form.pack_forget()
                num2Form.pack_forget()  
                a = (calcularRTA((num1Form.get()), num2Form.get()))
                txtResultadoVar.set(a)
            except ValueError:
                messagebox.showerror(title="INGRESO INCORRECTO", message="No se acepta campos vacios o caracteres que no sean números.")
        case msj.msg7:
            txtPrincipalVar.set(msj.msg0)
            btnVar.set(msj.bmsg0)
            txtResultadoVar.set("")
            radioVar.set("")

def changeLang():
    if lang.get() == "Español":
        lang.set("English")
    else:
        lang.set("Español")
    return lang



#Label

textoPrincipal = Label(programaFr, textvariable=txtPrincipalVar).pack()
textoResultado = Label(programaFr, textvariable=txtResultadoVar).pack()

#Radio Button
radioMayor = Radiobutton(programaFr, textvariable=BotonRadioMayor,variable =radioVar, value=1)
radioMenor = Radiobutton(programaFr, textvariable=BotonRadioMenor,variable =radioVar, value=2)

#Button
next = Button(programaFr, textvariable=btnVar, command=states).pack()
idioma = Button(programaFr, textvariable=lang, command=changeLang).pack()
#Entrada
num1Form = Entry(programaFr)
num2Form = Entry(programaFr)

#Imagen
isauiImg = ImageTk.PhotoImage(Image.open("isauiLogo.png"))
isauiLBL = Label(programaFr, image = isauiImg).place(anchor="sw",relx=0, rely=1)


ventana.mainloop()