"""
Escriba un algoritmo que lea un número entero y determine si es par o impar. Si es par,
que escriba todos los pares de manera descendiente desde sí mismo y hasta el cero. Si
es impar, que escriba todos los impares de manera descendiente desde si sí mismo
hasta el uno. Utilice la instrucción LEER NUMERO al inicio del programa para cargar un
número en la variable NUMERO.
"""


def leer_numero(numero):
    for _ in range(numero, 0, -2):
        print(_)


if __name__ == '__main__':
    entero = 11
    leer_numero(entero)