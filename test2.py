import random

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

def decision2():
    decision =str(input('¿Quieres, despertarla "dulcemente", "rápidamente" o dejarla "dormir"?\n'))
    if decision == 'dulcemente':
        print('Te acercas dulcemente hacia la cama y le acaricias con ternura la mejilla.')
        golpe_de_suerte(sandra)
        if golpe_de_suerte(sandra) >= 1:
            print('Unos segundos después ella abre los ojos y te da los buenos días. Se incorpora y te besa en la mejilla y dice. \n -¿Que vamos a hacer hoy?')
            decision1(choice1)
        else:
            print('Parece estar demasiado dormida para que solo eso funcione.')
            decision2()
    elif decision == 'rápidamente':
        print('Te acercas a la cama y le agitas el brazo con moderada energía')
        golpe_de_suerte(sandra)
        if golpe_de_suerte(sandra) >= 1:
            print('Valeria se levanta sobresaltada mirando al rededor. Cuando por fin se ubica un poco te dice con voz de estar medio dormida. \n -¿Que vamos a hacer hoy?')
            decision1(choice1)
        else:
            print('Parece estar demasiado dormida para que solo eso funcione.')
            decision2()
    elif decision == 'dormir':
        print('No te sientes capaz de perturbarla con lo mona que esta.')
        decision1(choice1)
    else:
        print('Por el amor del dios tallarín, esa no es una de las opciones')

decision2()
decision2()
decision2()
decision2()
decision2()
decision2()
decision2()
decision2()
decision2()
decision2()
decision2()
