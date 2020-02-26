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
          +"\nTurma: N01\n")

    while True:
        opcao = int(input("=== Opções ==="
              +"\n1-Cadastrar Grafo"
              +"\n2-Principais Grafos de Coloração (Extra)"
              +"\n3-Printar Grafo"
              +"\n4-Adjacentes (getAdjacentes)"
              +"\n5-Verificar se o Grafo é completo (ehCompleto)"
              +"\n6-Remover Aresta"
              +"\n7-Adicionar Aresta"
              +"\n8-Verificar se o Grafo é regular (ehRegular)"
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
            import src.extras
            src.extras.coloracaoExemplos()

        elif opcao == 3:
            try:
                printarAdjMATRIZ(qtdeVertices, adjMATRIZ)
            except UnboundLocalError:
                print("É necessário cadastrar o Grafo primeiro.")

        elif opcao == 4:
            try:
                import src.getAdjacentes
                src.getAdjacentes.getAdjacentes(qtdeVertices, adjMATRIZ)
            except UnboundLocalError:
                print("É necessário cadastrar o Grafo primeiro.")

        elif opcao == 5:
            try:
                import src.ehCompleto
                src.ehCompleto.ehCompleto(qtdeVertices, adjMATRIZ)
            except UnboundLocalError:
                print("É necessário cadastrar o Grafo primeiro.")

        elif opcao == 6:
            a1, a2 = input("Aresta(xx xx): ").split()
            a1 = int(a1)
            a2 = int(a2)
            adjMATRIZ[a1][a2] = 0

        elif opcao == 7:
            a1, a2 = input("Aresta(xx xx): ").split()
            a1 = int(a1)
            a2 = int(a2)
            adjMATRIZ[a1][a2] = 1

        elif opcao == 8:
            try:
                import src.ehRegular
                src.ehRegular.ehRegular(qtdeVertices, adjMATRIZ)
            except UnboundLocalError:
                print("É necessário cadastrar o Grafo primeiro.")
    
        elif opcao == 99:
            return 0

        else:
            print("Opção não encontrada.")


if __name__ == "__main__":
    main()
