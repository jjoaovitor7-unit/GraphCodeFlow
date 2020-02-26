#-*- coding: utf-8 -*-

def ehCompleto(qtdeV, MATRIZ):
    ehCompletoVerif = []
    for i in range(qtdeV):
        for j in range(qtdeV):
            ehCompletoVerif.append(MATRIZ[i][j])

    if sum(ehCompletoVerif) == (qtdeV ** 2):
        print("O grafo é completo.")

    elif sum(ehCompletoVerif) != (qtdeV ** 2):
        print("O grafo não é completo.")

    else:
        return 0
