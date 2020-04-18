#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def main():
    import src.extras as extras
    extras.header()

    while True:
        extras.options()
        try:
            option = int(input(": "))
        except ValueError:
            return print("Só é aceito números.")

        if option == 1:
            qtde_v = int(input("Quantidade de Vértices> "))

            if qtde_v <= 0:
                print("A quantidade de vértices precisa ser maior do que 0.")
                return 0

            m_adj = []
            for i in range(qtde_v):
                linha = [] # vértice
                for j in range(qtde_v):
                    adj = int(input("Adjacência "
                                    +"(v" + str(i) + "v" + str(j) + ")"
                                    +"(0>não|1>sim):"))

                    if adj == 0:
                        linha.append(0)
                    elif adj == 1:
                        linha.append(1)
                    else:
                        return print("Apenas é aceito 0 ou 1!")

                m_adj.append(linha)
            print("Grafo cadastrado!")

        elif option == 2:
            try:
                import src.printAMATRIZ as pMAdj
                pMAdj.printAMATRIZ(qtde_v, m_adj)
            except UnboundLocalError:
                extras.GrafoNotFoundError()

        elif option == 3:
            try:
                a1, a2 = input("Aresta(xx xx): ").split()
                a1 = int(a1)
                a2 = int(a2)
                m_adj[a1][a2] = 1
            except UnboundLocalError:
                extras.GrafoNotFoundError()

        elif option == 4:
            try:
                a1, a2 = input("Aresta(xx xx): ").split()
                a1 = int(a1)
                a2 = int(a2)
                m_adj[a1][a2] = 0
            except UnboundLocalError:
                extras.GrafoNotFoundError()

        elif option == 5:
            try:
                import src.getAdjacentes
                src.getAdjacentes.getAdjacentes(qtde_v, m_adj)
            except UnboundLocalError:
                extras.GrafoNotFoundError()

        elif option == 6:
            try:
                import src.ehCompleto
                src.ehCompleto.ehCompleto(qtde_v, m_adj)
            except UnboundLocalError:
                extras.GrafoNotFoundError()

        elif option == 7:
            try:
                import src.ehRegular
                src.ehRegular.ehRegular(qtde_v, m_adj)
            except UnboundLocalError:
                extras.GrafoNotFoundError()

        elif option == 8:
            import src.extras
            src.extras.exColoracao()

        elif option == 9:
            try:
                import src.ehConexo
                src.ehConexo.ehConexo(qtde_v, m_adj)
            except UnboundLocalError:
                extras.GrafoNotFoundError()
        elif option == 99:
            return 0

        else:
            print("Opção não encontrada.")


if __name__ == "__main__":
    main()
