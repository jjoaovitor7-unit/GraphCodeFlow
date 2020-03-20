#-*- coding: utf-8 -*-

def ehCompleto(qtde_v, MATRIZ):
    """Método ehCompleto p/ verificar se o Grafo é completo"""

    ehCompleto_ = []
    for i in range(qtde_v):
        for j in range(qtde_v):
            ehCompleto_.append(MATRIZ[i][j])

    if sum(ehCompleto_) == (qtde_v ** 2) or sum(ehCompleto_) == ((qtde_v ** 2) - qtde):
            print("O grafo é completo.")
            return 1

    else:
        print("O grafo não é completo.")
        return 0
