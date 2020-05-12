matriz = [[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]

def busca_profundidade(matriz, vertice):
    pilha = []
    visitados = []
    resultado = []
    for i in range(len(matriz)):
        visitados.append(False)
    visitados[vertice] = True
    #F T F F
    pilha.append(vertice)
    contador = 0

    while len(pilha) != 0: 
        topo = pilha[len(pilha)-1]
        while  contador != len(matriz[i]):
            if (visitados[contador] == False) and matriz[topo][contador] != 0:
                #T T T T 
                visitados[contador] = True
                pilha.append(contador)
            contador+= 1
        
        contador = 0
        resultado.append(pilha.pop())
    return resultado
    
def ehConexo(matriz):
    lista = busca_profundidade(matriz,0)
    if len(matriz) == len(lista):
       return True
    else:
       return False
    

if __name__ == "__main__":
    busca_profundidade(matriz,0)    
    print(ehConexo(matriz))
