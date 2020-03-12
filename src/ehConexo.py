#-*- coding: utf-8 -*-

def ehConexo(qtdeV, MATRIZ):
    for i in range(0, qtdeV):
        linha = []
        for j in range(0, qtdeV):
            linha.append(MATRIZ[i][j])

        if j == (qtdeV-1):
            if sum(linha) >= 1:
                linha.clear()
            else:
                linha.clear()
                print("O grafo não é conexo.")
                return 0

        return print("O grafo é conexo.")
