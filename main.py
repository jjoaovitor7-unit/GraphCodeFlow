#-*- coding: utf-8 -*-
#!/usr/bin/env python3

def printarAdjMATRIZ(qtdeV, MATRIZ):
    for i in range(qtdeV):
        for j in range(qtdeV):
            print(MATRIZ[i][j], end= ' ')
        print()


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

def main():
    print("=== Atividade de Implementação ==="
          +"\nAluno: João Vítor Silva Ferreira"
          +"\nTurma: N01\n")

    while True:
        opcao = int(input("=== Opções ==="
              +"\n1-Cadastrar Grafo"
              +"\n2-Principais Grafos de Coloração (Extra)"
              +"\n3-Printar Grafo"
              +"\n4-Verificar se o Grafo é completo (ehCompleto)"
              +"\n5-Remover Aresta"
              +"\n6-Adicionar Aresta"
              +"\n7-Verificar se o Grafo é regular (ehRegular)"
              +"\n99-Parar o Programa"
              +"\n: "))

        if opcao == 1:
            qtdeVertices = int(input("Quantidade de Vértices> "))

            if qtdeVertices <= 0:
                return 0

            adjMATRIZ = []
            for i in range(qtdeVertices):
                linha = []
                for j in range(qtdeVertices):
                    adjEntrada = int(input("Adjacência (v" + str(i) + "v" + str(j) + ")(0>não|1>sim):"))
                    if adjEntrada == 0:
                        linha.append(0)
                    elif adjEntrada == 1:
                        linha.append(1)
                    else:
                        print("Apenas é aceito 0 ou 1!")
                adjMATRIZ.append(linha)
            print("Grafo cadastrado!")

        elif opcao == 2:
            import extras
            extras.coloracaoExemplos()

        elif opcao == 3:
            try:
                printarAdjMATRIZ(qtdeVertices, adjMATRIZ)
            except UnboundLocalError:
                print("É necessário cadastrar o Grafo primeiro.")

        elif opcao == 4:
            try:
                ehCompleto(qtdeVertices, adjMATRIZ)
            except UnboundLocalError:
                print("É necessário cadastrar o Grafo primeiro.")

        elif opcao == 5:
            a1, a2 = input("Aresta(xx xx): ").split()
            a1 = int(a1)
            a2 = int(a2)
            adjMATRIZ[a1][a2] = 0

        elif opcao == 6:
            a1, a2 = input("Aresta(xx xx): ").split()
            a1 = int(a1)
            a2 = int(a2)
            adjMATRIZ[a1][a2] = 1

        elif opcao == 7:
            ehRegular(qtdeVertices, adjMATRIZ)

        elif opcao == 99:
            return 0

        else:
            print("Opção não encontrada.")


if __name__ == "__main__":
    main()
