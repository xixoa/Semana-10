# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:23:26 2022

@author: Sebastian
"""

import sqlite3

#Con el comando connect buscara la base de datos
#que tenga ese nombre, de lo contrario lo creará

conexion=sqlite3.connect("bdbiblioteca.db")
conexion.close()