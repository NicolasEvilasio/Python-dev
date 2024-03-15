def busca_linear(valor_buscado: int, lista: list) -> int:
    """
    Realiza uma busca linear por um valor em uma lista e retorna a posição onde o valor foi encontrado.

    A busca linear é um algoritmo simples que percorre toda a lista sequencialmente, comparando cada elemento
    com o valor buscado até que o valor seja encontrado ou até que toda a lista seja percorrida.

    Args:
        valor_buscado (int): O valor que está sendo buscado na lista.
        lista (list): A lista na qual o valor está sendo buscado.

    Returns:
        int: A posição do valor buscado na lista. Retorna -1 se o valor não for encontrado.

    Raises:
        AttributeError: Se o valor buscado não for encontrado na lista.

    Examples:
        >>> busca_linear(5, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        4
        >>> busca_linear(10, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        Traceback (most recent call last):
            ...
        AttributeError: O elemento não foi encontrado no vetor
        >>> busca_linear(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        2
    """
    posicao_resultado = -1

    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            posicao_resultado = i
            break

    if posicao_resultado < 0:
        raise AttributeError('O elemento não foi encontrado no vetor')

    else:
        return posicao_resultado
