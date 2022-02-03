# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:37:52 2021

@author: DiegoMartínLópez
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:40:50 2021

@author: Usuario
"""

#DIEGO MARTÍN LÓPEZ 1DAMB
#Profe, se que no he hecho lo de sustituir los numeros en el boleto por X, he estado mucho tiempo intentandolo pero no he conseguido encontrar la solucion. Espero que no baje mucho la nota


import random

print("Bienvenido a la loteria de Euromillón")

print("-----------------------------------------")

print("PREMIOS EN MÉTALICO")
print("-----------------------------------------")
print("\t1.- 5+2=15000000€                  --")
print("\t2.- 5+1=3000000€                   --")
print("\t3.- 5+0=1500000€                   --")
print("\t4.- 4+2=800000€                    --")
print("\t5.- 4+1=500000€                    --")
print("\t6.- 4+0=350000€                    --")
print("\t7.- 3+2=320000€                    --")
print("\t8.- 3+1=300000€                    --")
print("\t9.- 3+0=150000€                    --")
print("\t10.- 2+2=50000€                    --")
print("\t11.- 2+1=10000€                    --")
print("\t12.- 2+0=60€                       --")
print("-----------------------------------------")


print("BOLETO")
print("--------------------")
print("| 1 10 19 28 37 46 |")
print("| 2 11 20 29 38 47 |")
print("| 3 12 21 30 39 48 |")
print("| 4 13 22 31 40 49 |")
print("| 5 14 23 32 41 50 |")
print("| 6 15 24 33 42    |")
print("| 7 16 25 34 43    |")
print("| 8 17 26 35 44    |")
print("| 9 18 27 36 45    |")
print("--------------------")
print("| 1 5 9  |")
print("| 2 6 10 |")
print("| 3 7 11 |")
print("| 4 8 12 |")
print("--------------------")


#Programamos el boleto que quiere introducir el usuario
#Generamos 5 numeros irrepetibles y de rango 1-50

Num_bol = []
x = 1
while x <= 5:
    numero = int(input(f"Ingrese el numero {x} de su boleto: "))
    while(numero<1 or numero>50):
        print("Debe ser una opción disponible!")
        numero=int(input(f"Ingrese el numero {x} del boleto: "))
    if numero not in Num_bol:
        Num_bol.append(numero)
        x += 1
    else:
        print("El número está repetido, inténtelo con otro...")
        
#Generamos 2 numeros irrepetibles y de rango 1-12
        
Num_est = []
x = 1
while x <= 2:
    numero2 = int(input(f"Ingrese la estrella {x} de su boleto: "))
    while(numero2<1 or numero2>12):
        print("Debe ser una opción disponible!")
        numero2=int(input(f"Ingrese la estrella {x} del boleto: "))
    if numero2 not in Num_est:
        Num_est.append(numero2)
        x += 1
    else:
        print("El número está repetido, inténtelo con otro...")
        
print("----------------------------------------------------------")
                
print(f"Su boleto es : {Num_bol},{Num_est}")

#Ahora, generamos 5 numeros random para determinar el boleto ganador

lista=[]
for boleto in range(5):
    boleto=random.randint(1,50)
    if boleto not in lista:
       lista.append(boleto)
       boleto += 1


    
print("----------------------------------------------------------")


lista2=[]
for estrellas in range(2):
    estrellas=random.randint(1,12)
    if(estrellas not in lista2):
        lista2.append(estrellas)
        estrellas +=1
    
print(f"El boleto premiado es {lista}{lista2}")

print("----------------------------------------------------------")


#Hacemos una funcion para extraer los elementos comunes de las dos listas

def numeros_comunes(lista_1,lista_2):
    conjunto1=set(lista_1)       
    conjunto2=set(lista_2)
    return list(conjunto1 &  conjunto2)


resultado=numeros_comunes(Num_bol,lista)
resultado2=numeros_comunes(Num_est,lista2)
print(f"Los numeros que tienen en comun son {resultado}{resultado2}")
numeros_comun= len(resultado)   #Le damos valor a cuantos numeros han tenido en comun
estrellas_comun= len(resultado2)
print(f"Tiene {numeros_comun} números y {estrellas_comun} estrellas en común.")

#Implementamos los precios ganados

if numeros_comun==5 and estrellas_comun==2:
    print("¡Ha ganado 15000000€!")
    
if numeros_comun==5 and estrellas_comun==1:
    print("¡Ha ganado 3000000€!")
    
if numeros_comun==5 and estrellas_comun==0:
    print("¡Ha ganado 1500000€!")
    
if numeros_comun==4 and estrellas_comun==2:
    print("¡Ha ganado 800000€!")
    
if numeros_comun==4 and estrellas_comun==1:
    print("¡Ha ganado 500000€!")
    
if numeros_comun==4 and estrellas_comun==0:
    print("¡Ha ganado 350000€!")
    
if numeros_comun==3 and estrellas_comun==2:
    print("¡Ha ganado 320000€!")
    
if numeros_comun==3 and estrellas_comun==1:
    print("¡Ha ganado 300000€!")
    
if numeros_comun==3 and estrellas_comun==0:
    print("¡Ha ganado 150000€!")
    
if numeros_comun==2 and estrellas_comun==2:
    print("¡Ha ganado 50000€!")
    
if numeros_comun==2 and estrellas_comun==1:
    print("¡Ha ganado 10000€!")
    
if numeros_comun==2 and estrellas_comun==0:
    print("¡Ha ganado 60€!")
    
if numeros_comun==1 and estrellas_comun==2:
    print("Ha ganado 0€")
    
if numeros_comun==1 and estrellas_comun==1:
    print("Ha ganado 0€")
    
if numeros_comun==1 and estrellas_comun==0:
    print("Ha ganado 0€")
    
if numeros_comun==0 and estrellas_comun==2:
    print("Ha ganado 0€")
    
if numeros_comun==0 and estrellas_comun==1:
    print("Ha ganado 0€")
    
if numeros_comun==0 and estrellas_comun==0:
    print("Ha ganado 0€")
    



    



    
    
    


            

