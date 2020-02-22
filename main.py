#-*- coding: utf-8 -*-
#!/usr/bin/env python3

def printarAdjMATRIZ(qtdeV, MATRIZ):
    for i in range(qtdeV):
        for j in range(qtdeV):
            print(MATRIZ[i][j], end= ' ')
        print()


def main():
    print("=== Atividade de Implementação ==="
          +"\nAluno: João Vítor Silva Ferreira"
          +"\nTurma: N01")

    opcao = int(input("=== Opções ==="
          +"\n1-Cadastrar Grafo"
          +"\n2-Principais Grafos de Coloração (Extra)"
          +"\n: "))

    if opcao == 1:
        # pegar quantidade de vértices
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
        printarAdjMATRIZ(qtdeVertices, adjMATRIZ)

    elif opcao == 2:
        import extras
        extras.coloracaoExemplos()

    else:
        print("Opção não encontrada.")


if __name__ == "__main__":
    main()
