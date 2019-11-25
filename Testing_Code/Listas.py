lista = ["Metallica", "Megadeth", "Maiden", "Manowar"]
print(type(lista))
print(lista[2])
lista.append("Ghost") # Agrega al final de la lista
print(lista[:]) # Se imprime toda la lista
print("Index of Medageth: ")
print(lista.index("Megadeth"))
print("Index of Ghost: ")
print(lista.index("Ghost"))
print("Metallica" in lista)
print("metallica" in lista)
print("Another" in lista)
lista.remove("Manowar") # Remover un elemento de la lista
print(lista[:])
lista.extend(["Slayer","Sodom"]) # Extension de lista
print(lista[:])
