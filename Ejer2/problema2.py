from Sueldos import Sueldos

print("Problema No.2")
print("Solicitar sueldo base y valor de ventas realizadas, con ello deberá realizar los siguientes cálculos y mostrar los resultados:")

calcular=Sueldos()
calcular.sueldo=float(input("Ingrese el sueldo base: "))
calcular.venta=int(input("Ingrese las ventas realizadas: "))
print("\n\n")

calcular.calcularComision()
calcular.calcularIgss()
calcular.calcularAhorro()
calcular.calcularTotalganado()
calcular.calcularTotaldescuento()
calcular.clacularSueldo()