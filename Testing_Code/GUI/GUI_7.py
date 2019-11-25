	# Probando Check Buttons
from tkinter import *

raiz = Tk()
raiz.title("METAL!")
raiz.resizable(False, False)

	# Frames
frameSuperior = Frame(raiz, width=640, height=240)
frameSuperior.grid(row=0, column=0)
frameInferior = Frame(raiz, width=640, height=240)
frameInferior.grid(row=1, column=0)

	# Frame Superior

ironMaiden = IntVar()
metallica = IntVar()
megadeth= IntVar()
lambOfGod = IntVar()

frameTitulo = Frame(frameSuperior, width=640, height=100)
frameTitulo.grid(row=0, column=0)
Label(frameTitulo, text="METAL BANDS!", font=("Arial",13,"bold")).pack()

frameOpciones = Frame(frameSuperior, width=640, height=100)
frameOpciones.grid(row=1, column=0)
Checkbutton(frameOpciones, text="Iron Maiden", variable=ironMaiden, onvalue=1, offvalue=0).grid(row=0, column=0)
Checkbutton(frameOpciones, text="Metallica", variable=metallica, onvalue=1, offvalue=0).grid(row=0, column=1)
Checkbutton(frameOpciones, text="Megadeth", variable=megadeth, onvalue=1, offvalue=0).grid(row=1, column=0)
Checkbutton(frameOpciones, text="Lamb of God", variable=lambOfGod, onvalue=1, offvalue=0).grid(row=1, column=1)

def mostrarImagenes():
	if ironMaiden.get()==1:
		lblImage1.grid()
	else:
		lblImage1.grid_remove()

	if metallica.get()==1:
		lblImage2.grid()
	else:
		lblImage2.grid_remove()

	if megadeth.get()==1:
		lblImage3.grid()
	else:
		lblImage3.grid_remove()

	if lambOfGod.get()==1:
		lblImage4.grid()
	else:
		lblImage4.grid_remove()

frameBoton = Frame(frameSuperior, width=640, height=100)
frameBoton.grid(row=2, column=0)
Button(frameBoton, text="Show", command=mostrarImagenes).pack()

	# Frame Inferior
imagen1 = PhotoImage(file="Maiden.png")
lblImage1 = Label(frameInferior, image=imagen1)
lblImage1.grid(row=0, column=0)

imagen2 = PhotoImage(file="Metallica.png")
lblImage2 = Label(frameInferior, image=imagen2)
lblImage2.grid(row=0, column=1)

imagen3 = PhotoImage(file="Megadeth.png")
lblImage3 = Label(frameInferior, image=imagen3)
lblImage3.grid(row=1, column=0)

imagen4 = PhotoImage(file="LOG.png")
lblImage4 = Label(frameInferior, image=imagen4)
lblImage4.grid(row=1, column=1)

mostrarImagenes()

raiz.mainloop()
