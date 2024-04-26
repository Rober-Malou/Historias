# Librerías importadas

import random, emoji, time

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

# Función de Suerte

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
    print('Es una magnifica mañana de sábado en el reino. La reina, Sandra se despierta en su castillo de la sierra y se asoma a su balcón a contemplar su reino. No es un reino demasiado grande, pero es de ella.\n Casi todo es bosque mágico, y salvo algún ocasional viajero o invitado no hay nadie en kilómetros a la redonda. ')
    decision1(choice1)

#Primera decision del juego

def decision1(choice1):
    if choice1 == 0:
        decision = str(input('¿Quieres que sandra  "despierte" a la princesa, "desayune" o "salga" a dar el paseo? \n'))
        if decision == 'despierte':
            el_despertar_de_valeria()
        elif decision == 'desayune':
            el_desayuno()
        elif decision == 'salga':
            entrada_al_bosque()
        else:
            print(fallo)
            decision1(choice1)
    elif choice1 == 1:
        decision = str(input('¿Quieres que Sandra y Valeria "desayunen" o "salgan" a dar un paseo? \n'))
        if decision == 'desayunen':
            el_desayuno()
        elif decision == 'salgan':
            paseo_con_valeria()
        else:
            print(fallo)
            decision1(choice1)
    elif choice1 == 2:
        decision = str(input('¿Quieres que Sandra "despierte" a la princesa o "salga" a dar el paseo?\n'))
        if decision == 'despierte':
            el_despertar_de_valeria()
        elif decision == 'salga':
            entrada_al_bosque()
        else:
            print(fallo)
            decision1(choice1)
    elif choice1 == 3:
        print('Ahora todo lo que queda es que salgan a dar un paseo.')
        paseo_con_valeria()
    else:
        print('Algo ha salido mal, el dios tallarín no me ha sonreído, en el gremio a esto lo llamamos bug.')
        inicio()

# Escena del despertar

def el_despertar_de_valeria():
    global choice1
    choice1 += 1
    print('Sandra se dirige hacia la habitación de la princesa, una vez dentro se para un instante a contemplar la escena. La princesa Valeria esta dulcemente dormida completamente tranquila. Su habitación esta decorada con unicornios y cosas monas.\n ')
    decision2()

# Decision sobre como despertar a Valeria

def decision2():
    global choice1
    decision = str(input('¿Quieres que la reina la despierte "dulcemente", "rápidamente" o que la deje "dormir"?\n'))
    if decision == 'dulcemente':
        print('Te acercas dulcemente hacia la cama y le acaricias con ternura la mejilla.')
        golpe_de_suerte(sandra)
        if golpe_de_suerte(sandra) >= 1:
            print('Unos segundos después Valeria abre los ojos y le da los buenos días a Sandra. Se incorpora, le besa en la mejilla y dice: \n -¿Que vamos a hacer hoy?')
            valeria.activo = True
            decision1(choice1)
        else:
            print('Valeria sigue durmiendo profundamente.')
            decision2()
    elif decision == 'rápidamente':
        print('La reina le agita el brazo a la princesa.')
        golpe_de_suerte(sandra)
        if golpe_de_suerte(sandra) >= 1:
            print('Valeria se levanta sobresaltada mirando al rededor. Cuando por fin se ubica un poco le dice con voz de estar medio dormida a su madre. \n -¿Que vamos a hacer hoy mami?')
            valeria.activo = True
            decision1(choice1)

        else:
            print('Valeria sigue durmiendo profundamente.')
            decision2()
    elif decision == 'dormir':
        choice1 -= 1
        print('La reina no se siente capaz de perturbarla con lo mona que esta.')
        decision1(choice1)
    else:
        print(fallo)
        decision2()

# Escena del Desayuno

def el_desayuno():
    global choice1
    choice1 += 2
    if valeria.activo == True:
        print('Sandra y Valeria bajan a la cocina del castillo, allí encuentran un pollo con una sola ceja y un huevo crudo (solo la yema y la clara), ambos con gorros de cocinero y el pollo lleva la cascara de su huevo como pantalón. \n')
        decision3()
    else:
        print('Sandra baja a la cocina del castillo, allí encuentra un pollo con una sola ceja y un huevo crudo (solo la yema y la clara), ambos con gorros de cocinero y el pollo lleva la cascara de su huevo como pantalón. \n')
        decision4()

# Que Desayunar con Valeria

