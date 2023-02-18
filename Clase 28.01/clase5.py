class Vehiculo:
    def __init__(self, nombre: str, placa: str):
        self.nombre = nombre
        self.placa = placa
        self.__vin = None
    @property
    #lectura del valor de una propiedad
    def email(self):
        self.__vin ="prueba"
        return self.nombre + '.' + self.placa + '@gmail.com'
    #asigna valor a una propiedad
    @email.setter 
    def email(self, address):
        valor1 = address[:address.find('.')]
        self.placa = valor1
            
toyota = Vehiculo(nombre = '4Runner',placa = 'P666XXX')
toyota.email = 'toyota@gmail.com'
print(toyota.placa)
print (toyota.email)
print(toyota.nombre+'   '+toyota.placa)