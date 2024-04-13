import random, emoji

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

# Funcion de Suerte

def golpe_de_suerte(self):
    milagro = random.randint(-7, 0)
    ventaja = milagro + self.suerte
    if ventaja >= 1:
        return(ventaja)
          
    else:
        return(ventaja == 0)

# Distintos personajes

sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 7, 5, True)
valeria = Personaje('Valeria', 'Mujer', 'Humana', 3, 6, 9, 6, False)

# Mensajes de Error

fallo = 'Por el amor del dios tallarín, esa no es una de las opciones'

# Variables de contador

global choice1
choice1 = 0

# Obertura

print('Vienvenid@ espero que disfrutes esta corta historia interactiva y que su Tallarisca magnificencia te guie por el buen camino.')

# Explicación del juego

print('Para avanzar en el juego tendrás que escribir exactamente las palabras que aparezcan entre comillas ("Aquí") en la opción que quieras escoger (cuidado con acentos y esas cosas, soy un programador incompetente) y pulsar "Enter"')

# Inicio de la aventura

def inicio():
    print('Es una magnifica mañana de sábado en el reino. La reina Sandra se levanta en su castillo de la sierra y se asoma a su balcón a contemplar su reino. No es un reino demasiado grande, pero es de ella.\n Casi todo es bosque mágico, y salvo algún ocasional viajero o invitado no hay nadie en kilómetros a la redonda. Ahora que tu estas despierta.')
    decision1(choice1)

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
            print(fallo)
            decision1(choice1)
    elif choice1 == 1:
        decision = str(input('¿Quieres ir a "desayunar" o "salir" a dar el paseo? \n'))
        if decision == 'desayunar':
            el_desayuno()
        elif decision == 'salir':
            paseo_con_valeria()
        else:
            print(fallo)
            decision1(choice1)
    elif choice1 == 2:
        decision = str(input('¿Quieres ir a "despertar" a la princesa o "salir" a dar el paseo?\n'))
        if decision == 'despertar':
            el_despertar_de_valeria()
        elif decision == 'salir':
            entrada_al_bosque()
        else:
            print(fallo)
            decision1(choice1)
    elif choice1 == 3:
        print('Ahora todo lo que queda es salir a dar un paseo.')
        paseo_con_valeria()
    else:
        print('Algo ha salido mal, el dios tallarín no me ha sonreído, en el gremio a esto lo llamamos bug.')
        inicio()

# Escena del despertar

def el_despertar_de_valeria():
    global choice1
    choice1 += 1
    print('Te diriges hacia la habitación de la princesa, una vez dentro te paras un instante a contemplar la escena. Valeria esta dulcemente dormida completamente tranquila. Su habitación esta decorada con unicornios y cosas monas.\n ')
    decision2()

# Decision sobre como despertar a Valeria

def decision2():
    global choice1
    decision = str(input('¿Quieres, despertarla "dulcemente", "rápidamente" o dejarla "dormir"?\n'))
    if decision == 'dulcemente':
        print('Te acercas dulcemente hacia la cama y le acaricias con ternura la mejilla.')
        golpe_de_suerte(sandra)
        if golpe_de_suerte(sandra) >= 1:
            print('Unos segundos después ella abre los ojos y te da los buenos días. Se incorpora y te besa en la mejilla y dice. \n -¿Que vamos a hacer hoy?')
            valeria.activo = True
            decision1(choice1)
        else:
            print('Parece estar demasiado dormida para que solo eso funcione.')
            decision2()
    elif decision == 'rápidamente':
        print('Te acercas a la cama y le agitas el brazo con energía')
        golpe_de_suerte(sandra)
        if golpe_de_suerte(sandra) >= 1:
            print('Valeria se levanta sobresaltada mirando al rededor. Cuando por fin se ubica un poco te dice con voz de estar medio dormida. \n -¿Que vamos a hacer hoy?')
            valeria.activo = True
            decision1(choice1)

        else:
            print('Parece estar demasiado dormida para que solo eso funcione.')
            decision2()
    elif decision == 'dormir':
        choice1 -= 1
        print('No te sientes capaz de perturbarla con lo mona que esta.')
        decision1(choice1)
    else:
        print(fallo)
        decision2()

