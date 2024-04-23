def choice():
    miembros = 0

    def toreto(miembros):
        if miembros == 0:
            partner = input(str('"brian" "leti" "roman"'))
            if partner == 'brian':
                print(miembros)
                brian()
            elif partner == 'leti':
                print(miembros)
                leti()
            elif partner == 'roman':
                print(miembros)
                roman()
            else:
                toreto(miembros)   
        elif miembros == 1:
            partner = input(str('"leti" "roman"'))
            if partner == 'leti':
                print(miembros)
                leti()
            elif partner == 'roman':
                print(miembros)
                roman()
            else:
                toreto(miembros)
        elif miembros == 2:
            partner = input(str('"brian" "roman"'))
            if partner == 'brian':
                print(miembros)
                brian()
            elif partner == 'roman':
                print(miembros)
                roman()
            else:
                toreto(miembros)
        elif miembros == 3:
            partner = input(str('"roman"'))
            if partner == 'roman':
                print(miembros)
                roman()
            else:
                toreto(miembros)
        elif miembros == 4:
            partner = input(str('"brian" "leti"'))
            if partner == 'brian':
                print(miembros)
                brian()
            elif partner == 'leti':
                print(miembros)
                leti()
            else:
                toreto(miembros)
        elif miembros == 5:
            partner = input(str('"leti"'))
            if partner == 'leti':
                print(miembros)
                leti()
            else:
                toreto(miembros)
        elif miembros == 6:
            partner = input(str('"brian'))
            if partner == 'brian':
                print(miembros)
                brian()
            else:
                toreto(miembros)
        else:
            print('let\'s race')

    def brian():
        nonlocal miembros
        miembros += 1
        print('let\'s go brother')
        toreto(miembros)

    def leti():
        nonlocal miembros
        miembros += 2
        print('OK Dom')
        toreto(miembros)

    def roman():
        nonlocal miembros
        miembros += 4
        print('Look at my orange lambo')
        toreto(miembros)

    toreto(miembros)


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

sandra = Personaje('Sandra', 'Mujer', 'Humana', 6, 8, 7, 5, True)

sandra.fuerza += 1

print(vars (sandra))


