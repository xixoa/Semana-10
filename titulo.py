# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:55:42 2022

@author: Sebastian
"""

#Problema: Necesitamos mostrar los nombres de una cadena
#presentando las primeras letras en mayuscula
# en word se conoce como formato Titulo

#Importar la libreria

import camelcase

nombre="sebastian timo laura antezana"

print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamdo cam
cam=camelcase.CamelCase()
print("Con camelcase...")

#Imprimimos el nombre en formato titulo
#Utilizamos camelcase

print(cam.hump(nombre))

#Para resolver el problema 
#Creamos otro objeto llamado cam2
#Al definir el objeto, incluimos los argumentos
#'sebastian' y 'laura'

cam2=camelcase.CamelCase('sebastian','laura')
print(cam2.hump(nombre))