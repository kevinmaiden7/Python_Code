	# Probando Menus y Ventanas Emergentes
from tkinter import *
from tkinter import messagebox # Módulo de Tkinter para desplegar ventanas emergentes

raiz = Tk()
raiz.title("Ventana con Menú")
raiz.resizable(False, False)

barraMenu = Menu(raiz) # Clase Menu de la librería tkinter
raiz.config(menu=barraMenu, width=360, height=280)

	# Acciones
def asignarColorRojo():
	raiz.config(bg="red")
def asignarColorVerde():
	raiz.config(bg="green")
def asignarColorAzul():
	raiz.config(bg="blue")

def mostrarVentInfo():
	messagebox.showinfo("Info", "Informacion...")

def mostrarVentAdvertencia():
	messagebox.showwarning("Warning", "Advertencia...")

def mostrarVentError():
	messagebox.showerror("Error", "Error...")

def mostrarVentPregunta():
	resultado = messagebox.askquestion("Question", "Pregunta...")
	if resultado=="yes":
		print("Respondió afirmativamente")
	else:
		print("Respondió negativamente")

def mostrarVentConfirmar():
	resultado = messagebox.askokcancel("Confirmation", "Pregunta para confirmar...")
	if resultado: print("Se confirmó la acción")
	else: print("No se confirmó la acción")

def salir():
	raiz.destroy() # Cerrar programa

	# Opciones de Menú
opcLista1 = Menu(barraMenu, tearoff=0) # tearoff=0: Quitar barra de referencia
opcLista1.add_command(label="Ventana Informativa", command=mostrarVentInfo) # Agregar una opción a la cascada
opcLista1.add_command(label="Ventana Advertencia", command=mostrarVentAdvertencia)
opcLista1.add_command(label="Ventana Error", command=mostrarVentError)
opcLista1.add_separator() # Agregar separador
opcLista1.add_command(label="Ventana Pregunta", command=mostrarVentPregunta)
opcLista1.add_command(label="Ventana Confirmación", command=mostrarVentConfirmar)
barraMenu.add_cascade(label="Opciones", menu=opcLista1) # Se agrega la cascada a la barra de menú

opcColores = Menu(barraMenu, tearoff=0)
opcColores.add_command(label="Rojo", command=asignarColorRojo)
opcColores.add_command(label="Verde", command=asignarColorVerde)
opcColores.add_command(label="Azul", command=asignarColorAzul)
barraMenu.add_cascade(label="Colores", menu=opcColores)

opcAccion = Menu(barraMenu, tearoff=0)
opcAccion.add_command(label="Cerrar Programa", command=salir)
barraMenu.add_cascade(label="Salir", menu=opcAccion)

raiz.mainloop()
