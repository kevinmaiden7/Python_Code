	# Probando explorador de archivos
from tkinter import *
from tkinter import filedialog as fd # Módulo de Tkinter para usar un explorador de archivos

raiz = Tk()
raiz.title("Explorador")
raiz.resizable(False, False)

frameSuperior = Frame(raiz, width=360, height=120)
frameSuperior.grid(row=0, column=0)
frameInferior = Frame(raiz, width=360, height=120)
frameInferior.grid(row=1, column=0)

	# Frame superior

archivosPermitidos = ("Imágenes PNG","*.png") # Para filtrar la búsqueda de archivos

def abrirExplorador():
	rutaImagen = fd.askopenfilename(title="Explorador", initialdir="D:", filetypes=[archivosPermitidos])
	# La función askopenfilename retorna la ruta(absoluta) del archivo abierto, no el archivo como tal
	print(rutaImagen) # Informativo
	imagen = PhotoImage(file=rutaImagen)
	lblImage.config(image=imagen)
	lblImage.image=imagen

Label(frameSuperior, text="Seleccionar una imagen (.png)").grid(row=0, column=0)
Button(frameSuperior, text="Abrir explorador", command=abrirExplorador).grid(row=1, column=0)

	# Frame inferior
imagen = PhotoImage(file="Image_PNG.png")
lblImage = Label(frameInferior, image=imagen)
lblImage.pack()
#lblImage.grid(row=0, column=0)

raiz.mainloop()
