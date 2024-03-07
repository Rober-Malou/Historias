import random

class Personaje:
    def __init__(self, nombre, sexo, especie, fuerza, inteligencia, carisma, suerte):
        self.nombre = nombre
        self.sexo = sexo
        self.especie = especie
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.suerte = suerte

    def golpe_de_suerte(self):
        milagro = random.randint(-10, 0)
        ventaja = milagro + self.suerte
        if ventaja >= 1:
            return(ventaja)
            
        else:
            ventaja == 0

sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 9, 5)

camello = sandra

print(vars(camello))
