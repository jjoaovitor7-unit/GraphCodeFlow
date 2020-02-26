#-*- coding: utf-8 -*-

def ehRegular(qtdeV, MATRIZ):
    ehRegularVerifAux = []
    ehRegularVerif = []

    # grau dos vértices
    for i in range(qtdeV):
        for j in range(qtdeV):
            ehRegularVerifAux.append(MATRIZ[i][j])
            if j == (qtdeV-1):
                ehRegularVerif.append(sum(ehRegularVerifAux))
                ehRegularVerifAux.clear()

    print("Aux>", ehRegularVerifAux)
    print("Grau dos Vértices>", ehRegularVerif)

    ehRegularVerifMax = max(ehRegularVerif)
    x = 1
    v = 1 # verifRegular
    for x in range(len(ehRegularVerif)):
        if v == 0:
            print("O grafo não é regular.")
            return 0

        if ehRegularVerif[x] == ehRegularVerif[x-1]:
            v = 1
        else:
            v = 0

        if x == (len(ehRegularVerif)-1) and v == 1:
            print("O grafo é regular.")
