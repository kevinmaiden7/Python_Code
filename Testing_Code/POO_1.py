class Banda(): # Clase banda
	
	def __init__(self, nombre): # Constructor de la clase
		self.__nombre = nombre # __variable --> Atributo privado
		self.__pais = ""
		self.__numeroIntegrantes = 0
		self.__mejorAlbum = Album()

		# Métodos accesores
	def getNombre(self):
		return(self.__nombre)
	def setNombre(self, nombre):
		self.__nombre = nombre

	def getPais(self):
		return(self.__pais)
	def setPais(self, pais):
		self.__pais = pais

	def getNumIntegrantes(self):
		return(self.__numeroIntegrantes)
	def setNumIntegrantes(self, numeroIntegrantes):
		self.__numeroIntegrantes = numeroIntegrantes

	def getMejorAlbum(self):
		return(self.__mejorAlbum)

		# Otros métodos
	def presentarse(self):
		self.__prepararPresentacion()
		print(self.__nombre + " de " + self.__pais + " y sus " + str(self.__numeroIntegrantes) + 
			" integrantes está tocando en vivo!!!")

	def __prepararPresentacion(self): # __method --> Método privado
		print(self.__nombre + " está preparando su presentación")

# Fin de la clase Banda

class Album(): # Clase Album
	
	def __init__(self): # Constructor
		self.__nombre = ""
		self.__canciones = [] # Lista vacia

	# Métodos accesores
	def getNombre(self):
		return(self.__nombre)
	def setNombre(self, nombre):
		self.__nombre = nombre

	def agregarCancion(self, cancion):
		self.__canciones.append(cancion)
	def getCanciones(self):
		return(self.__canciones)

# Fin de la clase Album

# main
print("\tTESTEANDO POO EN PYTHON\n")
print("Creando un objeto tipo Banda...")
banda1 = Banda("Iron Maiden")
banda1.setPais("UK")
banda1.setNumIntegrantes(6)
print("Objeto creado: " + banda1.getNombre())
banda1.presentarse()
print("Asignando nombre al album")
banda1.getMejorAlbum().setNombre("TNOB")
print("Agregando canciones al album")
banda1.getMejorAlbum().agregarCancion("The Number of the Beast")
banda1.getMejorAlbum().agregarCancion("Hallowed by thy Name")
banda1.getMejorAlbum().agregarCancion("Run to the Hills")
print("canciones agregadas. Resultado:")
print(banda1.getNombre() + ": Album " + banda1.getMejorAlbum().getNombre())
for i in banda1.getMejorAlbum().getCanciones():
	print("- " + i)
print("\nFin del test")
