# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:31:36 2021

@author: DiegoMartínLópez
"""


def añoBisiesto(año): # Definimos la función

    
        
        if año %4 !=0: # No es divisible entre 4
            print(f"El año {año} no es bisiesto")
        
        elif año %4 ==0 and año %100 != 0: # Es divisible entre 4 pero no entre 100
            print(f"El año {año} no es bisiesto")
            
        elif año%4 ==0 and año %100 ==0 and año %400 !=0: # Es divisible entre 4 y 100 pero no entre 400
                print(f"El año {año} no es bisiesto")
        
        elif año%4 ==0 and año %100 ==0 and año %400 ==0: # Es divisible entre 4, 100 y 400
            print(f"El año {año} es bisiesto")
        
año=2000 # Año
añoBisiesto(año)
print(list(filter(añoBisiesto, range(2000, 2101))))
