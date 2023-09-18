class Numeros:
    num=0
    fact=1
    contador=0
    suma=0
    num1=0

    def calcularFactorial(self):
        for i in range(1,self.num+1):
            self.fact=self.fact*i
        print("El factoriqal del ",self.num," es ", (self.fact))
        print("\n\n")

    def verificarPrimo(self):
        if self.num>1:
            for i in range(2,self.num):
                if (self.num % i) == 0:
                    print("El ",self.num," no es un número primo")
                    break
            else:
                print("El ", self.num," es un número primo")
        else:
            print("El ",self.num," no es un número primo")
            print("\n\n")

    def verificarPerfecto(self):
        for i in range(1, self.num):
            if (self.num % i == 0):
                self.suma=self.suma+i
        if(self.suma== self.num):
            print("El número ingresado es perfecto: ",self.num)
        else:
            print("El número ingresado no es perfecto: ",self.num)
            print("\n\n")

    def convertirBinario(self):
        binarios=[]
        self.num1=self.num
        while self.num1!=0:
            binario=self.num1%2
            self.cociente=self.num1//2
            binarios.append(binario)
            self.num1=self.cociente
        print("El número convertido es: ",self.num)
        print(binarios)