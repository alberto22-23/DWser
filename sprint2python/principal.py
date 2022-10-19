from factorial import func_factorial

print('Función Factorial (con recursividad). Introducción de datos:')
n = int(input('Introduzca un número entero: '))

resultado = func_factorial(n)

print("Resultado:")
print("El factorial de ", n, " es: ", resultado)

input('Pulse INTRO para finalizar...') # Hago una pausa.