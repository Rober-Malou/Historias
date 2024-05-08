# Librerías importadas

import random, emoji, time, sys

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
    return(ventaja)

def ataque_aéreo():
    golpe_de_suerte(sandra)
    if golpe_de_suerte(sandra) >= 1:
        print('Mientras unos pájaros las sobrevuelan, uno de ello que había comido unas semillas en mal estado toma la decision de "bombardearlas". En silencio, Sandra le da las gracias a su tallarinesca magnificencia por acordarse de llevar algo de agua y unos pañuelos de papel. Se limpia y sigues con su paseo.')
    else:
        print('Sandra y Valeria ven como uno de los pájaros aligera su carga justo donde están ellas, pero gracias a sus reflejos felinos lo esquivan en el ultimo momento y siguen tan tranquila con tu paseo.')

# Distintos personajes

sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 7, 5, True)
valeria = Personaje('Valeria', 'Mujer', 'Humana', 3, 6, 9, 6, False)

# Mensajes de Error

fallo = 'Por el amor del dios tallarín, esa no es una de las opciones'
nota_de_autor= 'Nota del autor: Se ve que la he liado parda aquí'

# Frases finales obtenidas por logros

unicornio = 'Sandra y Valeria se dan cuenta de lo tarde que es, y se preparan para cenar e irse a la cama con la alegría de haber sido capaces de ayudar a una criatura tan magnifica. Desde ese dia y como agradecimiento, todos los días al despertar, verían como un cálido arcoíris entraba por su ventana'

# Variables de contador

global unicornio_salvado
unicornio_salvado = False

global choice1
choice1 = 0

global gudetama
gudetama = True

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
        print(nota_de_autor)
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
        despertar = golpe_de_suerte(sandra)
        if despertar >= 1:
            print('Unos segundos después Valeria abre los ojos y le da los buenos días a Sandra. Se incorpora, le besa en la mejilla y dice: \n -¿Que vamos a hacer hoy?')
            valeria.activo = True
            decision1(choice1)
        else:
            print('Valeria sigue durmiendo profundamente.')
            decision2()
    elif decision == 'rápidamente':
        print('La reina le agita el brazo a la princesa.')
        golpe_de_suerte(sandra)
        despertar = golpe_de_suerte(sandra)
        if despertar >= 0:
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
        global gudetama
        gudetama = False
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
        global gudetama
        gudetama = False
        print(emoji.emojize(':confetti_ball::confetti_ball:Sandra ha recibido la bendición de destino cumplido. El dios tallarín le otorga mas suerte en sus futuras aventuras.:confetti_ball::confetti_ball:'))

        decision1(choice1)
    else:
        print(fallo)
        decision4()

# Paseo con Valeria     

def paseo_con_valeria():
    print('Empiezan a pasear, con el sol en la cara y el castillo a la espalda. Poco a poco se van adentrando en el bosque, se encuentran ardillas escondiendo bellotas, pájaros sobrevolandolas y todo tipo de arboles y flores.')
    ataque_aéreo()
    print('Mientras se adentran en el bosque, ahora con un ojo en el cielo, van tranquilamente charlando, disfrutando de la compañía mutua. A lo lejos, apartado del sendero ven un bulto extraño que no pueden identificar bien.')
    vais_o_seguís()

# Decision sobre si investigas el bulto o no
    
def vais_o_seguís():    
    decision = str(input('¿Quieres que se "acerquen" a ver o que "sigan" con su camino?\n'))
    if decision == 'acerquen':
        el_allazgo_del_unicornio()
    elif decision == 'sigan':
        ascenso_a_la_montaña(unicornio_salvado)
    else:
        print(fallo)
        vais_o_seguís()

# Allazgo del unicornio

def el_allazgo_del_unicornio():
    print('Se acercan cuidadosamente pero el bosque es demasiado denso y no pueden hacerlo muy deprisa.')
    golpe_de_suerte(valeria)
    if golpe_de_suerte(valeria) <= 0:
        print('Valeria intenta pasar por encima de una rama, desafortunadamente se le engancha el pie de atrás al intentar pasarla. Al caerse se raspa la rodilla y se hace sangre. Empieza a llorar hasta que su madre va a verla. ')
        golpe_de_suerte(sandra)
        if golpe_de_suerte(sandra) <= 0:
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

# Sistema  de rescate

