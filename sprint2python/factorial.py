# Factorial con recursividad
def func_factorial(n):
    if n == 1:
        return 1
    else:
        return n * func_factorial(n-1)
