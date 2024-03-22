def busca_binaria(valor_buscado: int, lista: list) -> int:
    """
    Realiza uma busca binária por um valor em uma lista e retorna a posição onde o valor foi encontrado.

    A busca binária é um algoritmo que divide a lista ao meio repetidamente, comparando o valor buscado
    com o elemento central. Isso permite encontrar o valor de forma eficiente.

    Args:
        valor_buscado (int): O valor que está sendo buscado na lista.
        lista (list): A lista ordenada na qual o valor está sendo buscado.

    Returns:
        int: A posição do valor buscado na lista. Retorna -1 se o valor não for encontrado.

    Raises:
        AttributeError: Se o valor buscado não for encontrado na lista.

    Examples:
        >>> busca_binaria(5, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        4
        >>> busca_binaria(10, [1, 2, 3, 4, 5, 6, 7, 8, 9])

        >>> busca_binaria(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        2
        >>> busca_binaria(10, [])
        """
    inicio = 0
    fim = len(lista)
    meio = (inicio + fim) // 2

    if valor_buscado not in lista:
        return None

    # implementação do algorítmo de busca binária
    while valor_buscado != lista[meio]:
        if valor_buscado < lista[meio]:
            fim = meio - 1
            meio = (inicio + fim) // 2

        elif valor_buscado > lista[meio]:
            meio = (meio + 1 + fim) // 2

    return meio
