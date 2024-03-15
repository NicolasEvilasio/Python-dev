from gerar_lista import gerar_lista

numeros = gerar_lista()


def selection_sort(lista: list) -> list:
    tamanho_lista = len(lista)

    if tamanho_lista <= 0:
        print('Lista vazia')
        return []

    else:
        for i in range(tamanho_lista):
            menor_indice = i
            for j in range(i + 1, tamanho_lista):
                if numeros[j] < numeros[i]:
                    numeros[i], numeros[j] = numeros[j], numeros[i]

    return numeros


print(selection_sort(numeros))
