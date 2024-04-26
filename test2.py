import random, time

class Personaje:
    def __init__(self, nombre, sexo, especie, fuerza, inteligencia, carisma, suerte, activo):
        self.nombre = nombre
        self.sexo = sexo
        self.especie = especie
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.suerte = suerte
        self.activo = activo
def golpe_de_suerte(self):
    milagro = random.randint(-10, 0)
    ventaja = milagro + self.suerte
    if ventaja >= 1:
        return(ventaja)
          
    else:
        return(0)
       
sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 9, 5, True)
suerte_sandra = golpe_de_suerte(sandra)

global gudetama
gudetama = 1

def llegada_de_la_ayuda(gudetama):
    print('Sandra y Valeria se sientan nerviosamente a esperar.')
    if gudetama == 0:
        print('Sakipillo les trae una selección de bebidas (zumos, coca-cola, fanta, café, etc) y les sirve algo ellas mientras esperan a que lleguen los refuerzos.')
    elif gudetama == 1:
        print('Sakipillo y Gudetama les traen una selección de bebidas (zumos, coca-cola, fanta, café, etc) y les sirven algo mientras ellas esperan a que lleguen los refuerzos.')
    else:
        print('No tengo ni idea de que ha pasado aquí, la idea es que si elegiste comerte a Gudetama solo Sakipillo les llevaría unas bebidas, si no los 2, pero algo salio mal.')
    print('culo')

llegada_de_la_ayuda(gudetama)

gudetama -= 1

llegada_de_la_ayuda(gudetama)

