import math

# No considera el 1 como primo
def esPrimo(numero):
	if (numero < 2) or (((numero % 2) == 0) and (numero != 2)):
		return(False)
	if (numero == 2) or (numero == 3):
		return(True)
	raiz = int(math.sqrt(numero))
	for i in range(3, (raiz + 1)):
		if (numero % i) == 0: 
			return(False)
	return(True)

def generadorDePrimos(): # Generador
	numero = 2
	while True:
		if esPrimo(numero):
			yield numero # Se produce (y se retorna) un nuevo elemento
			# Se suspende el generador
		numero += 1

print("\tTESTEANDO GENERADORES EN PYTHON\n")
objetoGenerador = generadorDePrimos()
primo = next(objetoGenerador) # Generar nuevo elemento
print("Se genero el primer primo: " + str(primo))
decision = input("Generar otro primo (S/N): ")
while (decision == "S") or (decision == "s"):
	primo = next(objetoGenerador) # Generar nuevo elemento
	print("Nuevo primo: " + str(primo))
	decision = input("Generar otro primo (S/N): ")
print("Fin del programa")
