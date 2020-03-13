#-*- coding: utf-8 -*-

def printAMATRIZ(qtde_v, MATRIZ):
    """ Printar a Matriz de Adjacência """

    for i in range(qtde_v):
        for j in range(qtde_v):
            print(MATRIZ[i][j], end= ' ')
        print()
