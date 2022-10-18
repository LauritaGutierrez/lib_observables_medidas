# Hago uso de funciones para solucionar las operaciones solicitadas con numeros complejos

import math

def sum_complejos(a,b,c,d):
    num_real = a+c
    num_imaginario = b+d
    return (num_real, num_imaginario)

def rest_complejos (a,b,c,d):
    num_real = a - c
    num_imaginario = b - d
    return (num_real, num_imaginario)

def multiplicar(numero1, numero2):
    a = numero1[0] * numero2[0]
    b = numero1[0] * numero2[1]
    c = numero1[1] * numero2[0]
    d = numero1[1] * numero2[1]
    e = b + c
    f = a + d * -1
    return f, e


def conjugado(numero1):
    return numero1[0], numero1[1] * -1


def modulo(numero1):
    return (numero1[0] ** 2 + numero1[1] ** 2) ** 0.5


def dividir(numero1, numero2):
    numero3 = []
    numero3 = [numero2[0], numero2[1] * -1]
    a = numero1[0] * numero3[0]
    b = numero1[0] * numero3[1]
    c = numero1[1] * numero3[0]
    d = numero1[1] * numero3[1]
    e = b + c
    f = a + d * -1
    g = numero2[0] * numero3[0]
    h = numero2[0] * numero3[1]
    i = numero2[1] * numero3[0]
    j = numero2[1] * numero3[1]
    k = h + i
    l = g + j * -1
    resultado = (f / l, e / l)
    return resultado


def polar_cartesiano(numero1):
    r = numero1[0]
    angulo = numero1[1] * (math.pi / 180)
    x = r * math.cos(angulo)
    y = r * math.sin(angulo)
    return x, y


def cartesiano_polar(numero1):
    r = ((numero1[0] ** 2) + (numero1[1] ** 2)) ** 0.5
    angulo = math.atan2(numero1[1], numero1[0])
    return r, (angulo * (180 / math.pi))


def fase(numero1):
    fase = math.atan2(numero1[1], numero1[0])
    return fase


def suma_vector(vector1, vector2):
    vectorfinal = []
    if len(vector1) == len(vector2):
        for i in range(len(vector1)):
            vectorfinal.append(sum_complejos(vector1[i], vector2[i]))
    return vectorfinal


def inversovector(vector1):
    vectorfinal = []
    for i in range(len(vector1)):
        vectorfinal.append(conjugado(vector1[i]))
    return vectorfinal


def producto_vectores(vector1, vector2):
    resultado = (0, 0)
    for i in range(len(vector1)):
        resultado = sum_complejos(resultado, multiplicar(vector1[i], vector2[i]))
    return resultado


def producto_vectoresReales(vector1, vector2):
    resultado = 0
    for i in range(len(vector1)):
        resultado += vector1[i] * vector2[i]
    return resultado


def producto_interno(vector1, vector2):
    return producto_vectores((conjugada_vector(vector1)), vector2)


def escalar_vector(numero, vector1):
    operacion = []
    for i in vector1:
        resultado = multiplicar(numero, i)
        operacion.append(resultado)
    return operacion


def adicion_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2):
        print("La suma no esta definida")
    else:
        resultado = []
        for i in range(len(matriz1)):
            operacion = []
            for j in range(len(matriz2)):
                operacion.append(sum_complejos(matriz1[i][j], matriz2[i][j]))
            resultado.append(operacion)
        return resultado


def matriz_inversa(matriz1):
    resultado = []
    for i in range(len(matriz1)):
        resultado.append(inversovector(matriz1[i]))
    return resultado


def escalar_matriz(numero, matriz1):
    resultado = []
    for i in range(len(matriz1)):
        operacion = []
        for j in range(len(matriz1)):
            operacion.append(multiplicar(numero, matriz1[i][j]))
        resultado.append(operacion)
    return resultado


def transpuesta_matriz(matriz1):
    matriz = [0] * len(matriz1[0])
    for i in range(len(matriz1)):
        matriz[i] = [0] * len(matriz1)
        for j in range(len(matriz1[i])):
            matriz[i][j] = matriz1[j][i]
    return matriz


def transpuesta_vector(vector1):
    return vector1


def conjugada_matriz(matriz1):
    resultado = []
    for i in range(len(matriz1)):
        operacion = []
        for j in range(len(matriz1)):
            operacion.append(conjugado(matriz1[i][j]))
        resultado.append(operacion)
    return resultado


def conjugada_vector(vector1):
    resultado = []
    for i in vector1:
        resultado.append(conjugado(i))
    return resultado


def adjunta_matriz(matriz1):
    return transpuesta_matriz(conjugada_matriz(matriz1))


def adjunta_vector(vector1):
    return conjugada_vector(vector1)


def producto_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        operacion = []
        for j in range(len(matriz2[0])):
            save = (0, 0)
            for k in range(len(matriz2)):
                save = sum_complejos(multiplicar(matriz1[i][k], matriz2[k][j]), save)
            operacion.append(save)
        resultado.append(operacion)
    return resultado


def producto_matrices_reales(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            save = 0
            for k in range(len(matriz2)):
                multi = matriz1[i][k] * matriz2[k][j]
                save += multi
            fila.append(save)
        resultado.append(fila)
    return resultado


def norma(numero1):
    return (numero1[0] ** 2 + numero1[1] ** 2)


def norma_vector(vectorreal1):
    resultado = 0
    for i in vectorreal1:
        resultado = resultado + norma(i)
    return resultado


def distancia_vectores(vectorreal1, vectorreal2):
    resultado = ((vectorreal1[0] - vectorreal2[0]) ** 2 + (vectorreal1[1] - vectorreal2[1]) ** 2) ** 0.5
    return resultado


def matriz_unitaria(matriz1):
    resultado = producto_matrices(matriz1, adjunta_matriz(matriz1))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            posicion = resultado[i][j]
            if (i == j and (posicion[0] != 1 or posicion[1] != 0)):
                return False
            elif (i != j and (posicion[0] != 0 or posicion[1] != 0)):
                return False
    return True


def matriz_hermitiana(matriz1):
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if (matriz1[i][j] != adjunta_matriz(matriz1)[i][j]):
                return False
    return True


def producto_tensor(vector1, vector2):
    operacion = []
    for i in vector1:
        numero = i
        for j in vector2:
            numero2 = j
            resultado = multiplicar(numero, numero2)
            operacion.append(resultado)
    return operacion


def producto_tensor_matrices(matriz1, matriz2):
    operacion = []
    for i in range(len(matriz1)):
        for j in range(len(matriz2)):
            operacion.append(producto_tensor(matriz1[i], matriz2[j]))
    return operacion


def vector_matriz(vector, matriz):
    ans = []
    for i in range(len(matriz)):
        ans.append(producto_vectores(vector, matriz[i]))
    return ans


def vector_matriz_real(vector, matriz):
    resultado = []
    for i in range(len(matriz)):
        resultado.append(producto_vectoresReales(vector, matriz[i]))
    return resultado

##Probabilidad de la posicion de un vector

def probabilidad(pos, vector):
    print(vector)
    a = norma(vector[pos])
    b = norma_vector(vector)
    prob = (a / b)
    respuesta = prob * 100
    return respuesta

def accion_vec_matr(m,v):
    i = len(m)
    a = [(0,0)] * i
    for j in range(i):
        for k in range(i):
            a[j] = sum_complejos(a[j],producto_vectores(m[j][k],v[k]))
    return a


def amplitud_transicion(matriz, vector):
    a = vector_matriz(vector, matriz)
    conjugado = inversovector(a)
    respuesta = producto_vectores(conjugado, vector)
    return respuesta