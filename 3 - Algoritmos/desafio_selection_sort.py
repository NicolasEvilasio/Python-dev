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


def sort_produtos(produtos):
    """
    Ordena a lista de produtos de acordo com as regras especificadas.

    1. Ordene os dados de forma que sejam listados de acordo com os produtos com a quantidade em ordem decrescente.
    2. Caso dois produtos tenham a mesma quantidade, eles devem ser exibidos em ordem alfabética.
    3. Caso dois produtos tenham o mesmo nome, eles devem ser listados pelo id em ordem crescente.

    :param produtos: Uma lista de objetos da classe Produto.
    :return: None (a lista de produtos é ordenada in-place).

    Examples:
        >>> produto1 = Produto(1, 'ProdutoA', 10)
        >>> produto2 = Produto(2, 'ProdutoB', 5)
        >>> produto3 = Produto(3, 'ProdutoC', 10)
        >>> produto4 = Produto(4, 'ProdutoD', 8)
        >>> produtos = [produto1, produto2, produto3, produto4]
        >>> sort_produtos(produtos)
        >>> for p in produtos:
        ...     print(p.quantidade, p.nome, p.id)
        10 ProdutoA 1
        10 ProdutoC 3
        8 ProdutoD 4
        5 ProdutoB 2

        >>> produto1 = Produto(1, 'ProdutoA', 10)
        >>> produto2 = Produto(2, 'ProdutoA', 10)
        >>> produto3 = Produto(3, 'ProdutoC', 5)
        >>> produto4 = Produto(4, 'ProdutoD', 8)
        >>> produtos = [produto1, produto2, produto3, produto4]
        >>> sort_produtos(produtos)
        >>> for p in produtos:
        ...     print(p.quantidade, p.nome, p.id)
        10 ProdutoA 1
        10 ProdutoA 2
        8 ProdutoD 4
        5 ProdutoC 3

        >>> produto1 = Produto(1, 'ProdutoA', 10)
        >>> produto2 = Produto(2, 'ProdutoA', 1)
        >>> produto3 = Produto(3, 'ProdutoC', 5)
        >>> produto4 = Produto(4, 'ProdutoD', 8)
        >>> produtos = [produto1, produto2, produto3, produto4]
        >>> sort_produtos(produtos)
        >>> for p in produtos:
        ...     print(p.quantidade, p.nome, p.id)
        10 ProdutoA 1
        8 ProdutoD 4
        5 ProdutoC 3
        1 ProdutoA 2
    """
    for i in range(len(produtos)):
        maior_indice = i
        for j in range(i + 1, len(produtos)):
            if produtos[j].quantidade > produtos[maior_indice].quantidade:
                maior_indice = j
            elif produtos[j].quantidade == produtos[maior_indice].quantidade:
                maior_indice = j if produtos[j].nome < produtos[maior_indice].nome else maior_indice
                if produtos[j].nome == produtos[maior_indice].nome:
                    maior_indice = j if produtos[j].id < produtos[maior_indice].id else maior_indice
        produtos[i], produtos[maior_indice] = produtos[maior_indice], produtos[i]


if __name__ == '__main__':

    t = int(input())
    produtos = list()
    for _ in range(t):
        id, nome, quantidade = input().split()
        produto = Produto(int(id), nome, int(quantidade))
        produtos.append(produto)

    sort_produtos(produtos)

    for p in produtos:
        print(p.quantidade, p.nome, p.id)
