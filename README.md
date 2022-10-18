# TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS

Esta libreria se compone de operaciones con numeros complejos de matrices y vectores haciendo uso
del capitulo 4 y algunos ejercicios propuestos para poder comprender del todo la teoría.

## Para comenzar

Antes de comenzar, se necesita conocimientos previos, operaciones entre matrices y vectores de numeros complejos, 
probabilidad de un estado vectores, medicion...

## Requisitos

- Esta libreria, TEORÍA CUÁNTICA BÁSICA, OBSERVABLES Y MEDIDAS, se puede ejecutar en visual code de Python, en IDLE y en PyCharm, programas necesarios para
la prueba.

- Ordenador adecuado para lograr ejecutar un lenguaje de programacion.

### Partes

SIMULE EL PRIMER  SISTEMACUÁNTICO DESCRITO EN LA SECCIÓN 4.1

El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador permite especificar el número de posiciones
y un vector ket de estado asignando las amplitudes.

1. El sistema calcula la probabilidad de encontrarlo en una posición en particular.

2. El sistema si se le da otro vector Ket busca la probabilidad de transitar del primer vector al segundo.

COMPLETANDO LOS RETOS DE PROGRAMACIÓN DEL CAPÍTULO 4

1. Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación

2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.

3. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.

4. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.

EJERCICIOS PROPUESTOS
```
4.3.1
4.3.2
4.4.1
4.4.2
```
### Explicación ejercicios propuestos

### 4.3.1
```
Se debe encontrar todos los posibles estados a los que puede pasar el sistema descrito en el ejercicio 4.2.2 
después de realizar una medición ¿Cuál es la probabilidad de que un estado inicial normalizado |ψ⟩
transite a un eigenvector específico, digamos, |e⟩?
Sabiendo que la probabilidad de la transición al eigenvector
viene dada por el cuadrado del producto interior de los dos estados: |⟨e|ψ⟩|2
```
### 4.3.2
```
Haller la distribución de probabilidad de los valores propios como en el 4.3.1 anterior.
```
### 4.4.1
```
Se tiene que verificar si ambas son unitarias y si su producto da una matriz unitaria
                U1=[0,1],     U2= [sqrt2/2,sqrt2/2],
                   [1,0]          [sqrt2/2,sqrt2/2]
```

### 4.4.2
```
En este caso pide simular el mismo problema de las canicas, pero haciendo el cambio
con una bola de billar, determinando el estado del sistema, con el mismo estado inicial que seria:

              entrada = [[(0,0),(1/(2**(1/2)),0),(1/(2**(1/2)),0),(0,0)],
                         [(1/(2**(1/2)),0),(0,0),(0,0),(1/(2**(1/2)),0)],
                         [(1/(2**(1/2)),0),(0,0),(0,0),(1/(2**(1/2)),0)],
                         [(0,0),(1/(2**(1/2)),0),(-1/(2**(1/2)),0),(0,0)]]
              vector_res = [(1,0),(0,0),(0,0),(0,0)]
```

## Construido con

* Realizado con [Pycharm] (https://www.jetbrains.com/pycharm/) The Python IDE for Professional Developers.

## Autor
* **Laura Valentina Gutiérrez Rico**

* **Ciencias Naturales Y Tecnología**

