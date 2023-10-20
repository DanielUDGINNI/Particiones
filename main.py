# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 16:31:02 2023

@author: DanielVazquez
"""

import numpy as np
import pandas as pd
import math as mt
import matplotlib.pyplot as plt

data = pd.read_csv("irisbin.csv", header = None)

df = pd.DataFrame(data)

x1 = df.iloc[:, 0]
x2 = df.iloc[:, 1]
x3 = df.iloc[:, 2]
x4 = df.iloc[:, 3]

y1 = df.iloc[:, 4]
y2 = df.iloc[:, 5]
y3 = df.iloc[:, 6]


n = len(x1)

#Particion entrenamiento, validacion y prueba
def evp():
    ntrain = 50
    ntest = 20
    nvalidation = 30
        
    matriz = []
    matriz2 = []
    matriz3 = []
    fila = [0,0,0,0,0,0]
    
    p = n/100
    #%
    ntrain = int(ntrain * p)
    ntest = int(ntest * p)
    nvalidation = int(nvalidation * p)
    
    #entrenamiento
    for i in range (ntrain):
        fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
        matriz.append(fila)
    
    for j in range (ntrain, ntest):
        fila = [x1[j],x2[j],x3[j],y1[j],y2[j],y3[j]]
        matriz2.append(fila)
        
    for k in range(nvalidation, nvalidation):
        fila = [x1[j],x2[j],x3[j],y1[j],y2[j],y3[j]]
        matriz3.append(fila)
        
    x = []
    y = []
    for m in range (ntrain):
        element = matriz[m][0]
        element2 = matriz[m][5]
        x.append(element)
        y.append(element2)
    
    plt.figure()
    plt.plot(x,y,'g')
    plt.grid()
    plt.show()


#Particion entrenamiento y prueba
def ep():
    ntrain = 80
    ntest = 100 - ntrain
    
    matriz = []
    matriz2 = []
    fila = [0,0,0,0,0,0]
    p = n/100
    
    ntrain = int(ntrain * p)
    ntest = int(ntest * p)
    
    for i in range (ntrain):
        fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
        matriz.append(fila)
    
    for j in range (ntrain, ntest):
        fila = [x1[j],x2[j],x3[j],y1[j],y2[j],y3[j]]
        matriz2.append(fila)
        
    x = []
    y = []
    for m in range (ntrain):
        element = matriz[m][0]
        element2 = matriz[m][5]
        x.append(element)
        y.append(element2)
    
    plt.figure()
    plt.plot(x,y,'g')
    plt.grid()
    plt.show()


#Validacion cruzada, k partes iguales
def crossK():
    partes = 5
    t = 1
    r = n/partes
    ultimos = []
    
    matriz = []
    fila = [0,0,0,0,0,0]
    while(t!=partes):
        for i in range(r):
            fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
            matriz.append(fila)
            
        ultimos.append(i)
        t = t + 1

#Basada en grupos
def grupo():
    #grupo en y1 en 1 y -1
    matriz = []
    matriz2 = []
    fila = [0,0,0,0,0,0]
    
    for i in range(n):
        if y1[i] == -1:
            fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
            matriz.append(fila)
        if y1[i] == 1:
            fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
            matriz2.append(fila)

#Basada en rangos
def rango():
    matriz = []
    matriz2 = []
    matriz3 = []
    matriz4 = []
    fila = [0,0,0,0,0,0]
    
    for i in range(n):
        if x1[i] >= 4 or x1[i] < 5 :
            fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
            matriz.append(fila)
        if x1[i] >= 5 or x1[i] < 6 :
            fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
            matriz2.append(fila)
        if x1[i] >= 6 or x1[i] < 7 :
            fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
            matriz3.append(fila)
        if x1[i] >= 7 or x1[i] < 8 :
            fila = [x1[i],x2[i],x3[i],y1[i],y2[i],y3[i]]
            matriz4.append(fila)
            
    x = []
    y = []
    for m in range (len(matriz)):
        element = matriz[m][2]
        element2 = matriz[m][5]
        x.append(element)
        y.append(element2)
    
    plt.figure()
    plt.plot(x,y,'g')
    plt.grid()
    plt.show()


#Funcion a utilizar
rango()
