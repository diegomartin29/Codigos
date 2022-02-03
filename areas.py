# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:20:56 2021

@author: DiegoMartínLópez
"""
#Dada la siguiente lista, que contiene las medidas de base y altura respectivas 
#para 5 triángulos, calcular el área de todos ellos:
    
listaTriangulos=[(3,2), (1, 5), (6, 7)]
"""
triangulos=[
            (3,2),  Triángulo 1: base:3 - altura, 2
            (1, 5), Triángulo 2: base:1 - altura, 5 
            (6, 7) Triángulo 3: base:6 - altura, 7
           ]

"""
import math 
for triangulo in listaTriangulos:
    # obtengo uno a uno los elementos de la lista, es decir
    # obtengo uno a uno los triángulos de la lista
    # print(triangulo)
    # print(f"\t Base:{triangulo[0]}")
    # print(f"\t Altura:{triangulo[1]}")
    areaTriangulo=triangulo[0]*triangulo[1]/2
    print(f"El área del triángulo de base {triangulo[0]} y altura {triangulo[1]} es {areaTriangulo} metros cuadrados")
    
print("RECTANGULOS")
listaRectangulos=[(3,2), (1, 5), (6, 7)]
for rectangulo in listaRectangulos:
    # obtengo uno a uno los elementos de la lista, es decir
    # obtengo uno a uno los triángulos de la lista
    # print(rectangulo)
    # print(f"\t Base:{triangulo[0]}")
    # print(f"\t Altura:{triangulo[1]}")
    areaRectangulo=rectangulo[0]*rectangulo[1]
    print(f"El área del triángulo de base {rectangulo[0]} y altura {rectangulo[1]} es {areaRectangulo} metros cuadrados")

print("CIRCULOS")
listaCirculos=[3, 6, 1, 9, 5]
print("Pi: ", math.pi)
print("Pi con dos decimales: ", round(math.pi, 2))

for radio in listaCirculos:
    area=math.pi*radio**2
print(f"El area del circulo de valor {radio} = {round(area,2)} metros cuadrados")

print("CUADRADOS")
listaCuadrado=[4, 5 ,7, 8, 2, 1, 6]
for lado in listaCuadrado:
    area=lado**2
    print(f"El area del cuadrado de lado {lado} es {area} metros cuadrados")
    
listaRectangulos2= [(3,-2), (1,5), (6,7)]
for rectangulo2 in listaRectangulos2:
    if(rectangulo2[0]<=0 or rectangulo2[1]<=0):
         print(f"El elemento erróneo {rectangulo2}")
         
         #range(len(lista)-1, -1, -1)
for indice in range(len(listaRectangulos)-1, -1, -1):
    #comprobación y si es necesario borrado del elemento
    print(listaRectangulos[indice][1])
    if(listaRectangulos[indiceListaRectangulos][0]<=0 or listaRectangulos[indiceListaRectangulos][1]<=0):
        print(f"Elemento erróneo {listaRectangulos[indice]}")
    

        
        
