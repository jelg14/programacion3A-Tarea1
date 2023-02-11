import random 
class Mision():
    def bandera(self):
        return "Obtener bandera"
    def seek_and_destroy(self):
        return "seek and destroy"
    def duelo_por_equipos(self):
        return "duelo por equipos"
    def carrera_contra_tiempo(self):
        return "carrera contra tiempo"

class Habilidades():
    habilidades=["disparo","nadar","beber","volar","correr"]
    def get_habilidad(self):
        return "respirar"
    
class personajes():
    personajes = ["pobreza","ignorancia","Joker","ultron","el pinguino",\
                  "longe moco","Doflamingo", "Darkside","Horus","Darth Vader",
                  "Sauron","Darth Sidious", "Dr. Doom"]

class superHeroe(Mision,Habilidades):
    def __init__(self,nombre, alias, poderes):
        self.nombre = nombre
        self.alias = alias
        self.poderes = poderes
    def get_enemigo(self):
        p= personajes()
        return random.choices(p.personajes,k=3) # imprime varios datos aleatorios, dependiendo de la cantidad k que se solicite
    def get_amigos(self):
        self.carrera_contra_tiempo()
        p= personajes()
        return random.choice(p.personajes)#imprime un dato de forma aleatoria
    def carrera_contra_tiempo(self, isHero=True):
        return "carrera contra tiempo, super heroe: "+self.alias
    def get_habilidades(self):
        return set(random.choices(self.habilidades,k=random.randint(1,4)))

batman = superHeroe('Bruce Wayne','Batman',["millonario","Artes marciales"])
print(batman.get_enemigo())
print(batman.get_amigos())
print(batman.carrera_contra_tiempo())# utiliza metodo propio
print(batman.seek_and_destroy())
print(batman.get_habilidades())
print(batman.get_habilidad())
print()
mision = Mision()
print(mision.carrera_contra_tiempo())#utiliza metodo heredado