print('¿Cuál es la velocidad de la luz?')
print('a) 320 m/seg')
print('b) 150.000 km/seg')
print('c) 300.000 km/seg')

velocidad = str(input('Introduce a, b, ó c:\n'))
if velocidad == 'c':
    puntos1 = 10
if velocidad == 'a' or velocidad == 'b':
    puntos1 = -5

print('¿Cuál es la distancia media a la Luna?')
print('a) 563.000 km')
print('b) 384.400 km')
print('c) 150.900 km')

distancia = str(input('Introduce a, b, ó c:\n'))
if distancia == 'b':
    puntos2 = puntos1 + 10
if distancia == 'a' or distancia == 'c':
    puntos2 = puntos1 - 5
"""if puntos2 < 0:
    puntos2 = 0"""

print('¿Cuál es el diámetro de la Tierra?')
print('a) 12.742 km')
print('b) 15.745 km')
print('c) 60.226 km')

diametro = str(input('Introduce a, b, ó c:\n'))
if diametro == 'a':
    puntos3 = puntos2 + 10
if diametro == 'b' or diametro == 'c':
    puntos3 = puntos2 - 5
"""if puntos3 < 0:
    puntos3 = 0"""

print('¡Has conseguido ', puntos3, ' puntos!')

input('Pulse INTRO para finalizar...') # Hago una pausa.