from selection_sort import selection_sort
"""
Dado uma lista de produtos com as informações: Id, Nome e Quantidade. 

1 - Ordene os dados de forma que sejam listados de acordo com os produtos com a quantidade em ordem decrescente. 
2 - Caso dois produtos tenham a mesma quantidade, eles devem ser exibidos em ordem alfabética. 
3 - Caso dois produtos tenham o mesmo nome, eles devem ser listados pelo id em ordem crescente.

Entrada de dados

5
33 Monitor 10
85 Mouse 7
56 Notebook 3
19 Processador 23
22 HD 7
Saída de dados

Processador
Monitor
HD
Mouse
Notebook
"""


class Produto:
    def __init__(self, id, nome, quantidade):
        self.__id = id
        self.__nome = nome
        self.__quantidade = quantidade

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def quantidade(self):
        return self.__quantidade

    @id.setter
    def id(self, id):
        self.__id = id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade


if __name__ == '__main__':

    t = int(input())
    produtos = list()
    for i in range(t):
        id, nome, quantidade = input().split(' ')

        produto = Produto(int(id), nome, int(quantidade))
        produtos.append(produto)

    # Selection sort - requisito 01
    for i in range(t):
        menor_indice = i
        for j in range(i + 1, t):
            if produtos[j].quantidade < produtos[menor_indice].quantidade:
                menor_indice = j

        produtos[i], produtos[menor_indice] = produtos[menor_indice], produtos[i]

    for p in produtos:
        print(p.quantidade)