class Cancion():

	def __init__(self, titulo, duracion):
		self.__titulo = titulo
		self.__duracion = duracion

	# Métodos accesores
	def getTitulo(self):
		return(self.__titulo)

	def getDuracion(self):
		return(self.__duracion)

# Fin de la clase Cancion
