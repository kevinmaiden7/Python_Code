from tkinter import *

raiz = Tk()
raiz.title("Ventana")
raiz.resizable(False, False)
raiz.iconbitmap("Icon.ico")

frame = Frame(raiz, width="800", height="480", bg="white")
# frame estará contenido en raiz(contenedor)
frame.pack()

label = Label(frame, text="Label 1") # Clase Label de la librería tkinter
label.config(fg="red", font=("Arial", 20, "italic"))
label.place(x=5, y=5)

Label(frame, text="Label 2").place(x=150, y=5)

# Label como imagen
imagen = PhotoImage(file="Maiden_Logo.png") # Clase PhotoImage de la librería tkinter
label = Label(frame, image=imagen).place(x=5, y=100)

raiz.mainloop()
