def obtenerBinario():
	digito = int(input("Ingrese un digito binario: "))
	while (digito != 1) and (digito != 0): # Uso del operador and
		print("No ingreso un digito binario, intentelo de nuevo")
		digito = int(input("Ingrese un digito binario: "))
	print("Correcto\n")
	return(digito)

print("\tPROBANDO CICLO WHILE Y OPERADORES LOGICOS")
print("Debe ingresar dos digitos binarios\n")
digito1 = obtenerBinario()
digito2 = obtenerBinario()
print("Digitos ingresados: " + str(digito1) + " y " + str(digito2))
print("Operaciones logicas")
print("AND: " + str(digito1 and digito2))
print("OR: " + str(digito1 or digito2))
print("NOT: digito1 = " + str(not digito1) + " | digito2 = " + str(not digito2))
print("Fin de la prueba")
