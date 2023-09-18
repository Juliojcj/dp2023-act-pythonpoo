from Textos import Textos

print("Para cada inciso crear una aplicación con el lenguaje Python, utilizando POO.")
print("Problema No.1")

text=Textos()

text.text1=input("1. Ingrese un texto: ")
text.text2=input("2. Ingrese un texto: ")
text.text3=input("3. Ingrese un texto: ")
print("\n\n")

text.mostrarPromedio()
print("\n\n")

text.verLong()
print("\n\n")

text.concatenarTextos()
print("\n\n")

text.concatenarNumeros()