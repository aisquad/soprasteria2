"""
Desarrolle un algoritmo para el cálculo del salario de un trabajador. El importe
liquidado (sueldo) depende de una tarifa o precio por hora establecida y de un
condicionante sobre las horas trabajadas: si la cantidad de horas trabajadas es mayor a
40 horas, la tarifa se incrementa en un 50% para las horas extras. Calcular el sueldo
recibido por el trabajador en base las horas trabajadas y la tarifa. Utilice las
instrucciones LEER HORASTRABAJADAS y LEER TARIFA al inicio del programa para
cargar los valores en las variables HORASTRABAJADAS y TARIFA.
"""

import locale
from typing import Tuple


def leer_horas_trabajadas(horas: int) -> Tuple[int, int]:
    extras = horas - 40 if horas - 40 > 0 else 0
    estipuladas = horas - extras
    return estipuladas, extras


def leer_tarifa(horas_trabajadas: int, tarifa: int) -> str:
    estipuladas, extras = leer_horas_trabajadas(horas_trabajadas)
    sueldo = (estipuladas * tarifa) + (extras * tarifa * 1.5)
    sueldo = locale.format_string('%0.2f', sueldo, True, True)
    return f"Horas trabajadas: {horas_trabajadas} h.\nTarifa: {tarifa} €/h.\nImporte liquidado: {sueldo} €\n"


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'Spanish_Spain.1252')
    for horas, tarifa in ((60, 60), (35, 40)):
        print(f'== parámetros: {horas}, {tarifa} ==')
        resultado = leer_tarifa(horas, tarifa)
        print(resultado)
