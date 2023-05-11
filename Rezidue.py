# Rezidue- Es un programa para el calculo de fluido en un tubo, usando la ecuación de Bernoulli. 
# Desarrollado por CORSARIO_CL
#==========================================================

import math

densidad_fluido = float(input("Ingrese la densidad del fluido (kg/m^3): "))
velocidad_fluido = float(input("Ingrese la velocidad del fluido (m/s): "))
diametro_tubo = float(input("Ingrese el diámetro del tubo (m): "))
altura_fluido = float(input("Ingrese la altura del fluido (m): "))
gravedad = float(input("Ingrese la aceleración debida a la gravedad (m/s^2): "))

pi = math.pi
area_tubo = pi * (diametro_tubo / 2) ** 2
energia_cinetica = 0.5 * densidad_fluido * velocidad_fluido ** 2
energia_potencial = densidad_fluido * gravedad * altura_fluido
energia_total = energia_cinetica + energia_potencial
presion_tubo = energia_total / densidad_fluido
flujo_volumetrico = area_tubo * velocidad_fluido

print("El flujo volumétrico es:", flujo_volumetrico, "m^3/s")
print("La presión en el tubo es:", presion_tubo, "Pa")
