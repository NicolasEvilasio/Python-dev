def gerar_lista():
    tamanho = int(input("Digite o tamanho do vetor: "))
    numeros = list()

    for i in range(tamanho):
        valor = int(input(f'Digite o número do vetor na posião {i}: '))
        numeros.append(valor)

    print('Vetor: ', numeros)
    print('Posição 0:', numeros[0])

    return numeros