def decision3 ():
    decision = str(input('Shakipillo:\n - ¿Que queréis desayunar hoy mamis? Podemos prepararos "cereales", "bollos", o "huevos" con bacon\n'))
    if decision == 'cereales':
        print('Gudetama:\n - Que pereza.')
        print('Se ponen a preparar el desayuno a toda velocidad, en menos de 30 segundos todo esta listo y lo sirven en el patio. \n Sus majestades desayunan tranquilamente, con el sol dándoles en la cara. Durante el desayuno charlan animadamente y deciden ir a dar un paseo por el bosque.')
        sandra.fuerza = 7
        valeria.fuerza = 4
        paseo_con_valeria()
    elif decision == 'bollos':
        print('Gudetama:\n - Que pereza.')
        print('Gudetama pone a precalentar el horno mientras Sakipillo abre el congelador y saca varias pastas congeladas. Las coloca en una bandeja y las mete en el horno, mientras las pastas se hacen le sirven zumo en el patio a sus "mamis". Mientras Sandra y Valeria esperan tranquilamente contemplando la naturaleza.')
        print('A los pocos minutos Shakipillo y Gudetama vuelven con mini cruasanes, mantequilla y mermelada y varias mini napolitanas de chocolate. \n Tras desayunar, sus majestades deciden ir a dar un paseo en el Bosque.')
        sandra.fuerza += 1
        valeria.fuerza += 1
        sandra.carisma += 1
        valeria.carisma += 1
        paseo_con_valeria()
    elif decision == 'huevos':
        print('Gudetama:\n - Mal royo.')
        print('Sakipillo:\n - Pero Gudetama por fin las mamis van a permitirte cumplir tu destino como tu querías.')
        print('A Gudetama se le ilumina la cara, por fin podrá cumplir su destino. Se despide de los tres, se bebe un cuenquito de salsa de soja y se va a la sartén. Mientras Sakipillo termina de hacer el desayuno, sus majestades salen al patio a que les de el sol. A los pocos minutos Sakipillo trae zumo, huevos con bacon y un par de napolitanas de chocolate.\n Desayunan tranquilamente admirando la naturaleza y al terminar deciden irse a dar un paseo por el bosque.')
        sandra.fuerza += 1
        sandra.carisma += 1
        sandra.suerte += 1
        valeria.fuerza += 1
        valeria.carisma += 1
        valeria.suerte += 1
        print(emoji.emojize(':confetti_ball::confetti_ball:Sandra y Valeria reciben la bendición de destino cumplido. El dios tallarín les otorga mas suerte en futuras aventuras:confetti_ball::confetti_ball:'))
        paseo_con_valeria()
    else:
        print(fallo)
        decision3()        

# Que Desayunar Sola

def decision4():
    decision = str(input('Shakipillo:\n - ¿Que quieres desayunar hoy mami? Tenemos "cereales", "bollos", o "huevos" con bacon?\n'))
    if decision == 'cereales':
        print('Gudetama:\n - Que pereza.')
        print('Se ponen a preparar el desayuno a toda velocidad, en menos de 30 segundos todo esta listo y se lo sirven en el patio. \n Desayuna tranquilamente, con el sol dándole en la cara.')
        print('Sakipillo:\n - Le he preparado un tentempié a mi otra mami en caso de que quieran ir a dar un paseo juntas.')
        sandra.fuerza += 1
        valeria.fuerza += 1
        decision1(choice1)
    elif decision == 'bollos':
        print('Gudetama:\n - Que pereza.')
        print('Gudetama pone a precalentar el horno mientras Sakipillo abre el congelador y saca varias pastas congeladas. Las coloca en una bandeja y las mete en el horno, mientras las pastas se hacen le sirven zumo en el patio a la reina que espera pacientemente contemplando la naturaleza.')
        print('A los pocos minutos vienen con mini cruasanes, mantequilla, mermelada y varias mini napolitanas de chocolate.')
        print('Sakipillo:\n - Le he preparado un tentempié a mi otra mami en caso de que quieran ir a dar un paseo juntas.')
        sandra.fuerza += 1
        valeria.fuerza += 1
        sandra.carisma += 1
        decision1(choice1)
    elif decision == 'huevos':
        print('Gudetama:\n - Mal royo.')
        print('Sakipillo:\n - Pero Gudetama por fin mami va a permitirte cumplir tu destino como tu querías.')
        print('A Gudetama se le ilumina la cara, por fin podrá cumplir su destino. Se despide de los dos, se bebe un cuenquito de salsa de soja y se va a la sartén. Mientras Sakipillo termina de hacer el desayuno, Sandra sale al patio a que le de el sol. A los pocos minutos Sakipillo trae zumo, huevos con bacon y un par de napolitanas de chocolate.\n La reina desayuna tranquilamente admirando la naturaleza.')
        print('Sakipillo:\n - Le he preparado un tentempié a mi otra mami en caso de que quieran ir a dar un paseo juntas.')
        sandra.fuerza += 1
        sandra.carisma += 1
        sandra.suerte += 1
        valeria.fuerza += 1
        print(emoji.emojize(':confetti_ball::confetti_ball:Sandra ha recibido la bendición de destino cumplido. El dios tallarín le otorga mas suerte en sus futuras aventuras.:confetti_ball::confetti_ball:'))
        decision1(choice1)
    else:
        print(fallo)
        decision4()

