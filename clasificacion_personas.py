"""
Escriba un algoritmo que visualice una clasificación de 50 personas según edad y sexo.
Deberá mostrar los siguientes resultados:
a. Cantidad de personas mayores de edad (18 años o más).
b. Cantidad de personas menores de edad.
c. Cantidad de personas masculinas mayores de edad.
d. Cantidad de personas femeninas menores de edad.
e. Porcentaje que representan las personas mayores de edad respecto al total de
personas.
f. Porcentaje que representan las mujeres respecto al total de personas.

Utilice la instrucción LEER PERSONAS al inicio del programa para cargar los datos de las
50 personas en un variable, PERSONAS, que actúa como un vector de 50 posiciones.
Cada elemento de PERSONAS es de un tipo estructurado que dispone dos campos:
SEXO y EDAD.
"""
import random
from typing import List


class Persona:
    def __init__(self, sexo, edad):
        self.sexo = sexo
        self.edad = edad

    def __repr__(self):
        return f"<Pers.: {self.sexo} {self.edad}>"


class Resultado:
    def __init__(self):
        self.mayores_de_edad = 0
        self.menores_de_edad = 0
        self.masculinas_mayores_de_edad = 0
        self.femeninas_menores_de_edad = 0
        self.total_mujeres = 0
        self.talla = 0

    @property
    def porcentaje_mayores(self):
        return self.mayores_de_edad * 100 / self.talla

    @property
    def porcentaje_femenino(self):
        return self.total_mujeres * 100 / self.talla

    def __str__(self):
        return f"Mayores de edad: {self.mayores_de_edad}\n" \
               f"Menores de edad: {self.menores_de_edad}\n" \
               f"Masculinas mayores de edad: {self.masculinas_mayores_de_edad}\n" \
               f"Femeninas menores de edad: {self.femeninas_menores_de_edad}\n" \
               f"Mayores de edad respecto al total: {self.porcentaje_mayores:.2f} %\n" \
               f"Mujeres respecto al total: {self.porcentaje_femenino:.2f} %"


def leer_personas(personas: List[Persona]):
    resultado = Resultado()
    resultado.talla = len(personas)
    for persona in personas:
        if persona.edad >= 18:
            resultado.mayores_de_edad += 1
            if persona.sexo == 'M':
                resultado.masculinas_mayores_de_edad += 1
            else:
                resultado.total_mujeres += 1
        else:
            if persona.sexo == 'F':
                resultado.femeninas_menores_de_edad += 1
    resultado.menores_de_edad = 50 - resultado.mayores_de_edad
    resultado.total_mujeres += resultado.femeninas_menores_de_edad

    return resultado


if __name__ == '__main__':
    lista_personas = [Persona(random.choice(['M', 'F']), random.randint(1, 99)) for _ in range(50)]
    print(lista_personas)
    res = leer_personas(lista_personas)
    print(res)