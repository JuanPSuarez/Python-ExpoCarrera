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

        Emsg0 = "Welcome..."
        Emsg1 = "Think of a two-digit number (not equal)."
        Emsg2 = "Now reverse the order of the figures."
        Emsg3 = "Is the new number higher or lower than the first?."
        Emsg4 = "So, subtract the number you thought first from the new number."
        Emsg5 = "ow add the numbers of the number you thought at the beginning."
        Emsg6 = "Type the numbers you got ."
        Emsg7 = "The number is...."

        Ebmsg0 = "Start"
        Ebmsg1 = "Next"
        Ebmsg2 = "Calculate"
        Ebmsg3 = "Finish"

        EmsgBRadioMay = "Higher"
        EmsgBRadioMen = "Lower"

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
    if lang.get() == "Español":
        match msg:
            case msj.msg0 | msj.Emsg0:
                txtPrincipalVar.set(msj.msg1)
                btnVar.set(msj.bmsg1)
            case msj.msg1 | msj.Emsg1:
                txtPrincipalVar.set(msj.msg2)
            case msj.msg2:
                txtPrincipalVar.set(msj.msg3)
                radioMayor.pack()
                radioMenor.pack()
            case msj.msg3 | msj.Emsg3:
                try:
                    int(radioVar.get())
                    txtPrincipalVar.set(msj.msg4)
                    radioMayor.pack_forget()
                    radioMenor.pack_forget()
                except ValueError:
                    messagebox.showerror(title="Opcion inválida", message="Seleccione si es mayor o menor.")
            case msj.msg4 | msj.Emsg4:
                txtPrincipalVar.set(msj.msg5)
            case msj.msg5 | msj.Emsg5:
                txtPrincipalVar.set(msj.msg6)
                btnVar.set(msj.bmsg2)
                num1Form.pack()
                num2Form.pack()   
            case msj.msg6 | msj.Emsg6:
                try:
                    int(num1Form.get()) and int(num2Form.get())
                    txtPrincipalVar.set(msj.msg7)
                    btnVar.set(msj.bmsg3)
                    num1Form.pack_forget()
                    num2Form.pack_forget()  
                    a = (calcularRTA((num1Form.get()), num2Form.get()))
                    txtResultadoVar.set(a)
                except ValueError:
                    messagebox.showerror(title="Ingreso incorrecto", message="El formulario solo acepta números.")
            case msj.msg7 | msj.Emsg7:
                txtPrincipalVar.set(msj.msg0)
                btnVar.set(msj.bmsg0)
                txtResultadoVar.set("")
                radioVar.set("")
    else:
        match msg:
            case msj.Emsg0 | msj.msg0:
                txtPrincipalVar.set(msj.Emsg1)
                btnVar.set(msj.Ebmsg1)
            case msj.Emsg1 | msj.msg1:
                txtPrincipalVar.set(msj.Emsg2)
            case msj.Emsg2 | msj.msg2:
                txtPrincipalVar.set(msj.Emsg3)
                radioMayor.pack()
                radioMenor.pack()
            case msj.Emsg3 | msj.msg3:
                try:
                    int(radioVar.get())
                    txtPrincipalVar.set(msj.Emsg4)
                    radioMayor.pack_forget()
                    radioMenor.pack_forget()
                except ValueError:
                    messagebox.showerror(title="Invalid Option", message="Select if the number is higher or lower.")
            case msj.Emsg4 | msj.msg4:
                txtPrincipalVar.set(msj.Emsg5)
            case msj.Emsg5 | msj.msg5:
                txtPrincipalVar.set(msj.Emsg6)
                btnVar.set(msj.Ebmsg2)
                num1Form.pack()
                num2Form.pack()   
            case msj.Emsg6 | msj.msg6:
                try:
                    int(num1Form.get()) and int(num2Form.get())
                    txtPrincipalVar.set(msj.Emsg7)
                    btnVar.set(msj.Ebmsg3)
                    num1Form.pack_forget()
                    num2Form.pack_forget()  
                    a = (calcularRTA((num1Form.get()), num2Form.get()))
                    txtResultadoVar.set(a)
                except ValueError:
                    messagebox.showerror(title="Wrong Input", message="Form only accepts numbers.")
            case msj.Emsg7 | msj.msg7:
                txtPrincipalVar.set(msj.Emsg0)
                btnVar.set(msj.Ebmsg0)
                txtResultadoVar.set("")
                radioVar.set("")
def changeLang():
    if lang.get() != "Español":
        lang.set("Español")
        BotonRadioMayor.set(msj.msgBRadioMay)
        BotonRadioMenor.set(msj.msgBRadioMen)
    else:
        lang.set("English")
        BotonRadioMayor.set(msj.EmsgBRadioMay)
        BotonRadioMenor.set(msj.EmsgBRadioMen)
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