def estrategia_de_rescate():
    global unicornio_salvado
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
            print(emoji.emojize(':confetti_ball::confetti_ball:Sandra y Valeria han recibido la bendición de la magia del unicornio. A partir de ahora la suerte les sonreirá aun mas'))
            sandra.suerte += 1
            valeria.suerte += 1
            unicornio_salvado = True
            ascenso_a_la_montaña()
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

        suerte_sandra = golpe_de_suerte(sandra)
        suerte_valeria = golpe_de_suerte(valeria)
        inteligencia = suerte_sandra + suerte_valeria + sandra.inteligencia + valeria.inteligencia
        if inteligencia >= 16:
            print('Las dos a la vez empujan el palo hacia arriba. El palo cruje y parece que se va a romper pero consiguen levantar lo bastante para que el unicornio se revuelva y consiga salir de debajo del árbol.')
            print('El unicornio se mantiene erguido y orgulloso contemplando a sus rescatadoras. Amistosamente se acerca primero a la princesa y luego a la reina y gacha la cabeza como haciendo una reverencia y las acaricia suavemente con el cuerno en la frente.')
            print('Cuando el cuerno las roza, puede verse por un instante un destello de luz, casi como un arcoíris. Después se aleja trotando alegremente por el bosque rezumando felicidad y magia por todo su ser.')
            print(emoji.emojize(':confetti_ball::confetti_ball:Sandra y Valeria han recibido la bendición de la magia del unicornio. A partir de ahora la suerte les sonreirá aun mas'))
            sandra.suerte += 1
            valeria.suerte += 1
            unicornio_salvado = True
            ascenso_a_la_montaña()
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

# Llamada a la policía

def llamada_a_la_policía():
    print('Llegando al castillo el teléfono de Sandra recupera la suficiente cobertura como para poder hacer una llamada. Dado que es una reina, Sandra no llama a la guardia forestal directamente, eso es poca cosa para ella, ella llama al ministerio de exteriores español, al despacho del ministro nada menos.')
    print('- Despacho del Ministro de Exteriores. El señor ministro ahora esta ocupado en una reunión. Si es tan amable de dejar un mensaje conmigo, su secretaria, se lo haré llegar lo antes posible.')
    print('-Buenos días. Soy su majestad la reina Sandra legitima soberana de HASTA EL COÑO Y MAS ALLÁ. Necesito hablar inmediatamente con el señor ministro. Tengo una situación de máxima urgencia asi que paseme con el INMEDIATAMENTE.')
    suerte_sandra = golpe_de_suerte(sandra)
    negociación = suerte_sandra + sandra.carisma
    if negociación > 8:
        print('-Discúlpeme majestad. Enseguida le paso.')
        print('-Ministro de exteriores al habla, dígame majestad.')
        print('-Necesito inmediatamente que manden un equipo de rescate de guardias forestales. Tenemos un unicornio atrapado bajo un árbol en el bosque del reino.')
        print('-¿Disculpe?¿Un unicornio ha dicho?No quisiera sonar irrespetuoso o insinuar nada, pero los unicornios no existen majestad.')
        print('-Puedes mandar un equipo de rescate inmediatamente para salvar a ese unicornio, o puedes explicarle a los españoles porque ya no se venden mis torrijas en territorio nacional, los franceses llevan haciéndome ofertas años y están dispuestos a pagar mejor que vosotros. La única razón por la que no había aceptado aun es porque son franceses, pero eso puede cambiar en cualquier momento.')
        print('-Discúlpeme majestad, por su puesto majestad, inmediatamente majestad. Estarán allí lo antes posible.')
        print('-Y acompañados de una disculpa suya, escrita a mano, firmada y sincera.')
        print('Por supuesto majestad, estarán en la puerta de su castillo lo antes posible.')
        llegada_de_la_ayuda()
    else:
        print('-Disculpe "alteza" estoy bastante segura de que es país no existe y en el ministerio no apreciamos las bromas telefónicas. Puede decirme quien es y que quiere o haga el favor de dejar la linea libre, que esto es un ministerio.')
        print('-Mira niña voy a darte cinco minutos para que uses Google. Yo espero.')
        time.sleep(5)
        print('Discúlpeme alteza, en seguida la paso.')
        print('-Ministro de exteriores al habla, dígame majestad.')
        print('-Necesito inmediatamente que manden un equipo de rescate de guardias forestales. Tenemos un unicornio atrapado bajo un árbol en el bosque del reino.')
        print('-¿Disculpe?¿Un unicornio ha dicho?No quisiera sonar irrespetuoso o insinuar nada, pero los unicornios no existen majestad.')
        print('-Puedes mandar un equipo de rescate inmediatamente para salvar a ese unicornio, o puedes explicarle a los españoles porque ya no se venden mis torrijas en territorio nacional, los franceses llevan haciéndome ofertas años y están dispuestos a pagar mejor que vosotros. La única razón por la que no había aceptado aun es porque son franceses, pero eso puede cambiar en cualquier momento.')
        print('-Discúlpeme majestad, por su puesto majestad, inmediatamente majestad. Estarán allí lo antes posible.')
        print('-Y acompañados de una disculpa suya, escrita a mano, firmada y sincera.')
        print('Por supuesto majestad, estarán en la puerta de su castillo lo antes posible.')
        llegada_de_la_ayuda()

