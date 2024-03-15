def selection_sort(lista: list) -> list:
    """
    Ordena uma lista de elementos usando o algoritmo Selection Sort.

    O Selection Sort é um algoritmo de ordenação que divide a lista em duas partes:
    uma parte ordenada e outra parte desordenada. Ele procura o menor elemento
    na parte desordenada e o move para a parte ordenada. Esse processo é repetido
    até que todos os elementos estejam na parte ordenada.

    Args:
        lista (list): A lista de elementos a ser ordenada.

    Returns:
        list: A lista ordenada.

    Examples:
        >>> selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        >>> selection_sort([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
        >>> selection_sort([1, 2, 3, 4, 5])
        [1, 2, 3, 4, 5]
    """
    tamanho_lista = len(lista)

    if tamanho_lista <= 0:
        print('Lista vazia')
        return []

    else:
        for i in range(tamanho_lista):
            menor_indice = i

            for j in range(i + 1, tamanho_lista):
                if lista[j] < lista[menor_indice]:
                    menor_indice = j

            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

    return lista
