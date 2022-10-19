print('¿Cuál es la velocidad de la luz?')
print('a) 320 m/seg')
print('b) 150.000 km/seg')
print('c) 300.000 km/seg')
velocidad = str(input('Introduce a, b, ó c:\n'))

if velocidad == 'a':
    print('Esa es la velocidad del sonido. Has fallado.')
elif velocidad == 'b':
    print('No es correcto. Has fallado.')
else:
    print('¡Correcto!')
input('Pulse INTRO para finalizar...') # Hago una pausa.