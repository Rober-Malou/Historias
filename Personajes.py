import random

# Plantilla personajes

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

# Distintos personajes

sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 9, 5)

# Obertura
print('Bienvenida, últimamente tu trabajo a sido muy duro, y el resto de tu vida también. No puedo hacer mucho, pero tampoco quiero no hacer nada. Espero que te guste y que perdones la infinidad de faltas de ortografía.')

#Explicación del juego
print('Para avanzar en el juego tendrás que escribir exactamente las palabras que aparezcan entre comillas ("Aquí") en la opción que quieras escoger y pulsar "Enter"')

#Inicio de la aventura
def inicio():
    print('Es una magnifica mañana de sábado en el reino. La reina Sandra se levanta en su castillo de la sierra y se asoma a su balcón a contemplar sus tierras, nada salvo bosque en el horizonte. Esta mañana ha decidido ir a dar un paseo por su magnifico bosque.')
    decision = str(input('Quieres ir a "despertar" a la princesa, "desayunar", o "salir" a dar el paseo \n'))
    if decision == "despertar":
        el_despertar_de_valeria()
    elif decision == "desayunar":
        el_desayuno()
    elif decision == "salir":
        entrada_al_bosque()
    else:
        print('Por el amor del dios tallarín, esa no es una de las opciones')
        decision()

def el_despertar_de_valeria():
    print('culo')
    el_desayuno()

def el_desayuno():
    print('caca')

def entrada_al_bosque():
    print('pedo')

inicio()