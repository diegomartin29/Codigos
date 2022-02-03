# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 08:52:37 2021

@author: DiegoMartínLópez
"""

import functools

def esPar(x):
    return x%2==0


def suma(x,y):
    return x+y


listanumeros=list(range(1,41))
listaNumerosPar=list(filter(esPar,listanumeros))
print (listaNumerosPar)

resultado=functools.reduce(suma, listaNumerosPar)
print(resultado)

#--------------------------------------------------------------------------

def suma(x,y):
    return x+y
tupla=(1, 2, 3, 4, 5, 6, 7, 8, 9, 100)
listaNumeros=list(range(1,11))
print(listaNumeros)
resultado=functools.reduce(suma, tupla)

print(resultado)

#------------------------------------------------------------------

resultado=functools.reduce(suma,filter(esPar,range(1,41)))

