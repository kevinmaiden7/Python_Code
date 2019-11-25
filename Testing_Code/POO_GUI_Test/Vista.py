from tkinter import *
from Utilidad import imprimirMensaje
#from Principal import funcionF

def solicitarImpresion():
	imprimirMensaje("Invocado desde la vista")

def configurarInterfaz(titulo):
	raiz = Tk()
	raiz.title("Ventana")
	#raiz.resizable(False, False)

	frame = Frame(raiz, width="480", height="360")
	frame.pack()

	Label(frame, text=titulo).grid(row=0, column=0)
	Button(frame, text="Accionar", command=solicitarImpresion).grid(row=1, column=0)
	#Button(frame, text="Accionar2", command=funcion).grid(row=2, column=0)
	Label(frame, text="--------").grid(row=3, column=0)

	#raiz.mainloop()
	return(raiz)

def iniciarInterfaz(raiz):
	raiz.mainloop()
	