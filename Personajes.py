import random

# Plantilla personajes

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
            ventaja == 0

# Distintos personajes

sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 9, 5, True)



# Obertura
print('Bienvenida, últimamente tu trabajo a sido muy duro, y el resto de tu vida también. No puedo hacer mucho, pero tampoco quiero no hacer nada. Espero que te guste y que perdones la infinidad de faltas de ortografía.')

#Explicación del juego
print('Para avanzar en el juego tendrás que escribir exactamente las palabras que aparezcan entre comillas ("Aquí") en la opción que quieras escoger y pulsar "Enter"')

#Inicio de la aventura
def inicio():
    choice1 = 0
    print('Es una magnifica mañana de sábado en el reino. La reina Sandra se levanta en su castillo de la sierra y se asoma a su balcón a contemplar su reino. No es un reino demasiado grande, pero es de ella.\n Casi todo es bosque mágico, y salvo algún ocasional viajero o invitado no hay nadie en kilómetros a la redonda. Ahora que tu estas despierta.')
#Primera decision del juego
    def decision1(choice1):
        if choice1 == 0:
            decision = str(input('¿Quieres ir a "despertar" a la princesa, "desayunar" o "salir" a dar el paseo? \n'))
            if decision == 'despertar':
                el_despertar_de_valeria()
            elif decision == 'desayunar':
                el_desayuno()
            elif decision == 'salir':
                entrada_al_bosque()
            else:
                print('Por el amor del dios tallarín, esa no es una de las opciones')
                decision1(choice1)
        elif choice1 == 1:
            decision = str(input('¿Quieres ir a "desayunar" o "salir" a dar el paseo? \n'))
            if decision == 'desayunar':
                el_desayuno()
            elif decision == 'salir':
                entrada_al_bosque()
            else:
                print('Por el amor del dios tallarín, esa no es una de las opciones')
                decision1(choice1)
        elif choice1 == 2:
            decision = str(input('¿Quieres ir a "despertar" a la princesa o "salir" a dar el paseo?'))
            if decision == 'despertar':
                el_despertar_de_valeria()
            elif decision == 'salir':
                entrada_al_bosque()
            else:
                print('Por el amor del dios tallarín, esa no es una de las opciones')
                decision1(choice1)
        elif choice1 == 3:
            print('Ahora todo lo que queda es salir a dar un paseo.')
            entrada_al_bosque()
        else:
            print('Algo ha salido mal, el dios tallarín no me ha sonreído')
            inicio()

    def el_despertar_de_valeria():
        nonlocal choice1
        choice1 += 1
        print('Te diriges hacia la habitación de la princesa, una vez dentro te paras un instante a contemplar la escena. Valeria esta dulcemente dormida completamente tranquila. Su habitación esta decorada con unicornios y cosas monas.\n ')
        decision =str(input('¿Quieres, despertarla "dulcemente", "rápidamente" o dejarla "dormir"?'))
        if decision == 'dulcemente':
            print('Te acercas dulcemente hacia la cama y le acaricias con ternura la mejilla, unos segundos después ella abre los ojos y te da los buenos días mientras se rasca los ojitos')
            decision1(choice1)
        else:
            print('culo')
            decision1(choice1)
        
    def el_desayuno():
        print('caca')

    def entrada_al_bosque():
        print('pedo')

    decision1(choice1)
inicio()