#Definicao do grafo
grafo = [[0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]

#Metodo responsavel por remover um no(Marcamos o mesmo como None)
def remove_no(no):
    grafo[no] = None
    
#Retornar o no do grafo que possui grau 0(sera retornado o primeiro no de grau 0 encontrado)
def retorna_no_grau_de_entrada_0():
    for i in range(0, len(grafo)):
        if(grafo[i] != None):
            grau_de_entrada = retorna_grau_de_entrada(i)
            if (grau_de_entrada == 0):
                return i

#Dado um no, verificar se o mesmo possui grau 0
def retorna_grau_de_entrada(no_atual):
    grau_de_entrada = 0
    for no in grafo:
        if(no != None):
            for aresta in range(0, len(no)):
                if(aresta == no_atual and no[aresta] != 0):
                    grau_de_entrada += 1

    return grau_de_entrada

#Metodo responsavel por realizar a ordenacao topologica no grafo
def ordenacao_topologica():
    ordenacao_topologica = []
    for i in range(0, len(grafo)):
        no_atual = retorna_no_grau_de_entrada_0()
        if no_atual == None:
            print("Nao é possivel realizar a ordenacao topologica")
            break
        ordenacao_topologica.append(no_atual+1)
        remove_no(no_atual)

    return ordenacao_topologica

#Main
if __name__ == "__main__":
    ordenacao_topologica_ordem = ordenacao_topologica()
    if ordenacao_topologica_ordem != []:
        print('Ordem: ', end='')
        for i in range(0, len(ordenacao_topologica_ordem)):
            if(i == len(ordenacao_topologica_ordem) - 1):
                print(ordenacao_topologica_ordem[i])
                break
            print(ordenacao_topologica_ordem[i], end='-')
