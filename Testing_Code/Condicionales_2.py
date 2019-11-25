print("Probando la concatenacion de operadores de comparacion")
numero1 = int(input("Ingrese el numero1: "))
numero2 = int(input("Ingrese el numero2: "))
numero3 = int(input("Ingrese el numero3: "))
numero4 = int(input("Ingrese el numero4: "))
print("Ingreso correctamente los 4 numeros")
print("Numero 1 = " + str(numero1))
print("Numero 2 = " + str(numero2))
print("Numero 3 = " + str(numero3))
print("Numero 4 = " + str(numero4))
print("Evaluando...")
suma1 = numero1 + numero2
suma2 = numero2 + numero3
suma3 = numero3 + numero4
if (numero1<suma1<suma2<suma3):
	print("Secuencia correcta")
else:
	print("Secuencia incorrecta")
print()
print("Fin del test...")
