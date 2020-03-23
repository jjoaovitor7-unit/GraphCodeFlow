#-*- coding: utf-8 -*-

def ehConexo(qtde_v, MATRIZ):
    """Método ehConexo p/ verificar se o Grafo é conexo"""

    for i in range(0, qtde_v):
        linha = []
        for j in range(0, qtde_v):
            linha.append(MATRIZ[i][j])

        if j == (qtde_v-1):
            if sum(linha) >= 1:
                linha.clear()
            else:
                linha.clear()
                print("O grafo não é conexo.")
                return 0

        return print("O grafo é conexo.")
