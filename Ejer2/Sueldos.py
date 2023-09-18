class Sueldos:
    comision=0
    igss=0.0
    ahorro=0
    totalG=0
    totalD=0
    sueldoL=0
    venta=0
    sueldo=0.0

    def calcularComision(self):
        self.comision=(self.venta*0.10)
        print("Comisión por ventas (10% del total vendido), ",self.comision)

    def  calcularIgss(self):
        self.igss=((4.83*self.sueldo)/100)
        print("IGSS (4.83% del sueldo base) ",self.igss)

    def calcularAhorro(self):
        self.ahorro=((self.sueldo+self.comision)*0.07)
        print("Ahorro (7% del total ganado) ",round(self.ahorro,2))
    
    def calcularTotalganado(self):
        self.totalG=self.sueldo+self.comision
        print("Total ganado = sueldo base + comisión por ventas + bonificación. ",self.totalG)

    def calcularTotaldescuento(self):
        self.totalD=(self.ahorro+self.igss)
        print("Total descuentos = ahorro + IGSS. ",round(self.totalD,2))

    def clacularSueldo(self):
        self.sueldoL=self.totalG-self.totalD
        print("Sueldo liquido = Total ganado – total descuentos.",round(self.sueldoL,2))