from Vista import configurarInterfaz, iniciarInterfaz
from ModuloClase import Clase
from ModuloClase2 import Clase2

def funcionF():
	print("FUNCION!!")

titulo = "CONFIGURADO\nDESDE PRINCIPAL"
raiz = configurarInterfaz(titulo)

for i in range(5):
	print(i)

print("ANTES DE INICIAR LA INTERFAZ")
iniciarInterfaz(raiz)
funcionF()
print("FIN INTERFAZ\n")

objeto = Clase("objeto1")
print("Nombre asignado : " + objeto.getNombre())
objeto.imprimirMensaje()
objeto2 = Clase2()
objeto2.imprimirMensaje("Soy el objeto 2")
print("Fin del Test")