# Paseo con Valeria     

def paseo_con_valeria():
    print('Empiezan a pasear, con el sol en la cara y el castillo a la espalda. Poco a poco se van adentrando en el bosque, se encuentran ardillas escondiendo bellotas, pájaros sobrevolandolas y todo tipo de arboles y flores.')
    golpe_de_suerte(sandra)
    if golpe_de_suerte == 0:
        print('Mientras unos pájaros las sobrevuelan, uno de ello que había comido unas semillas en mal estado toma la decision de "bombardearlas". En silencio, Sandra le da las gracias a su tallarinesca magnificencia por acordarse de llevar algo de agua y unos pañuelos de papel. Se limpia y sigues con su paseo.')
    else:
        print('Sandra y Valeria ven como uno de los pájaros aligera su carga justo donde están ellas, pero gracias a sus reflejos felinos lo esquivan en el ultimo momento y siguen tan tranquila con tu paseo.')
    print('Mientras se adentran en el bosque, ahora con un ojo en el cielo, van tranquilamente charlando, disfrutando de la compañía mutua. A lo lejos, apartado del sendero ven un bulto extraño que no pueden identificar bien.')
    vais_o_seguís()

# Decision sobre si investigas el bulto o no
    
def vais_o_seguís():    
    decision = str(input('¿Quieres que se "acerquen" a ver o que "sigan" con su camino?\n'))
    if decision == 'acerquen':
        el_allazgo_del_unicornio()
    elif decision == 'sigan':
        ascenso_a_la_montaña()
    else:
        print(fallo)
        vais_o_seguís()

# Allazgo del unicornio

def el_allazgo_del_unicornio():
    print('Se acercan cuidadosamente pero el bosque es demasiado denso y no pueden hacerlo muy deprisa.')
    golpe_de_suerte(valeria)
    if golpe_de_suerte == 0:
        print('Valeria intenta pasar por encima de una rama, desafortunadamente se le engancha el pie de atrás al intentar pasarla. Al caerse se raspa la rodilla y se hace sangre. Empieza a llorar hasta que su madre va a verla. ')
        golpe_de_suerte(sandra)
        if golpe_de_suerte ==0:
            print('La reina se acerca, limpia la herida he intenta cubrirla con una tirita que lleva en el bolso. Desgraciadamente el raspón es demasiado grande y no queda totalmente cubierto.')
            valeria.fuerza -= 1
        else:
            print('La reina se acerca, limpia la herida y la tapa con una tirita. Valeria parece incomoda los 3 o 4 primeros pasos, pero en seguida se le  olvida el golpe.')
    else:
        print('Al saltar una rama, Valeria esta a punto de caerse, pero consigue mantener el equilibrio.')
    print('Al llegar al lugar donde habían visto algo extraño ven que un precioso unicornio, con el pelaje blanco y las crines color arcoíris, esta atrapado bajo un árbol caído la noche anterior.')
    el_rescate_del_unicornio()

# Rescate del unicornio

def el_rescate_del_unicornio():
    print('Valeria intenta acariciar al animal, calmarlo, decirle que todo va a salir bien. El unicornio parece entender a la princesa y aparenta estar mas relajado.')
    print('La reina da una vuelta al rededor del animal y el árbol, cuidadosamente analizando la situación. Después de unos minutos decide que solo hay tres cosas que pueden intentar:')

    estrategia_de_rescate()
