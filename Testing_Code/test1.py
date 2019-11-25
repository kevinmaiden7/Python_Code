def funcionBasica(): # Declaracion de funcion
	print("Print desde la funcion")

def potenciaDos(exponente):
	print(2**exponente)

def funcionPiso(numerador, denominador):
	return(numerador // denominador)

def aumentarValor(numero):
	numero += 1
	print("Print desde aumentarValor()")
	print(numero)
	print("---------------------------")

saludo = "Saludos desde Python!"
print(saludo)
numero1 = 20
numero2 = 6
print(numero1)
print(numero2)
if numero1 > numero2:
	print("El numero 1 es mayor que el numero 2")
else:
	print("El numero 2 es mayor que el numero 1")
print("End")
funcionBasica()
print("----------------------")
funcionBasica()
print("Se va a invocar la funcion potenciaDos:")
potenciaDos(5)
potenciaDos(6)
potenciaDos(10)
print("Se va a invocar funcionPiso:")
print(funcionPiso(32,7))
resultado = funcionPiso(64,10)
print(resultado)
print("Se va a invocar aumentarValor:")
numero = 20
aumentarValor(numero)
print("Print afuera de aumentarValor()")
print(numero)
