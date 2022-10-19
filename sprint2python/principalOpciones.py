import time

from factorial import func_factorial

from factorial2 import func_factorial2

print('Cálculo del factorial de un número')
print('a) Cáculo del factorial mediante algoritmo con recursividad:')
print('b) Cáculo del factorial mediante algoritmo con bucle "while":')

eleccion = str(input('Elija opción: a ó b:\n' '> '))

if eleccion == 'a':
    print('Función Factorial con recursividad.')
    n = int(input('Introduzca un número entero: '))
    start_time = time.time()
    resultado = func_factorial(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Resultados:")
    print('El tiempo de ejecución con recursividad ha sido :' + str(elapsed_time) + ' s')
    print("El factorial de ", n, " es: ", resultado)

    input('Pulse INTRO para finalizar...') # Hago una pausa.

elif eleccion == 'b':
    print('Función Factorial con bucle "while".')
    n = int(input('Introduzca un número entero: '))
    start_time = time.time()
    resultado = func_factorial2(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Resultados:")
    print('El tiempo de ejecución con "while" ha sido :' + str(elapsed_time) + ' s')
    print("El factorial de ", n, " es: ", resultado)

    input('Pulse INTRO para finalizar...') # Hago una pausa.

else:
    print('Tecla no válida.')

    input('Pulse INTRO para finalizar...')  # Hago una pausa.