# realizar clase llamada Vaca, puede proveer queso(hereda de leche), leche(hereda de vaca) y derivados, a su vez debe tener propiedades
from datetime import datetime 
class vaca():
    def __init__(self, raza:str, pelaje:str, cuernos: bool, noSerie:str,\
        alimentacion:str, pedigree:str, peso:float, ):
        self.raza = raza
        self.pelaje = pelaje
        self.cuernos = cuernos
        self.noSerie = noSerie
        self.peso = peso
        self.alimentacion = alimentacion
        self.pedigree = pedigree
        
class Lacteos(vaca):
    def __init__(self, tipoLacteo:str, temperatura:str, textura:str, estado:str , \
                 procesado: bool, envase: str, fechaVencimiento:datetime, marca:str, precio:float):
        self.tipoLacteo = tipoLacteo
        self.temperatura = temperatura
        self.textura = textura
        self.procesado = procesado
        self.envase=envase
        self.fechaVencimiento=fechaVencimiento
        self.marca=marca
        self.precio=precio
    def get_productos(self):
        if(self.pedigree=="productor"):
            if(self.raza == "argentina"):
                return True
                
    
shorthorn = vaca('Britanica','blanco',True,'025994-j','trigo','productor',740)
pardo = vaca('Suiza','negro',False,'568971-v','pasto','reproduccion',800)
criolla = vaca('argentina','colorado',True,'9987564-l','maiz','productor',440)

flan = Lacteos('flan','ambiente','gelatinosa','solido',True,'plastico',datetime.now(),'Colun',15.00)
helado = Lacteos('helado','fria','cremosa','solido',True,'plastico',datetime.now(),'Sarita',10.00)
lecheEntera = Lacteos('leche','fria','cremosa','liquida',False,'vidrio',datetime.now(),'artesanal',5.00)

        
