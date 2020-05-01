#-*- coding: utf-8 -*-

def BFS(qtde_v, MATRIZ, v):
    fila = []
    visi = []

    visi.append(v)
    fila.append(v)

    while len(fila) != 0:
        u = fila[0]
        fila.pop()
        print("fila>", fila)
        for j in range(qtde_v):
            if MATRIZ[v][j] == 1 and j not in visi:
                visi.append(j)
                fila.append(j)
        v+=1
        print("fila>", fila)
        print("visi>", visi)