# Primer final

def llegada_de_la_ayuda():
    print('Sandra y Valeria se sientan nerviosamente a esperar.')
    if gudetama == False:
        print('Sakipillo les trae una selección de bebidas (zumos, coca-cola, fanta, café, etc) y les sirve algo ellas mientras esperan a que lleguen los refuerzos.')
    elif gudetama == True:
        print('Sakipillo y Gudetama les traen una selección de bebidas (zumos, coca-cola, fanta, café, etc) y les sirven algo mientras ellas esperan a que lleguen los refuerzos.')
    else:
        print('Nota del autor: No tengo ni idea de que ha pasado aquí, la idea es que si elegiste comerte a Gudetama solo Sakipillo les llevaría unas bebidas, si no los 2, pero algo salio mal.')
    print('A las pocas horas llegaron los guardias forestales. Llegaron en varias camionetas llenas hasta arriba de motosierras, poleas, cuerdas, sierras... Todo lo que puedas imaginar necesario o util para rescatar a cualquiera o cualquier cosa de debajo de un árbol.')
    print('La reina y la princesa rápidamente les guían hacia el lugar donde el unicornio esta atrapado. Cuando llegan al lugar Sandra y Valeria rápidamente van a confortar y calmar a la criatura mientras los guardias forestales se ponen manos a la obra.')
    print('Un pequeño grupo vuelve a por las herramientas necesarias que estaban en las camionetas, el resto se pone a calzar y montar soportes para sujetar el árbol para aliviar la presión del animal y protegerlo en caso de que algo saliera mal durante el rescate.')
    print('Después atan unas cuerdas al árbol y las pasan por unas poleas. Cuando están firmemente tensadas y sujetas al suelo empiezan primero a cortar ramas y demás cosas que podrían resultar peligrosas. Cuando todo eso por fin esta echo empiezan a cortar una gran sección del árbol.')
    print('Cuando por fin terminan de cortar el tronco lo levantan con ayuda de las poleas. En el momento en el que unicornio tiene suficiente espacio para moverse se ve un cegador destello de luz arcoíris, para cuando los allí presentes pudieron recuperar la vista no había rastro del unicornio por ninguna parte.')
    print('La princesa y la reina volvieron con los guardas al palacio. Al llegar los guardas forestales hicieron un saludo militar y pusieron rumbo para España')
    print(unicornio)
    print(emoji.emojize('\n\n\n\n\n\n\n\n\n:confetti_ball::confetti_ball::confetti_ball::confetti_ball:!!!!HAS FINALIZADO LA RUTA DE RESCATAR AL UNICORNIO CON AYUDA Y VALERIA¡¡¡¡:confetti_ball::confetti_ball::confetti_ball::confetti_ball:'))
    fin_del_juego()
    
# Camino a la montaña
    
