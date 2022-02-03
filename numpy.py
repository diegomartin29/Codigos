# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 09:03:55 2022

@author: DiegoMartínLópez
"""


import pandas as pd
import numpy as np


userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_table('d:/usuarios/Users/DiegoMartínLópez/Documents/Programacion/Base de datos movies Programacion/ml-1m/users.dat', engine='python', sep='::',
header=None, names=userHeader)
movieHeader = ['movie_id', 'title', 'genders']
movies = pd.read_table('d:/usuarios/Users/DiegoMartínLópez/Documents/Programacion/Base de datos movies Programacion/ml-1m/movies.dat', engine='python', sep='::'
, header=None, names=movieHeader, encoding="latin1")
ratingHeader = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('d:/usuarios/Users/DiegoMartínLópez/Documents/Programacion/Base de datos movies Programacion/ml-1m/ratings.dat', engine='python', sep='::', header=None, names=ratingHeader)
# Merge data




