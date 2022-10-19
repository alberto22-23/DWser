import random 

preguntas = ['pregunta1', 'pregunta2', 'pregunta3']

listaResultado = random.sample(preguntas, 2)
print(listaResultado)

#puntos1 = 0 
#puntos2 = 0
#puntos3 = 0
#puntosTotales = 0

def func_pregunta1():
    #global puntos1
    global puntosTotales
    print('¿Cuál es la velocidad de la luz?')
    print('a) 320 m/seg')
    print('b) 150.000 km/seg')
    print('c) 300.000 km/seg')

    velocidad = str(input('Introduce a, b, ó c:\n'))
    if velocidad == 'c':
        #puntos1 = 10
        puntosTotales = 10
    if velocidad == 'a' or velocidad == 'b':
        #puntos1 = -5
        puntosTotales = -5
    #puntosTotales = puntos1

def func_pregunta2():
    global puntosTotales
    #global puntos2
    print('¿Cuál es la distancia media a la Luna?')
    print('a) 563.000 km')
    print('b) 384.400 km')
    print('c) 150.900 km')

    distancia = str(input('Introduce a, b, ó c:\n'))
    if distancia == 'b':
        #puntos2 = puntosTotales + 10
        puntosTotales = puntosTotales + 10
    if distancia == 'a' or distancia == 'c':
        #puntos2 = puntosTotales - 5
        puntosTotales = puntosTotales - 5
    #puntosTotales = puntos2
    """if puntos2 < 0:
        puntos2 = 0"""

def func_pregunta3():
    global puntosTotales
    #global puntos3
    print('¿Cuál es el diámetro de la Tierra?')
    print('a) 12.742 km')
    print('b) 15.745 km')
    print('c) 60.226 km')
    
    diametro = str(input('Introduce a, b, ó c:\n'))
    if diametro == 'a':
        #puntos3 = puntosTotales + 10
        puntosTotales = puntosTotales + 10
    if diametro == 'b' or diametro == 'c':
        #puntos3 = puntosTotales - 5
        puntosTotales = puntosTotales - 5
    #puntosTotales = puntos3
    """if puntos3 < 0:
        puntos3 = 0"""


if listaResultado[0] == "pregunta1":
    func_pregunta1()

if listaResultado[0] == "pregunta2":
    func_pregunta2()

if listaResultado[0] == "pregunta3":
    func_pregunta3()

if listaResultado[1] == "pregunta1":
    func_pregunta1()

if listaResultado[1] == "pregunta2":
    func_pregunta2()

if listaResultado[1] == "pregunta3":
    func_pregunta3()  

print('¡Has conseguido ', puntosTotales, ' puntos!')

input('Pulse INTRO para finalizar...') # Hago una pausa.