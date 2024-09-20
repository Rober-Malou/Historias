import random, time,sys

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

       
sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 9, 5, True)


global gudetama
gudetama = True

def llegada_de_la_ayuda(gudetama):
    print('Sandra y Valeria se sientan nerviosamente a esperar.')
    if gudetama == False:
        print('Sakipillo les trae una selección de bebidas (zumos, coca-cola, fanta, café, etc) y les sirve algo ellas mientras esperan a que lleguen los refuerzos.')
    elif gudetama == True:
        print('Sakipillo y Gudetama les traen una selección de bebidas (zumos, coca-cola, fanta, café, etc) y les sirven algo mientras ellas esperan a que lleguen los refuerzos.')
    else:
        print('No tengo ni idea de que ha pasado aquí, la idea es que si elegiste comerte a Gudetama solo Sakipillo les llevaría unas bebidas, si no los 2, pero algo salio mal.')
    print('culo')

def golpe_de_suerte(self):
    milagro = random.randint(-7, 0)
    ventaja = milagro + self.suerte
    return(ventaja)
def ataque_aéreo():
    golpe_de_suerte(sandra)
    if golpe_de_suerte(sandra) >= 0:
        print('Mientras unos pájaros las sobrevuelan, uno de ello que había comido unas semillas en mal estado toma la decision de "bombardearlas". En silencio, Sandra le da las gracias a su tallarinesca magnificencia por acordarse de llevar algo de agua y unos pañuelos de papel. Se limpia y sigues con su paseo.')
    else:
        print('Sandra y Valeria ven como uno de los pájaros aligera su carga justo donde están ellas, pero gracias a sus reflejos felinos lo esquivan en el ultimo momento y siguen tan tranquila con tu paseo.')

def caca():
    print('culo')
    ataque_aéreo()
    print('pis')

caca()