def ascenso_a_la_montaña():
    if unicornio_salvado == True:
        print('Con la alegría de haber podido ayudar al unicornio y la sensación dentro de sus corazones de que su suerte había cambiado ligeramente para mejor, Sandra y Valeria vuelven al sendero y lo continúan alegremente. Lo mas curioso es de todo es que la reina empezó a notar que los pájaros ya no las sobrevolaban, quizá el unicornio hizo algo que impide el bombardeo aviario, al menos en un futuro cercano.')
    else:
        print('Con la precaución por bandera y la seguridad de Valeria en mente la reina decidió ignorar el sospechoso bulto en el bosque y continuar con su camino.')
        ataque_aéreo()
    print('Al llegar al pie de la montaña tranquilamente empezaron el ascenso, no era una una pendiente muy inclinada y se subía con facilidad. Según van subiendo el bosque muy lentamente empieza a despejarse, no tanto como para que vieran menos árboles, pero les daban mas a menudo los rayos del sol.')
    print('Al llegar hacia la mitad de la montaña el camino se bifurca en dos, ambos caminos parecen ser prácticamente iguales pero cada uno se siente distinto. Cuando sus altezas se centran en el camino de la derecha algo inquietante les recorre el cuerpo, puede ser bueno, puede ser malo, no lo tienen nada claro, sin embargo al centrarse en el camino de la derecha la sensación que tienen es que todavía no pasa nada, pero dentro de poco pasaría. Esto era algo que ellas no entendían bien, quizá lo estaban imaginando, desde luego esto era la primera vez que les pasaba.')
    bifurcación()

# Bifurcación del ascenso

def bifurcación():
    dirección = input(str('¿Deben de ir hacia la "derecha", la "izquierda" o "volver" al castillo?\n'))
    if dirección == 'derecha':
        cueva()
    elif dirección == 'izquierda':
        cumbre_de_la_montaña()
    elif dirección == 'volver':
        retorno_al_castillo()
    else:
        print(fallo)
        bifurcación()

# Introducción al dios tallarín
def cueva():
    print('Sus altezas se deciden por la ruta de la derecha intentando no hacerle mucho caso a ese extraño sentimiento que les inunda el pecho con cada paso que dan. Al cavo de unos minutos consiguen olvidar la extraña sensación y vuelven a disfrutar del paseo y el suave ascenso a la cima.')
    print('Como a tres cuartas partes de la altura de ascenso total se encuentran con una cueva. Generalmente Sandra ignoraría la cueva, sabe que son peligrosas, en ellas viven animales que pueden atacar si se sienten amenazados, sin luz, pueden tropezarse, o incluso podría haber algún socavón profundo. Pero parecía haber una hoguera al fondo y la reina definitivamente quería averiguar si alguien más vivía en su reino, ella no toleraría invasores bajo ninguna circunstancia.')
    print('Asi que con la ayuda de la linterna del Movil y el fuego al fondo se adentran en la cueva. Al acercarse a la hoguera ven lo que parece un hombre mayor, alto, con barba, cubierto con una manta o túnica y parecía estar inmerso en sus pensamientos')
    print('Sandra:\n-¡¿Quien es usted y que hace en mi reino!?\n El hombre sonrió y las miro a los ojos, con la clase de mirada que tiene aquellas personas que son capaces de ver dentro del alma de cualquiera y entender mas allá de lo que se les pone delante.')
    print('Anciano:\n- Buenos... ¿días?, ¿tardes?, no estoy seguro de la hora, pero no importa, las estaba esperando majestades. Por favor acérquense, siéntense, tómense algo conmigo, estarán cansadas después de llevar paseando tanto rato.')
    print('Sandra, preocupada y sin pensarlo cogió de la mano a Valeria y la medio escondió detrás de ella queriendo protegerla, a pesar de no creer que estaban en autentico peligro el anciano parecía saber mas de lo que debía y eso no le gustaba.')
    print('Sandra:\n-¿Quien es usted y que quiere? No voy a tolerar la presencia de desconocidos en mi reino')
    print('Anciano:\n-Quien soy no es importe y le garantizo que mi presencia no tendrá que ser tolerada por mucho tiempo, pase lo que pase, para esta noche me habré marchado. Ahora mismo, en la cima de la montaña se esta realizando un ritual prohibido si lo llevan a cabo con éxito el resultado puede ser impredecible. Es vuestro reino y vuestro amigo, eso lo hace vuestra responsabilidad. Yo puedo o no ayudaros, pero de nuevo vuestra responsabilidad, vuestra decision.')
    print('Sandra:\n-¿Como que mi amigo?¿Y un ritual?¿Que ritual?\nValeria no paraba de mirar alrededor, no entendía lo que estaba pasando pero era muy inteligente y observadora. Rápidamente se dio cuenta de que la sombra del anciano era extraña, parecía una gran pelota pero no era perfectamente redonda tenia bultos, como si fuera un ovillo de cables y tenia dos grandes y largos brazos, lisos, algo perecido a tentáculos. También se dio cuenta de que había una lata en el fuego con lo que parecía una albóndiga flotando encima y su túnica parecía hecha por alguna clase de fibra gruesa o tejido extraño, realmente parecían espaguetis, pero eso no podía ser.')
    print('Valeria también se dio cuenta de que la actitud del anciano no era una que había visto nunca, el anciano no parecía estar ahi o tratarlas como si realmente estuvieran allí, no podía explicárselo bien a si misma, pero la sensación que tenia era que el anciano estaba simplemente paseando por el zoo y ellas eran una atracción sin importancia, algo como las cabras, que te paras un momento a verlas y te pueden hacer gracia pero si no estuvieran tampoco son la razón para ir al zoo')  
    print('Anciano:\n-Majestad esas preguntas se vas a responder solas para ti y no son interesantes para mi pero quisiera ayudar.¿Estaríais dispuestas a responder a mis preguntas, es importante para saber como puedo ayudar mejor a sus majestades?')
    print('Sandra:\n-¡¿Tu te crees que somos tus monos de feria?! Vete a...\n El anciano hizo un gesto provocando que la reina se callara en ese instante.')
    cuestionario_tallarín

