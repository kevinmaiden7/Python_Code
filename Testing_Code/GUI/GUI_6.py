	# Probando Radio Buttons
from tkinter import *

raiz = Tk()
raiz.title("Ventana")
#raiz.resizable(False, False)
raiz.config(bg="white")

frame = Frame(raiz, width="600", height="480")
frame.pack()

#
value = IntVar() # Objeto tipo Integer

colores = ["red", "green", "blue", "yellow"]
def cambiarColor():
	raiz.config(bg=colores[value.get()])

Label(frame, text="COLOR").grid(row=0, column=0)
Radiobutton(frame, text="Rojo", variable=value, value=0, command=cambiarColor).grid(row=1, column=0)
Radiobutton(frame, text="Verde",variable=value, value=1, command=cambiarColor).grid(row=2, column=0)
Radiobutton(frame, text="Azul", variable=value, value=2,command=cambiarColor).grid(row=1, column=1)
Radiobutton(frame, text="Amarillo", variable=value, value=3,command=cambiarColor).grid(row=2, column=1)

raiz.mainloop()
