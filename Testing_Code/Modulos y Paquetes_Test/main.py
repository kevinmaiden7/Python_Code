from modelo.Banda import Banda
from modelo.Album import Album
from modelo.Cancion import Cancion

def mostrarAlbum(banda, album):
	print(banda.getNombre() + " (" + banda.getPais() + ") - " + album.getNombre())
	contador = 1
	for cancion in album.getCanciones():
		print(str(contador) + ". " + cancion.getTitulo() + " : " 
			+ str(cancion.getDuracion()) + " minutos")
		contador += 1
	print("Duracion total = " + str(album.getDuracionTotal()) + " minutos\n")

banda = Banda("Iron Maiden", "UK")
print("Se creó la banda: " + banda.getNombre())
album = Album("The Number of the Beast")
cancion = Cancion("The Number of The Beast", 4.50)
album.agregarCancion(cancion)
cancion = Cancion("Run to the Hills", 3.52)
album.agregarCancion(cancion)
cancion = Cancion("Hallowed Be Thy Name", 7.10)
album.agregarCancion(cancion)
banda.agregarAlbum(album)
print("Se creó el album " + album.getNombre() + " y se agregaron varias canciones")
album = Album("Powerslave")
cancion = Cancion("Aces High", 4.29)
album.agregarCancion(cancion)
cancion = Cancion("The Duellists", 6.06)
album.agregarCancion(cancion)
cancion = Cancion("Powerslave", 7.12)
album.agregarCancion(cancion)
cancion = Cancion("Rime of the Ancient Mariner", 13.42)
album.agregarCancion(cancion)
banda.agregarAlbum(album)
print("Se creó el album " + album.getNombre() + " y se agregaron varias canciones\n")
for album in banda.getAlbumes():
	mostrarAlbum(banda, album)
print("Fin del test")
