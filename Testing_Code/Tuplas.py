info = ("Kevin",9,12,1997) # Tupla
print("Nombre: " + info[0])
print("Dia: " + str(info[1]))
print("Mes: " + str(info[2]))
print("Año: " + str(info[3]))
print("--------------------")
tupla1 = ("info1", "info2", 1, 1, 0.5)
lista1 = list(tupla1) # Convirtiendo una tupla en lista
# para convertir una lista en tupla: tuple()
print("Imprimiendo tupla")
print(tupla1)
print("Imprimiendo lista")
print(lista1)
print("Buscando valores")
print("info2" in tupla1)
print(0 in tupla1)
print(1 in tupla1)
total = tupla1.count(1) # Numero de veces que aparece un elemento en una tupla
print("Numero de veces que aparece el 1: " + str(total))
longitud = len(tupla1) # Numero de elementos en una tupla
print("Longitud de la tupla1: " + str(longitud))
print("--------------------")
print("Tupla 2:")
tupla2 = ("Elemento1", "Elemento2", "Elemento3", 20)
var1, var2, var3, num = tupla2 # Desempaquetado de tupla
print(var1 + " " + var2 + " " + var3 + " " + str(num))
print(tupla2.index("Elemento3")) # index() tambien funciona para listas
lista2 = list(tupla2)
print(lista2)
print(lista2.index(20))
print(lista2.index("Elemento1"))
