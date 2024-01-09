# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:06:56 2023

@author: saulpdev
"""
#Ejemplo de programacion orientado a objetos 

#Definimos las clases
class Martillo:
    def __init__(self, tipo_mango="madera"):
        self.tipo_mango = tipo_mango

    def martillar(self):
        print("¡Martillando!")

    def sacar_clavos(self):
        print("Sacando clavos.")

# Ejemplo de uso

martillo_goma = Martillo(tipo_mango="goma")
martillo_madera = Martillo()


#instanciamos
print("Martillo ")
print("Tipo de mango:", martillo_goma.tipo_mango)
martillo_goma.martillar()
martillo_goma.sacar_clavos()

print("\nMartillo ")
print("Tipo de mango:", martillo_madera.tipo_mango)
martillo_madera.martillar()
martillo_madera.sacar_clavos()
