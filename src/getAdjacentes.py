#-*- coding: utf-8 -*-

def getAdjacentes(qtdeV, MATRIZ):
    aMATRIZ = []
    for i in range(qtdeV):
        linha = []
        for j in range(qtdeV):
            if MATRIZ[i][j] == 1:
                linha.append("v" + str(j))
        aMATRIZ.append(linha)

    y = 0
    for i in aMATRIZ:
        print("v" + str(y) + ": ", i)
        y+=1
