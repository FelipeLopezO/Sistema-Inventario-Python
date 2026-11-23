# Sistema-Inventario-Python
Entrega final Fundamentos de programacion
Universidad Nacional Abierta y a Distancia (UNAD)

1. Descripcion del proyecto
A partir de la problematica numero 4 propuesta por el docente, se desarrollo una aplicacion
en python donde se usa una matriz para almacenar la informacion de los articulos y permite
identificar aquellos productos que necesitan reabastecimiento, hacer el calculo de las 
cantidades necesarias, como funciones adicionales añadidas por autoria propia, hay una
seleccion individual de los articulos, su revision especifica del estado de cantidades y
actualizar las existencias del inventario.

2. Objetivo General
Desarrrolar una herramienta que permita gestionar un inventario mediante el uso de matrices,
funciones, estructuras condicionales y ciclos, facilitando el control de existencias y el
calculo de cantidades necesarias para el reabastecimiento.

3.Funcionalidades principales
El sistema cuenta con las siguentes funcionalidades:
- Consulta individual de articulos: Por medio del codigo de producto es posuble cosultar su informacion
- Consulta del estado del inventario: Muestra el stock actual y el stock minimo requerido de cada articulo
- Actualizacion de existencias: Permite modificar la cantidad disponible de un artiulo e informa el stock anterior 
- Calculo de reabastecimiento: Determina automaticamente cuantas unidades deben solicitarse para alcanzar el stock minimo requerido.
- Reporte general: Presenta informacion de todos los articulos y un resumen de las existencias.
- Identificacion de articulos criticos: Muestra los productops cuyo stock actual se encuentra por debajo se encuentra por debajo del minimo requerido

4. Estructura de la matriz
El inventario se encuentra organizado mediante una matriz que contiene cuatro campos por articulo
Campos: Codigo del articulo, Nombre del articulo, Stock actual, Stock minimo.

5. Lenguaje
Este trabajo fue programado en Python 3