# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:49:58 2021

@author: DiegoMartínLópez
"""

import math

print("CALCULADORA")
print("-----------------------------------------")
print("\t1.- Funciones                      --")
print("\t2.- Suma de dos números            --")
print("\t3.- Resta de dos números           --")
print("\t4.- Multiplicación de dos números  --")
print("\t5.- División de dos números        --")
print("\t6.- Cociente                       --")
print("\t7.- Resto                          --")
print("\t8.- Exponenciación de dos números  --")
print("\t9.- Area Triángulo                 --")
print("\t10.- Area Rectángulo                --")
print("\t11.- Area Círculo                  --")
print("\t12.- Area Cuadrado                 --")
print("\t13.- Salir                         --")
#print("\t9.- ")
print("-----------------------------------------")
opc = int(input("Introduzca una opción: "))
while(opc<1 or opc>13):
    print("Debe ser una opción disponible!")
    opc = int(input("Introduzca opción valida: "))


if(opc==1):
    def sumarPidiendo():
        Numero1=int(input("Introduce un número: "))    
        Numero2=int(input("Introduce un número: "))    
        print(f"{Numero1}+{Numero2}={Numero1+Numero2}")
        return(Numero1+Numero2)
    
    def restarPidiendo():
        Numero1=int(input("Introduce un número: "))    
        Numero2=int(input("Introduce un número: "))    
        print(f"{Numero1}-{Numero2}={Numero1-Numero2}")
        return(Numero1-Numero2)
    
    def multiplicarPidiendo():
        Numero1=int(input("Introduce un número: "))    
        Numero2=int(input("Introduce un número: "))    
        print(f"{Numero1}*{Numero2}={Numero1*Numero2}")
        return(Numero1*Numero2)
    
    def dividirPidiendo():
        Numero1=int(input("Introduce un número: "))    
        Numero2=int(input("Introduce un número: "))    
        print(f"{Numero1}/{Numero2}={Numero1/Numero2}")
        return(Numero1/Numero2)
    
    def cocientePidiendo():
        Numero1=int(input("Introduce un número: "))    
        Numero2=int(input("Introduce un número: "))    
        print(f"El cociente de la division {Numero1}/{Numero2}={Numero1//Numero2}")
        return(Numero1//Numero2)
    
    def restoPidiendo():
        Numero1=int(input("Introduce un número: "))    
        Numero2=int(input("Introduce un número: "))    
        print(f"El resto de la división {Numero1}+{Numero2}={Numero1%Numero2}")
        return(Numero1%Numero2)
    
    def exponentePidiendo():
        Numero1=int(input("Introduce un número: "))    
        Numero2=int(input("Introduce un número: "))    
        print(f"El exponente del numero {Numero1}^{Numero2}={Numero1**Numero2}")
        return(Numero1**Numero2)
    5
    def areaTrianguloPidiendo():
        Numero1=int(input("Introduzca la base del triangulo: "))
        Numero2=int(input("Introduzca la altura del triangulo: "))
        areaTriangulo=x*y/2
        print(f"El área del triángulo de base {Numero1} y altura {Numero2} es {areaTriangulo} metros cuadrados")
        return(areaTriangulo)
    
    def areaRectanguloPidiendo():
        Numero1=int(input("Introduzca la base del rectangulo: "))
        Numero2=int(input("Introduzca la altura del rectangulo: "))
        areaRectangulo=x*y
        print(f"El área del rectangulo de lado {Numero1} y lado {Numero2} es {areaRectangulo} metros cuadrados")
        return(areaRectangulo)
    
    def areaCirculoPidiendo():
        import math
        Numero1=int(input("Introduzca el radio del círculo: "))
        areaCirculo=math.pi*Numero1**2
        print(f"El área del circulo de radio {Numero1} es {areaCirculo} metros cuadrados")
        return(areaCirculo)
    
    def areaCuadradoPidiendo():
        Numero1=int(input("Introduzca el lado del cuadrado: "))
        areaCuadrado=Numero1**2
        print(f"El área del cuadrado de lado {Numero1} es {areaCuadrado} metros cuadrados")
        return(areaCuadrado)
    

if(opc==2):
    lamSuma = lambda x, y: x+y
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"El resultado de la suma {x}+{y} es {lamSuma(x,y)}")
elif(opc==3):
    lamResta = lambda x, y: x-y
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{lamResta(x,y)}")
elif(opc==4):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}*{y}={x*y}")
elif(opc==5):
    print("No se podrá dividir entre 0")
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}/{y}={x/y}")
elif(opc==6):
    print("No se podrá dividir entre 0")
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"El cociente de la división {x}/{y}={x//y}")
elif(opc==7):
    print("No se podrá dividir entre 0")
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"El resto de la división {x}/{y}={x%y}")
elif(opc==8):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}^{y}={x**y}")
if(opc==9):
    x=int(input("Introduzca la base del triangulo: "))
    y=int(input("Introduzca la altura del triangulo: "))
    areaTriangulo=x*y/2
    print(f"El área del triángulo de base {x} y altura {y} es {areaTriangulo} metros cuadrados")
if(opc==10):
    x=int(input("Introduzca la base del rectangulo: "))
    y=int(input("Introduzca la altura del rectangulo: "))
    areaRectangulo=x*y
    print(f"El área del rectangulo de lado {x} y lado {y} es {areaRectangulo} metros cuadrados")
if(opc==11):

    x=int(input("Introduzca el radio del círculo: "))
    areaCirculo=math.pi*x**2
    print(f"El área del circulo de radio {x} es {areaCirculo} metros cuadrados")
    
    
    
    


 