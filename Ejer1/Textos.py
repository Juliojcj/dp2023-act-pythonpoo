import re
class Textos:
    text1=""
    text2=""
    text3=""
    long=0
    cont=0

    def mostrarPromedio(self):
        self.long=(len(self.text1)+ len(self.text2)+ len(self.text3))/3
        print("a. Mostrar el promedio de las longitudes de los textos es: ",self.long)

    def verLong(self):
        self.long=len(self.text1) + len(self.text2) + len(self.text3)
        if self.long>15:
            print("El largo es mayor a 15")
        elif(self.long<15):
            print("El largo es menor a 15")
        else:
            print("El largo es igual a 15")

    def concatenarTextos(self):
        self.cont=self.text1+" "+self.text2+" "+self.text3
        print("Concatenar los textos")
        print(self.cont)
    
    def  concatenarNumeros(self):
        self.cont=self.text1+" "+self.text2+" "+self.text3
        print("Concatenar los textos")
        print(self.cont)
        self.contntext=lambda x: len(re.findall("[0-9]", str(x)))
        print("indicar la cantidad de caracteres numéricos existentes.")
        print(self.contntext(self.cont)) 