# Escena del Desayuno

def el_desayuno():
    global choice1
    choice1 += 2
    if valeria.activo == True:
        print('Bajáis a la cocina del castillo, allí encontráis un pollo con una sola ceja y un huevo crudo(solo la yema y la clara), ambos con gorros de cocinero y el pollo lleva la cascara como pantalones. \n')
        decision3()
    else:
        print('Bajas a la cocina del castillo, allí encuentras un pollo con una sola ceja y un huevo crudo(solo la yema y la clara), ambos con gorros de cocinero y el pollo lleva la cascara como pantalones. \n')
        decision4()

# Que Desayunar con Valeria

def decision3 ():
    decision = str(input('Shakipillo - ¿Que queréis desayunar hoy mamis? ¿Queréis "cereales", "bollos", o "huevos" con bacon?\n'))
    if decision == 'cereales':
        print('Gudetama - Que pereza.')
        print('Se ponen a preparar el desayuno a toda velocidad, en menos de 30 segundos todo esta listo y os lo sirven en el patio. \n Desayunáis tranquilamente, con el sol dándoos en la cara. Al terminar os disponéis a dar un tranquilo paseo por el bosque.')
        sandra.fuerza = 7
        valeria.fuerza = 4
        paseo_con_valeria()
    elif decision == 'bollos':
        print('Gudetama - Que pereza.')
        print('Gudetama pone a precalentar el horno mientras Sakipillo abre el congelador y saca varias pastas de el. Las coloca en una bandeja y las mete en el horno, mientras las pastas se hacen os sirven zumo en el patio y esperáis contemplando la naturaleza.')
        print('A los pocos minutos vienen con mini cruasanes, mantequilla y mermelada y varias mini napolitanas de chocolate. \n Al terminar el agradable desayuno os preparais para dar un paseo por el bosque.')
        sandra.fuerza = 7
        valeria.fuerza = 4
        sandra.carisma = 8
        valeria.carisma = 10
        paseo_con_valeria()
    elif decision == 'huevos':
        print('Gudetama - Mal royo.')
        print('Sakipillo - Pero Gudetama por fin mis mamis van a permitirte cumplir tu destino como tu querías.')
        print('A Gudetama se le ilumina la cara, por fin podrá cumplir su destino. Se despide de los tres, se bebe un quenquito de salsa de soja y se va a la sartén. Mientras Sakipillo termina de hacer el desayuno, vosotras salís al patio a que os de el sol. A los pocos minutos Sakipillo trae zumo, huevos con bacon y un par de napolitanas de chocolate.\n Desayunáis tranquilamente admirando la naturaleza y al terminar decidís iros a dar un paseo por el bosque')
        sandra.fuerza = 7
        sandra.carisma = 8
        sandra.suerte = 6
        valeria.fuerza = 4
        valeria.carisma = 10
        valeria.suerte = 7
        print(emoji.emojize(':confetti_ball::confetti_ball:Habéis recibido la bendición de destino cumplido(El dios tallarín os otorga mas suerte en vuestras futuras aventuras):confetti_ball::confetti_ball:'))
        paseo_con_valeria()
    else:
        print(fallo)
        decision3()        

# Que Desayunar Sola

