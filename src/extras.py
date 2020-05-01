#-*- coding: utf-8 -*-

def header():
	"""Cabeçalho do Programa"""

	print("=== Atividade de Implementação ==="
        +"\nGrupo:\nJoão Vítor Silva Ferreira\nAdiel Vieira Nascimento"
        +"\n\nTurma:\nN01\n")


def options():
	"""Opções do Programa"""

	print("=== Opções ==="
        +"\n1-Cadastrar Grafo"
        +"\n2-Printar Grafo"
        +"\n3-Adicionar Aresta"
        +"\n4-Remover Aresta"
        +"\n5-Adjacentes (getAdjacentes)"
        +"\n6-Verificar se o Grafo é completo (ehCompleto)"
        +"\n7-Verificar se o Grafo é regular (ehRegular)"
        +"\n8-Principais Grafos de Coloração (Extra)"
        +"\n9-Verificar se o Grafo é conexo (ehConexo)"
        +"\n10-Busca em Largura"
        +"\n99-Parar o Programa")


def exColoracao():
    """Exemplos de Grafos de Coloração"""

    print("C5 (Grafo Circular)     | X(G) = 3"
       +"\nW5 (Grafo Roda (Wheel)) | X(G) = 3"
       +"\nW6 (Grafo Roda (Wheel)) | X(G) = 4"
       +"\nGrafo de Pertersen      | X(G) = 3")


def GrafoNotFoundError():
    print("É necessário cadastrar o Grafo primeiro.")
