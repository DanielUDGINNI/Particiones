# Particiones
#Daniel Alberto Vazquez Ramirez
#Seminario de Solucion de Problemas de Sistemas Basados en Conocimientos

Realizar un programa que permita generar un conjunto de particiones de entrenamiento considerando un dataset. El programa debe permitir seleccionar la cantidad de particiones y el porcentaje de patrones de entrenamiento y prueba.

El programa de este repositorio funciona a traves del archivo main.py el cual carga archivo excel csv utilizando la libreria de pandas, y asignando los valores a traves de la funcion iloc a vectores. Este programa consta de 5 funciones para particionar el dataset encontrado en el mismo repositorio. 
La primera particion funciona para obtener segmento de entrenamiento, validacion y prueba. def evp():
Se modifican las variables llamadas ntrain, ntest y nvalidation por valores en los que al sumarse den como resultado 100. Esto para poder obtener porcentajes alrededor del 100.
La longitud del dataset se divide entre 100 y segun el numero de las variables modificadas se multiplica por el resultado obtenido.
Los ciclos funcionan para agregar las filas a una matriz y se detienen hasta llegar a la longitud de valores que representan el porcentaje modificado en las variables. Esto se hace 3 veces para poder obtener los 3 diferentes tamaños de arreglos. El segundo y tercer ciclo inician a partir del numero anterior utilizado, para continuar con el indice perteneciente.

La particion definida por entrenamiento y prueba def ep(): se define por dos variables, la unica editable es la llamada ntrain para ingresar el porcentaje destinado al entrenamiento. El porcentaje restante lo calcula el programa y se le otorga a prueba. El funcionamiento de agregar a la matriz cada fila de datos se basa en el concepto de la particion anterior, segun el tamaño calculado realizara iteraciones pertinentes. El inicio y final se define por las variables de ntrain y ntest. Las particiones que dividen por segmentos de prueba y entrenamiento contienen funcion para graficar los datos. Se pueden modificar con la variable del segundo corchete para elegir la columna de la matriz.

La particion definida como def crook(): sirve para particionar el dataset en partes iguales. La variable declarada dentro de la funcion como partes se puede modificar por el usuario. La funcion divide la longitud en las n partes definida por el usuario. EL ciclo for añade filas a una matriz hasta que el ciclo while termine su ejecucion. Se obtiene un arreglo llamado ultimos, donde se guarda el que indice de la matriz se divide cada parte. 

La particion definida como def grupo(): divide el dataset segun el valor obtenido en la columna y1 que pueden ser los valores -1 o 1. Se añaden las filas a diferentes matrices. 

La particion definida como def rango(): se basa en los datos de la columna X1, las cuales estan entre 4 y 8. En este caso se hacen 4 matrices dado que existen 4 rangos distintos. Dentro del ciclo se utilizan estructuras condicionales como IF, para saber en que matriz añadir la fila correspondiente al indice.

En la ultima linea de codigo se escribe la funcion deseada a ejecutar.


