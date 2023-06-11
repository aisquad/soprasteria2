"""
Desarrolle un algoritmo para el cálculo del salario de un trabajador. El importe
liquidado (sueldo) depende de una tarifa o precio por hora establecida y de un
condicionante sobre las horas trabajadas: si la cantidad de horas trabajadas es mayor a
40 horas, la tarifa se incrementa en un 50% para las horas extras. Calcular el sueldo
recibido por el trabajador en base las horas trabajadas y la tarifa. Utilice las
instrucciones LEER HORASTRABAJADAS y LEER TARIFA al inicio del programa para
cargar los valores en las variables HORASTRABAJADAS y TARIFA.
"""


def leer_horas_trabajadas(horas):
    extras = horas - 40 if horas - 40 > 0 else 0
    estipuladas = horas - extras
    return estipuladas, extras


def leer_tarifa(horas, tarifa):
    estipuladas, extras = leer_horas_trabajadas(horas)
    return (estipuladas * tarifa) + (extras * tarifa * 1.5)


if __name__ == '__main__':
    print(leer_tarifa(90, 60))
    print(leer_tarifa(35, 40))