
 def _init_(self, marca, modelo, velocidad_max,
                 nivel_combustible, año_fabricacion):

        self.marca = marca
        self.modelo = modelo
        self._velocidad_max = 0
        self._nivel_combustible = 0.0
        self._año_fabricacion = 0

        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

 
    @property
    def año_fabricacion(self):
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, año):
        if año < 1886 or año > 2026:
            raise ValueError(
                "El año de fabricación debe estar entre 1886 y 2026."
            )
        self._año_fabricacion = año


    # NIVEL DE COMBUSTIBLE


    @property
    def nivel_combustible(self):
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, nivel):
        if nivel < 0.0 or nivel > 100.0:
            raise ValueError(
                "El nivel de combustible debe estar entre 0.0 y 100.0."
            )
        self._nivel_combustible = nivel

    
    # PROPERTY: VELOCIDAD MÁXIMA
    
    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, velocidad):
        if velocidad <= 0:
            raise ValueError(
                "La velocidad máxima debe ser mayor que 0."
            )
        self._velocidad_max = velocidad

    
    # MÉTODO TIEMPO DE LLEGADA

    def tiempo_llegada(self, distancia_km):
        return distancia_km / self.velocidad_max
   
    # MÉTODO STR
  
    def _str_(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Velocidad máxima: {self.velocidad_max} km/h\n"
            f"Nivel de combustible: {self.nivel_combustible}%\n"
            f"Año de fabricación: {self.año_fabricacion}"
        )


# PRUEBA DEL AUTOMÓVIL

auto = Automovil(
    "Toyota",
    "Corolla",
    180.0,
    75.0,
    2022
)

print("===== DATOS DEL AUTOMÓVIL =====")
print(auto)

print("\n===== TIEMPO DE LLEGADA =====")
distancia = 360
tiempo = auto.tiempo_llegada(distancia)

print(f"Distancia: {distancia} km")
print(f"Tiempo de llegada: {tiempo:.2f} horas")


# PRUEBA DE PROPIEDADES


print("\n===== PRUEBA DE PROPIEDADES =====")

auto.velocidad_max = 200.0
print(f"Nueva velocidad máxima: {auto.velocidad_max} km/h")

auto.nivel_combustible = 90.0
print(f"Nuevo nivel de combustible: {auto.nivel_combustible}%")

auto.año_fabricacion = 2024
print(f"Nuevo año de fabricación: {auto.año_fabricacion}")


# PRUEBA DE VALIDACIÓN


print("\n===== PRUEBA DE VALIDACIÓN =====")

try:
    auto.año_fabricacion = 1800
except ValueError as error:
    print(f"Error detectado: {error}")
  
