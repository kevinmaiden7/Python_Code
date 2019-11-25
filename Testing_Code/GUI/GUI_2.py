from tkinter import *

raiz = Tk()
raiz.title("Ventana con Frame")
#raiz.resizable(False, False)
frame = Frame() # Clase Frame de la librería Tkinter
frame.pack() # Se "empaqueta" el frame en la raiz
frame.config(width="800", height="480") 
# La raiz se adapta inicialmente al tamaño del frame
frame.config(bg="white")
raiz.mainloop()
