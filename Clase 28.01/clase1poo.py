#clase 1,2 y 3
from datetime import date 

class Genero:
	def __init__(self, nombre): #inicializa con este metodo la funcion
		self.nombre = nombre

class Habilidades:
	def __init__(self, habilidad:str, desc: str=None):
		self.habilidad = habilidad

class Debilidades:
	def __init__(self, debilidad):
		self.debilidad = debilidad

#ambiente, lugares de desarrollo, clase, casas de produccion 		
class Ambiente:
	def __init__(self,ambiente):
		self.ambiente = ambiente

class LugaresDesarrollo:
	def __init__(self,lugar):
		self.lugar = lugar

class Clases:
	def __init__(self, edadMinima):
		self.edadMinima = edadMinima

class CasaProduccion:
	def __init__(self, casa):
		self.casa = casa

class Personajes:
	def __init__(self, nombre, apellido, sexo, edad, raza, habilidades: Habilidades, debilidades: Debilidades):
		self.nombre = nombre
		self.apellido = apellido
		self.sexo = sexo
		self.edad = edad
		self.raza = raza
		self.habilidades = habilidades
		self.debilidades = debilidades

class Serie:
	def __init__ (self, nombre: str = "", genero: Genero=None, personajes=None, \
		fecha: date=None, ambiente: Ambiente=None, lugaresDeDesarrollo:LugaresDesarrollo=None, clases: Clases=None, casaDeProduccion: CasaProduccion=None):
			self.nombre =nombre
			self.genero = genero
			self.personajes = personajes
			self.fecha = fecha
			self.ambiente = ambiente
			self.lugaresDeDesarrollo = lugaresDeDesarrollo
			self.clases = clases
			self.casaDeProduccion = casaDeProduccion

lista_habilidades = []
lista_personajes = []
lista_debilidades = []

habilidad = Habilidades("deportes")
habilidad2 = Habilidades("logica")
habilidad3 = Habilidades("videojuegos")

debilidad = Debilidades("idiomas")
debilidad2 = Debilidades("fragil")
debilidad3 = Debilidades("Ortografia")

lista_habilidades.append(habilidad)
lista_habilidades.append(habilidad2)
lista_habilidades.append(habilidad3)

lista_debilidades.append(debilidad)
lista_debilidades.append(debilidad2)
lista_debilidades.append(debilidad3)

print (lista_habilidades)


oliver = Personajes('Oliver','Aton','Masculino',19,'ladino',lista_habilidades,lista_debilidades)
lista_personajes.append(oliver)

lista_debilidades2 = [Debilidades("Humildad"),Debilidades("Deportes")]
lista_habilidades2 = [Habilidades("programar"),Habilidades('videojuegos'),Habilidades('musica')]


miguel = Personajes('Miguel','Arrivillaga','Masculino',20,'ladino',lista_habilidades2,lista_debilidades2)
lista_personajes.append(miguel)
#recorrer listado de personajes
for x in lista_personajes:
    print("///////////////////////////////////")
    print("NOMBRE: ",x.nombre)
    print("APELLIDO: ",x.apellido)
    print("GENERO: ",x.sexo)
    print("EDAD: ",x.edad)
    print("RAZA: ",x.raza)
    if x.nombre == 'Oliver': # FORMA 1 para recorrer un ARRAY dentro de OTRO ARRAY
        h = []
        d = []
        for i in lista_habilidades:
            h.append(i.habilidad)
        for i in lista_debilidades:
            d.append(i.debilidad)
        print("Habilidades de Oliver:",h)
        print("Debilidades de Oliver: ",d)
        h.clear()
        d.clear()
    elif x.nombre == 'Miguel': # FORMA 2 para recorrer un ARRAY dentro de OTRO ARRAY
        for i in lista_habilidades2:
            print("Habilidades de Miguel:",i.habilidad)
        for i in lista_debilidades2:
            print("Debilidades de Miguel: ",i.debilidad)


