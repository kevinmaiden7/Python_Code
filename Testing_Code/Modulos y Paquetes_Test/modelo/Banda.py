class Banda():

	def __init__(self, nombre, pais):
		self.__nombre = nombre
		self.__pais = pais
		self.__albumes = []

	# Métodos accesores
	def getNombre(self):
		return(self.__nombre)

	def getPais(self):
		return(self.__pais)

	def agregarAlbum(self, nuevoAlbum):
		self.__albumes.append(nuevoAlbum)
	def getAlbumes(self):
		return(self.__albumes)

# Fin de la clase Banda
