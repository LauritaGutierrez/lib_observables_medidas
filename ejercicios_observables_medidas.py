import numpy as np
import calculator_complex_numbers as cn

#SIMULANDO SISTEMACUÁNTICO SECCIÓN 4.1

#1.Sistema calcula la probabilidad de encontrar en una posición en particular.
def posicion_probabi(numPosiciones,vector):
    tamano = len(vector)
    con = 0
    for j in range(tamano):
        con = con + (cn.modulo(vector[j]))**2
    con = con**(1/2)
    final_pro = (cn.modulo(vector[numPosiciones])**2)/con**2
    return final_pro

#2.Sistema si se le da otro vector Ket busca la probabilidad de transitar del primer vector al segundo.

def transitar_vect(vect,w):
    t_vec = len(vect)
    finl = [(0, 0)] * t_vec
    for j in range(t_vec):
        finl[j] = cn.conjugada_vector(w[j])
    ampl_fin = (0, 0)
    for i in range(t_vec):
        ampl_fin = cn.sum_complejos(ampl_fin, cn.multiplicar(vect[i],finl[i]))
    return ampl_fin

#Retos de programación del capítulo

#N3
def valores_propios(matriz,posicion):
    tamano =len(matriz)
    psi_c = [(0,0)] * tamano
    m = [[(0,0) for i in range(tamano)] for i in range(tamano)]
    z = [[(0,0) for i in range(tamano)] for i in range(tamano)]

    for i in range(tamano):
        psi_c[i] = cn.conjugada_vector(posicion[i])
    for i in range(tamano):
        psi_c[i] = cn.conjugada_vector(posicion[i])
    for i in range (tamano):
        for j in range(tamano):
            m[i][j] = cn.conjugada_matriz(matriz[i][j])
    mat = np.array(m)
    valores_propios,vectores_propios = np.linalg.eig(mat)#calcular los valores propios y los vectores propios rectos de una matriz cuadrada
    for i in range(tamano):
        for j in range(tamano):
            z[j][i] = (psi_c[i]*vectores_propios[i])
    for i in range(tamano):
        print((cn.norma_vector(z[i])**2))
    return vectores_propios

#N4
def estado_final(mat,vector,clik):
    for i in range(clik):
        vector = cn.accion_vec_matr(mat,vector)
    return vector