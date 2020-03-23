#-*- coding: utf-8 -*-

def getAdjacentes(qtde_v, MATRIZ):
    """Método getAdjacentes p/ pegar os adjacentes do Grafo"""

    aMATRIZ = []
    for i in range(qtde_v):
        linha = []
        for j in range(qtde_v):
            if MATRIZ[i][j] == 1:
                linha.append("v" + str(j))
        aMATRIZ.append(linha)

    y = 0
    for i in aMATRIZ:
        print("v" + str(y) + ": ", i)
        y+=1
