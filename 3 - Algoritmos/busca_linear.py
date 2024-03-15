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
    """
    posicao_resultado = -1

    for i in range(len(lista)):
        if numeros[i] == valor_buscado:
            posicao_resultado = i
            break

    if posicao_resultado < 0:
        print('O elemento não foi encontrado no vetor')
        raise AttributeError

    else:
        return posicao_resultado


if __name__ == '__main__':
    from gerar_lista import gerar_lista

    numeros = gerar_lista()
    numero_pesquisar = int(input('Digite o valor a ser pesquisado no vetor: '))
    posicao = busca_linear(numero_pesquisar, numeros)

    print(f'O elemento {numero_pesquisar} foi encontrado na posição {posicao}')
