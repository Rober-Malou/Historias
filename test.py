def choice():
    miembros = 0
    def toreto(miembros):
        if toreto == 0:
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
                toreto()
        elif toreto == 1:
            partner = input(str('"leti" "roman"'))
            if partner == 'leti':
                print(miembros)
                leti()
            elif partner == 'roman':
                print(miembros)
                roman()
            else:
                toreto()
        elif toreto == 2:
            partner = input(str('"brian" "roman"'))
            if partner == 'brian':
                print(miembros)
                brian()
            elif partner == 'roman':
                print(miembros)
                roman()
            else:
                toreto()
        elif toreto == 3:
            partner = input(str('"roman"'))
            if partner == 'roman':
                print(miembros)
                roman()
            else:
                toreto()
        elif toreto == 4:
            partner = input(str('"brian" "leti"'))
            if partner == 'brian':
                print(miembros)
                brian()
            elif partner == 'leti':
                print(miembros)
                leti()
            else:
                toreto()
        elif toreto == 5:
            partner = input(str('"leti"'))
            if partner == 'leti':
                print(miembros)
                leti()
            else:
                toreto()
        elif toreto == 6:
            partner = input(str('"brian'))
            if partner == 'brian':
                print(miembros)
                brian()
        else:
            print('let\'s race')
    def brian():
        miembros =+ 1
        print('let\'s go brother')
        toreto()

    def leti():
        miembros =+ 2
        print('OK Dom')
        toreto()

    def roman():
        miembros =+ 4
        print('Look at my orange lambo')
        toreto()
    toreto()
choice()