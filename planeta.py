

import math

class Planeta:
  def_init_(self, nombre, masa, radio, distancia_al_sol, tiene_vida=false):
  self.nombre = nombre
  self.masa = masa
  self.radio = radio
  self.distancia_al_sol = distancia_al_sol
  self.tiene_vida = tiene_vida

  def calcular_densidad(self):
    volumen=(4/3)* math.pi*self.radio **3
    densidad= self.masa/volumen
    return densidad
  
  
  def es_Planeta_exterior(self):
    return self.distancia_al_sol < 5.2
    
  def _str_(self):
    tipo= "Exterior" if.self.es_planeta_exterior() else "Interior"
    return (
      f"Planeta": {self.nombre}/n"
    f"Densidad: {self.calcular_densidad:.2f} kg/m3/n"
    f"tipo: {tipo}/n"
    f"tiene vida:{self.tiene_vida}"
    )

planeta1= Planeta(
  "Tierra",
  5.972e24
  6.31e6
1.0
True
)

planeta2= Planeta(
  "Jupiter"
  1.898e27
  6.9911e7
  5.2
  )
   print(planeta1)
   print()
   print(planeta2)
   
    

