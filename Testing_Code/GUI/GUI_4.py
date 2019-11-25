from tkinter import *

raiz = Tk()
raiz.title("Ventana")
raiz.config(bg="white")
#raiz.resizable(False, False)

frame = Frame(raiz, width="800", height="480")
frame.pack()

	# Labels
lblNombre = Label(frame, text="Nombre:")
lblNombre.grid(row=0, column=0, sticky="e", padx=5, pady=1) # sticky = alineación

lblCorreo = Label(frame, text="Correo Electrónico:")
lblCorreo.grid(row=1, column=0, sticky="e", padx=5, pady=1)

lblClave = Label(frame, text="Contraseña:")
lblClave.grid(row=2, column=0, sticky="e", padx=5, pady=1)

	# Entries
entryNombre = Entry(frame) # Clase Entry de la librería tkinter
entryNombre.grid(row=0, column=1, padx=5)

entryCorreo = Entry(frame)
entryCorreo.grid(row=1, column=1, padx=5)

entryClave = Entry(frame)
entryClave.grid(row=2, column=1, padx=5)
entryClave.config(show="*")

raiz.mainloop()