def estrategia_de_rescate():
    decision = str(input('Levantar el árbol con "fuerza" bruta, levantar el árbol usando otro árbol o rama como "palanca" o intentar "llamar" mas tarde a los guardias forestales del vecino reino de España.\n'))
    if decision == 'fuerza':
        print('La reina le dice a la princesa que valla a donde esta ella y que a la de tres las dos van a empujar el árbol hacia arriba y un lado y que con un poco de suerte el unicornio podrá dar el ultimo empujón y liberarse.')
        print('Sandra:\n-A la de una.')
        time.sleep(2)
        print('-A la de dos.')
        time.sleep(2)
        print('-Y a la de !!!!TREEEEES¡¡¡¡')
        suerte_sandra = golpe_de_suerte(sandra)
        suerte_valeria = golpe_de_suerte(valeria)
        fuerza = suerte_sandra + suerte_valeria + sandra.fuerza + valeria.fuerza
        if fuerza >= 16:
            print('El árbol empieza a crujir mientras lo levantan, apenas consiguen levantarlo cinco centímetros, pero es lo necesario para que el unicornio se pueda intentar incorporar, al hacerlo, termina haciendo que el árbol ruede al suelo quedando totalmente libre.')
            print('El unicornio se mantiene erguido y orgulloso contemplando a sus rescatadoras. Amistosamente se acerca primero a la princesa y luego a la reina y gacha la cabeza como haciendo una reverencia y las acaricia suavemente con el cuerno en la frente.')
            print('Cuando el cuerno las roza, puede verse por un instante un destello de luz, casi como un arcoíris. Después se aleja trotando alegremente por el bosque rezumando felicidad y magia por todo su ser.')
            print(':confetti_ball::confetti_ball:Sandra y Valeria han recibido la bendición de la magia del unicornio. A partir de ahora la suerte les sonreirá aun mas')
            sandra.suerte += 1
            valeria.suerte += 1
            bosque_profundo()
        else:
            print('El árbol empieza a crujir mientras lo levantan pero apenas se mueve, el unicornio intenta revolverse y levantarse sin éxito. Después de unos segundos no les queda mas remedio que rendirse.')
            print('Sandra entonces intenta buscar a su alrededor por si hay algún tronco o palo con el que hacer palanca pero sin éxito no quedándoles más remedio que volver al castillo a llamar a los guardas forestales.')
            print('Se despiden del unicornio prometíendole volver con ayuda y se dirigen de vuelta al castillo donde hay cobertura.')
            llamada_a_la_policía()
    elif decision == 'palanca':
        print('Sandra se pone a buscar una rama gruesa o un árbol pequeño para poder usar como palanca mientras Valeria sigue manteniendo al unicornio tranquilo y acompañado. Unos minutos después la reina vuelve con una rama que parece lo bastante gruesa y fuerte para la tarea.')    
        print('Entre las dos encuentran un lugar que parece bueno para colocar la rama y creen que no se va a deslizar.')
        print('Sandra:\n-A la de una.')
        time.sleep(2)
        print('-A la de dos.')
        time.sleep(2)
        print('-Y a la de !!!!TREEEEES¡¡¡¡')

        inteligencia = suerte_sandra + suerte_valeria + sandra.inteligencia + valeria.inteligencia
        if inteligencia >= 16:
            print('Las dos a la vez empujan el palo hacia arriba. El palo cruje y parece que se va a romper pero consiguen levantar lo bastante para que el unicornio se revuelva y consiga salir de debajo del árbol.')
            print('El unicornio se mantiene erguido y orgulloso contemplando a sus rescatadoras. Amistosamente se acerca primero a la princesa y luego a la reina y gacha la cabeza como haciendo una reverencia y las acaricia suavemente con el cuerno en la frente.')
            print('Cuando el cuerno las roza, puede verse por un instante un destello de luz, casi como un arcoíris. Después se aleja trotando alegremente por el bosque rezumando felicidad y magia por todo su ser.')
            print(':confetti_ball::confetti_ball:Sandra y Valeria han recibido la bendición de la magia del unicornio. A partir de ahora la suerte les sonreirá aun mas')
            sandra.suerte += 1
            valeria.suerte += 1
            bosque_profundo()
        else:
            print('Empiezan a empujar el palo hacia arriba pero enseguida se resbala. Al caerse, el palo que estaban usando se parte y queda totalmente inutilizable.')
            print('Intentan buscar otro palo que les sirva pero sin suerte no quedándoles más remedio que volver al castillo a llamar a los guardas forestales.')
            print('Se despiden del unicornio prometíendole volver con ayuda y se dirigen de vuelta al castillo donde hay cobertura.')
            llamada_a_la_policía()
    elif decision == 'llamada':
        print('La reina y la princesa después de considerar sus opciones llegan a la conclusión de que su mejor opción es llamar a la guardia forestal del reino de España. Se despiden del unicornio augurándole que volverán a ayudarlo y comienzan a caminar dirección al castillo, donde hay cobertura.')
        llamada_a_la_policía()
    else:
        print(fallo)
        estrategia_de_rescate()

def llamada_a_la_policía():
    print('Llegando al castillo el teléfono de Sandra recupera la suficiente cobertura como para poder hacer una llamada. Dado que es una reina, Sandra no llama a la guardia forestal directamente, eso es poca cosa para ella, ella llama al ministerio de exteriores español, al despacho del ministro nada menos.')
def bosque_profundo():
    print('teta')       
def ascenso_a_la_montaña():
    print('culo')

def entrada_al_bosque():
    print('pedo')

inicio()