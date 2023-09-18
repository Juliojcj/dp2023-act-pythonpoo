from Numeros import Numeros

print("Problema No.3")
print("Solicitar 1 valor numérico de base 10 y realizar lo siguiente:")

valor=Numeros()
valor.num=int(input("Ingrese un número: "))

print("a. Calcular y mostrar el factorial del valor ingresado")
valor.calcularFactorial()

print("Indicar si el número es primo.")
valor.verificarPrimo()

print("Indicar si el número es perfecto.")
valor.verificarPerfecto()

print("Convertir el número a binario")
valor.convertirBinario()