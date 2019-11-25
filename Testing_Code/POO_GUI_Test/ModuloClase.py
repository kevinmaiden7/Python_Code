class Clase():

	def __init__(self, nombreObjeto):
		self.__nombre = nombreObjeto

	def getNombre(self):
		return(self.__nombre)

	def imprimirMensaje(self):
		print("Mensaje desde " + self.__nombre)
