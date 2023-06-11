"""
Escriba un algoritmo que lea un número entero y determine si es par o impar. Si es par,
que escriba todos los pares de manera descendiente desde sí mismo y hasta el cero. Si
es impar, que escriba todos los impares de manera descendiente desde si sí mismo
hasta el uno. Utilice la instrucción LEER NUMERO al inicio del programa para cargar un
número en la variable NUMERO.
"""
from typing import NoReturn


def leer_numero(entero) -> NoReturn:
    print(', '.join(f'{_}' for _ in range(entero, -1, -2)))


if __name__ == '__main__':
    for numero in (1, 2, 3, 10, 11):
        print(f"== entero: {numero} ==")
        leer_numero(numero)
        print()
