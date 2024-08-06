import random

global eleccion
eleccion = random.randint(0, 1)
def caca():
    global eleccion
    if eleccion == 1:
        print('caca')
    else:
        pedo()

def pedo():
    global eleccion
    if eleccion == 0:
        print('pedo')
    else:
        caca()


caca()
pedo()
pedo()
caca()
