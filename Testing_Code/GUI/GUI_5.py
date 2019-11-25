from tkinter import *

	# Raiz
raiz = Tk()
raiz.title("Programa")
raiz.resizable(False, False)
raiz.config(bg="white")
raiz.iconbitmap("Icon.ico")

padx = 5
pady = 1

	# Frame principal y para el botón

framePrincipal = Frame(raiz, width="800", height="240")
framePrincipal.grid(row=0, column=0)
frameBoton = Frame(raiz, width="800", height="240")
frameBoton.grid(row=1, column=0)

	# Frame1

frame1 = Frame(framePrincipal, width="400", height="240")
frame1.grid(row=0, column=0)

	# Labels
lblF1Info = Label(frame1, text="Datos...")
lblF1Info.config(fg="red")
lblF1Info.grid(row=0, column=0, sticky="e")

lblF1Nombre = Label(frame1, text="Nombre:")
lblF1Nombre.grid(row=1, column=0, sticky="e", padx=padx, pady=pady)

lblF1Edad = Label(frame1, text="Edad:")
lblF1Edad.grid(row=2, column=0, sticky="e", padx=padx, pady=pady)

lblF1Correo = Label(frame1, text="Correo Electrónico:")
lblF1Correo.grid(row=3, column=0, sticky="e", padx=padx, pady=pady)

lblF1Clave = Label(frame1, text="Contraseña:")
lblF1Clave.grid(row=4, column=0, sticky="e", padx=padx, pady=pady)

	# Entries
entryNombre = Entry(frame1)
entryNombre.grid(row=1, column=1, padx=padx)

entryEdad = Entry(frame1)
entryEdad.grid(row=2, column=1, padx=padx)

entryCorreo = Entry(frame1)
entryCorreo.grid(row=3, column=1, padx=padx)

entryClave = Entry(frame1)
entryClave.grid(row=4, column=1, padx=padx)
entryClave.config(show="*")

	# Frame2

fuente = ("Calibri", 10, "italic")
nombre = StringVar() # Especificar que la variable es una cadena de caracteres(Objeto String)
edad = StringVar()
correo = StringVar()
clave = StringVar()

frame2 = Frame(framePrincipal, width="400", height="240")
frame2.grid(row=0, column=1)

	# Labels
lblF2Info = Label(frame2, text="Datos ingresados...")
lblF2Info.config(fg="red", font=fuente)
lblF2Info.grid(row=0, column=0)

lblF2Nombre = Label(frame2, textvariable=nombre) # Asociar widget(en este caso un label) a una variable
lblF2Nombre.grid(row=1, column=0, sticky="e", padx=padx, pady=pady)

lblF2Edad = Label(frame2, textvariable=edad)
lblF2Edad.grid(row=2, column=0, sticky="e", padx=padx, pady=pady)

lblF2Correo = Label(frame2, textvariable=correo)
lblF2Correo.grid(row=3, column=0, sticky="e", padx=padx, pady=pady)

lblF2Clave = Label(frame2, textvariable=clave)
lblF2Clave.grid(row=4, column=0, sticky="e", padx=padx, pady=pady)

	# Frame botones

def accionar():
	nombreIngresado = entryNombre.get()
	edadIngresada = entryEdad.get()
	correoIngrasado = entryCorreo.get()
	claveIngresada = entryClave.get()
	nombre.set(nombreIngresado)
	edad.set(edadIngresada)
	correo.set(correoIngrasado)
	clave.set(claveIngresada)

def limpiar():
	nombre.set("")
	edad.set("")
	correo.set("")
	clave.set("")

btnAccion = Button(frameBoton, text="Accion", command=accionar)
btnAccion.grid(row=0, column=0)

btnLimpiar = Button(frameBoton, text="Limpiar", command=limpiar)
btnLimpiar.grid(row=0, column=1)

raiz.mainloop()
