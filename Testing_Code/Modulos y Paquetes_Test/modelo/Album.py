class Album():
	
	def __init__(self, nombre):
		self.__nombre = nombre
		self.__canciones = []
		self.__duracionTotal = 0

	# Métodos accesores
	def getNombre(self):
		return(self.__nombre)

	def agregarCancion(self, nuevaCancion):
		self.__canciones.append(nuevaCancion)
		self.__actualizarDuracionTotal(nuevaCancion)
		
	def getCanciones(self):
		return(self.__canciones)

	def getDuracionTotal(self):
		return(self.__duracionTotal)

	# Métodos privados
	def __actualizarDuracionTotal(self, nuevaCancion): 
		self.__duracionTotal += nuevaCancion.getDuracion()

# Fin de la clase Album
