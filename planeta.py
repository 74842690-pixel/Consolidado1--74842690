
import math


class Planeta:

    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida

    def calcular_densidad(self):
        volumen = (4 / 3) * math.pi * self.radio ** 3
        densidad = self.masa / volumen
        return densidad

    def es_planeta_exterior(self):
        return self.distancia_al_sol > 5.2

    def __str__(self):
        tipo = "Exterior" if self.es_planeta_exterior() else "Interior"

        return (
            f"Nombre: {self.nombre}\n"
            f"Densidad: {self.calcular_densidad():.2f} kg/m³\n"
            f"Tipo: {tipo}"
        )


# INSTANCIAS DE PRUEBA


planeta1 = Planeta(
    "Tierra",
    5.972e24,
    6.371e6,
    1.0,
    True
)

planeta2 = Planeta(
    "Jupiter",
    1.898e27,
    6.9911e7,
    5.2
)


# MOSTRAR INFORMACIÓN


print(" PLANETA 1 ")
print(planeta1)

print("\n PLANETA 2 ")
print(planeta2)
   
    