def decision4():
    decision = str(input('Shakipillo - ¿Que quieres desayunar hoy mami? ¿Quieres "cereales", "bollos", o "huevos" con bacon?\n'))
    if decision == 'cereales':
        print('Gudetama - Que pereza.')
        print('Se ponen a preparar el desayuno a toda velocidad, en menos de 30 segundos todo esta listo y te lo sirven en el patio. \n Desayunas tranquilamente, con el sol dándote en la cara.')
        print('Sakipillo - Le he preparado un tentempié a mi otra mami en caso de que quieran ir a dar un paseo juntas.')
        sandra.fuerza = 7
        valeria.fuerza = 4
        decision1(choice1)
    elif decision == 'bollos':
        print('Gudetama - Que pereza.')
        print('Gudetama pone a precalentar el horno mientras Sakipillo abre el congelador y saca varias pastas del mismo. Las coloca en una bandeja y las mete en el horno, mientras las pastas se hacen te sirven zumo en el patio y esperas contemplando la naturaleza.')
        print('A los pocos minutos vienen con mini cruasanes, mantequilla y mermelada y varias mini napolitanas de chocolate.')
        print('Sakipillo - Le he preparado un tentempié a mi otra mami en caso de que quieran ir a dar un paseo juntas.')
        sandra.fuerza = 7
        valeria.fuerza = 4
        sandra.carisma = 8
        decision1(choice1)
    elif decision == 'huevos':
        print('Gudetama - Mal royo.')
        print('Sakipillo - Pero Gudetama por fin mami va a permitirte cumplir tu destino como tu querías.')
        print('A Gudetama se le ilumina la cara, por fin podrá cumplir su destino. Se despide de los tres, se bebe un cuenquito de salsa de soja y se va a la sartén. Mientras Sakipillo termina de hacer el desayuno, sales al patio a que te de el sol. A los pocos minutos Sakipillo trae zumo, huevos con bacon y un par de napolitanas de chocolate.\n Desayunas tranquilamente admirando la naturaleza.')
        print('Sakipillo - Le he preparado un tentempié a mi otra mami en caso de que quieran ir a dar un paseo juntas.')
        sandra.fuerza = 7
        sandra.carisma = 8
        sandra.suerte = 6
        valeria.fuerza = 4
        print(emoji.emojize(':confetti_ball::confetti_ball:Has recibido la bendición de destino cumplido(El dios tallarín te otorga mas suerte en vuestras futuras aventuras):confetti_ball::confetti_ball:'))
        decision1(choice1)
    else:
        print(fallo)
        decision4()

# Paseo con Valeria     

def paseo_con_valeria():
    print('Empezáis a pasear, con el sol en la cara y el castillo a la espalda. Poco a poco os vais adentrando en el bosque, os encontráis ardillas escondiendo bellotas, pájaros sobrevolandoos.')
    golpe_de_suerte(sandra)
    if golpe_de_suerte == 0:
        print('Mientras te sobrevuela, un pájaro te bombardea. En silencio le das las das las gracias a su tallarinesca magnificencia porque te acordaste de llevar algo de agua y unos pañuelos de papel. Te limpias y sigues con tu paseo.')
    else:
        print('Ves como uno de los pájaros aligera la carga justo donde tu estas, pero con unos reflejos felinos lo esquivas en el ultimo momento y sigues tan tranquila con tu paseo.')
    print('Mientras os adentráis en el bosque, ahora con un ojo en el cielo, vais tranquilamente charlando, disfrutando de la compañía de la otra. A lo lejos, un poco alejado del sendero veis un bulto extraño que no podéis identificar bien.')
    vais_o_seguís()

# Decision sobre si investigas el bulto o no
    
def vais_o_seguís():    
    decision = str(input('Quieres, "acercarte" a ver o "seguir" con vuestro camino.\n'))
    if decision == 'acercarte':
        el_rescate_del_unicornio()
    elif decision == 'seguir':
        ascenso_a_la_montaña()
    else:
        print(fallo)
        vais_o_seguís()

# Rescate del unicornio

def el_rescate_del_unicornio():
    print('Os vais acercando cuidadosamente pero el bosque es demasiado denso y no podéis hacerlo muy deprisa.')
    golpe_de_suerte(valeria)
    if golpe_de_suerte == 0:
        print('Valeria intenta pasar por encima de una rama, desafortunadamente se le engancha el segundo pie al intentar pasarlo por encima de la rama. Al caerse se raspa la rodilla y se hace sangre en la rodilla. ')

     
def ascenso_a_la_montaña():
    print('culo')

def entrada_al_bosque():
    print('pedo')

inicio()