# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 09:25:52 2021

@author: DiegoMartínLópez
"""

def media(a,b):
  impar = imp = 0
  for num in range(a,b):
    if num%2 == 0: 
      imp += num 
      impar += 1 
  acum = imp / impar 
  return acum
 
v1 = int(input('Valor inicial:'))
v2 = int(input('Valor final:'))
print(media(v1,v2))