def cuestionario_tallarín():
    cuestionario = input(str('Si no quieres mi ayuda dilo, pero estoy buscando un "sí" o un "no", el resto es innecesario y no tenéis tiempo.'))
    if cuestionario == 'sí':
        print('Después de pensarlo por un momento la reina miro a Valeria y esta asintió con la cabeza como diciendo adelante')

def cumbre_de_la_montaña():
    print('culo')

# Segundo final posible
 
def retorno_al_castillo():
    if unicornio_salvado == True:
        print('El dia esta despejado, ni un solo pájaro sobrevuela a sus altezas')
    elif unicornio_salvado == False:
        ataque_aéreo
    else:
        print(nota_de_autor)
    print('Sandra y Valeria no tenían nada claro porque sentían lo que sentían al llegara a esa intersección pero tenían muy claro que no les gustaba puesto que no se lo podían explicar en absoluto. Descendieron la montaña tranquilamente, disfrutando del paseo, charlando, contemplando la fauna y la flora.')
    if gudetama == False:
        print('Al llegar ya esta anocheciendo, sus majestades deciden darse una ducha mientras Sakippillo les prepara la cena.')
    elif gudetama == True:
        print('Al llegar ya esta anocheciendo, sus majestades deciden darse una ducha mientras Sakippillo y Gudetama les preparan la cena.')
    else:
        print(nota_de_autor)
    if unicornio_salvado == True:
        print(unicornio)
        print(emoji.emojize('\n\n:confetti_ball::confetti_ball::confetti_ball::confetti_ball:!!!!HAS FINALIZADO LA RUTA DE RESCATAR AL UNICORNIO CON AYUDA Y VALERIA¡¡¡¡ y luego te has rajado y has vuelto al castillo sin seguir explorando mucho mas.:confetti_ball::confetti_ball::confetti_ball::confetti_ball:'))
        fin_del_juego()
    elif unicornio_salvado == False:
        print('La princesa y la reina cenan y se van a la cama. A pesar de haber tenido un dia agradable y tranquilo se acuestan pensando que su dia podía haber sido mucho mas de lo que había sido.')
        print('NO ME INVESTIGAS QUE PASA EN EL BOSQUE, NO SIGUES SUBIENDO LA MONTAÑA PARA VER QUE HAY EN LA CIMA, NADA. ¿SE PUEDE SABER PARA QUE HAS ENCENDIDO ESTE JUEGO? ESPERO QUE HALLAS LLEGADO AQUÍ SOLO PORQUE QUERÍAS VER TODAS LAS OPCIONES POSIBLES.')
        fin_del_juego()

def entrada_al_bosque():
    print('pedo')

def fin_del_juego():
    que_hacer = input(str('¿Quieres volver a "jugar" o "dejarlo" por el momento?\n'))
    if que_hacer == 'jugar':
        inicio()
    elif que_hacer == 'dejarlo':
        print('Hasta la próxima.')
        time.sleep(5)
        sys.exit()
    else:
        print(fallo)
        fin_del_juego()
inicio()