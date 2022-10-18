import calculator_complex_numbers as cn

# Modelando en la libreria los ejercicios propuestos.
# 4.3.1
# 4.3.2
# 4.4.1
# 4.4.2

#-----------------------------------
#Punto 4.3.1
def probabilidades(posicion, index):
    e = [[(0,1),(1,0)],[(0,-1),(1,0)],[(1,0),(1,0)],[(-1,0),(1,0)],[(0,0),(1,0)],[(1,0),(0,0)]]##es el estado que ingresa
    result = []
    for i in range((index*2)-2,index*2):
        if cn.probabilidad(posicion,e[i])!= 0.0: ##uso de ecuacion de probabilidad y posicion
            result = result + e[i]
    return result

#-----------------------------------
#Punto 4.4.1
def unitario(vector,y):
    tamano = len(vector)
    entr = [[(0,0) for i in range (tamano)] for i in range (tamano)]
    if cn.matriz_unitaria(vector) and cn.matriz_unitaria(y) == False:
        print("Estas no son unitarias")
    else:##una vez sabiendo que es falso, se evalua si es unitario o no con el producto de matrices
        entr = cn.producto_matrices(cn.transpuesta_vector(vector),y)
        if cn.matriz_unitaria(entr):
            print("unitario")
        else:
            print("No unitario")
#-----------------------------------
#Punto 4.4.2
def experimento_billar(vector_e,bolas,n_clicks):
    for i in range(n_clicks):
        vector_e = cn.vector_matriz_real(vector_e,bolas)
    return vector_e