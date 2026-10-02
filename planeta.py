

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
    

