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
import unittest
from typing import List, NoReturn


class Persona:
    def __init__(self, sexo: str, edad: int):
        self.sexo = sexo
        self.edad = edad

    def __repr__(self):
        return f"<Pers.: {self.sexo} {self.edad}>"


class Personas:
    def __init__(self):
        self._limite = 50
        self._lista_personas: List[Persona] = []

    @property
    def limite(self) -> int:
        return self._limite

    def __iter__(self):
        return self._lista_personas.__iter__()

    def __repr__(self):
        return ', '.join(f"{_}" for _ in self._lista_personas)

    def poblar(self, lista_personas: List[Persona]) -> NoReturn:
        if len(lista_personas) != 50:
            raise OverflowError('La lista debe contener 50 elementos')
        elif any([not isinstance(_, Persona) for _ in lista_personas]):
            raise TypeError('La lista debe contener elementos de la clase Persona')
        self._lista_personas = lista_personas

    def poblar_aleatoriamente(self) -> NoReturn:
        lista_personas = [Persona(random.choice(['M', 'F']), random.randint(1, 100)) for _ in range(self.limite)]
        self.poblar(lista_personas)


class Resultado:
    def __init__(self, limite: int):
        self.mayores_de_edad = 0
        self.menores_de_edad = 0
        self.masculinas_mayores_de_edad = 0
        self.femeninas_menores_de_edad = 0
        self.total_mujeres = 0
        self.talla = limite

    @property
    def porcentaje_mayores(self) -> float:
        return self.mayores_de_edad * 100 / self.talla

    @property
    def porcentaje_femenino(self) -> float:
        return self.total_mujeres * 100 / self.talla

    def __str__(self):
        return f"Mayores de edad: {self.mayores_de_edad}\n" \
               f"Menores de edad: {self.menores_de_edad}\n" \
               f"Masculinas mayores de edad: {self.masculinas_mayores_de_edad}\n" \
               f"Femeninas menores de edad: {self.femeninas_menores_de_edad}\n" \
               f"Mayores de edad respecto al total: {self.porcentaje_mayores:.2f} %\n" \
               f"Mujeres respecto al total: {self.porcentaje_femenino:.2f} %"


def leer_personas(lista_personas: Personas) -> NoReturn:
    resultado = Resultado(lista_personas.limite)
    for persona in lista_personas:
        if persona.edad >= 18:
            resultado.mayores_de_edad += 1
            if persona.sexo == 'M':
                resultado.masculinas_mayores_de_edad += 1
            else:
                resultado.total_mujeres += 1
        else:
            if persona.sexo == 'F':
                resultado.femeninas_menores_de_edad += 1
    resultado.menores_de_edad = resultado.talla - resultado.mayores_de_edad
    resultado.total_mujeres += resultado.femeninas_menores_de_edad
    print(resultado)


class TestClass(unittest.TestCase):
    def test_49_personas(self):
        # No contiene suficientes elementos.
        with self.assertRaises(OverflowError):
            test_personas = Personas()
            test_personas.poblar([Persona(random.choice(['M', 'F']), random.randint(1, 100)) for _ in range(49)])
            leer_personas(test_personas)

    def test_51_personas(self):
        # Contiene elementos de más.
        with self.assertRaises(OverflowError):
            test_personas = Personas()
            test_personas.poblar([Persona(random.choice(['M', 'F']), random.randint(1, 100)) for _ in range(51)])
            leer_personas(test_personas)

    def test_contiene_objetos_ajenos(self):
        # Se introduce al menos un elemento que no corresponde al tipo de objeto esperado.
        with self.assertRaises(TypeError):
            test_personas = Personas()
            lista = [Persona(random.choice(['M', 'F']), random.randint(1, 100)) for _ in range(49)]
            lista.append(('F', 27))  # Lo correcto es lista.append(Persona('F', 27))
            test_personas.poblar(lista)

    def test_correcto(self):
        # La inserción de elementos es correcta.
        test_personas = Personas()
        lista = [Persona(random.choice(['M', 'F']), random.randint(1, 100)) for _ in range(49)]
        persona = Persona('F', 27)
        lista.append(persona)
        test_personas.poblar(lista)
        self.assertTrue(len(lista) == 50)
        self.assertListEqual([isinstance(_, Persona) for _ in lista], [True] * 50)


if __name__ == '__main__':
    personas = Personas()
    personas.poblar_aleatoriamente()
    print(personas)
    leer_personas(personas)

    unittest.main()

