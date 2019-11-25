from tkinter import * # Se importa la librería tkinter

raiz = Tk() # Llamado a la clase Tk
raiz.title("Ventana") # Titulo de la ventana
raiz.geometry("800x480") # Tamaño
raiz.resizable(False, False) # Horizontal, Vertical
raiz.iconbitmap("Icon.ico") # Icono de la ventana
raiz.mainloop() # Habilitar ventana
