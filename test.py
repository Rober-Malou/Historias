import random
import climage 

# converts the image to print in terminal 
# inform of ANSI Escape codes 
output = climage.convert('circulo_invocacion.jpg') 

# prints output on console. 
print(output)


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
