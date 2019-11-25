def dividir(numerador, denominador):
	try:
		return(numerador/denominador)
	except ZeroDivisionError: # Error de division por cero
		print("No se puede dividir entre 0")
		return("Error --> Division por cero")
	finally:
		print("Finalizó la funcion dividir")

print("\tTESTEANDO EXCEPCIONES EN PYTHON\n")
while True:
	try:
		numerador = float(input("Numerador: "))
		denominador = float(input("Denominador: "))
		break
	except ValueError: # Error haciando casting de tipos de datos
		print("No se ingresó correctamente uno de los operandos. Intentelo de nuevo")

print("Resultado: " + str(dividir(numerador, denominador)))
print("Fin del test")
