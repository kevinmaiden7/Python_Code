print("\tPROBANDO CICLO FOR\n")
albumes = ["TNOB", "Master of Puppets", "Rust in Peace", "Peace Sells", "Powerslave"]
bandas = ["Iron Maiden", "Metallica", "Megadeth", "Megadeth", "Iron Maiden"]
print("Prueba albumes:")
contador = 0
for i in albumes: # Declaracion de ciclo for
	print(str(contador + 1) + ". " + i + " : " + bandas[contador])
	contador+=1
print("Fin de lista\n")
print("Recorriendo un String(cadena de caracteres)")
cadena = input("Ingrese una cadena de caracteres: ")
print("Se va a imprimir " + cadena + " caracter a caracter y en minuscula")
print("Longitud de cadena: " + str(len(cadena)))
for i in cadena:
	char = i.lower() # Funcion para convertir a minuscula
	# para convertir a mayuscula: upper()
	print(char)
print("Fin del proceso\n")
print("Mejorando la prueba de albumes usando range()")
for i in range(5):
	print(str(i+1)+". " + albumes[i] + " : " + bandas[i])
print("Fin de la lista\n")
