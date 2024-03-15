# 0 | 1 | 2 | 3 | 4
# 5 | 2 | 4 | 6 | 1

numeros = list()
tamanho = int(input("Digite o tamanho do vetor: "))

for i in range(tamanho):
    valor = int(input(f'Digite o número do vetor na posião {i}: '))
    numeros.append(valor)

print('Vetor: ', numeros)
print('Posição 1:', numeros[1])

# BUSCA LINEAR
numero_pesquisar = int(input('Digite o valor a ser pesquisado no vetor: '))
posicao_resultado = -1

for i in range(tamanho):
    if numeros[i] == numero_pesquisar:
        posicao_resultado = i
        break

if posicao_resultado < 0:
    print('O elemento não foi encontrado no vetor')
else:
    print(f'O elemento {numero_pesquisar} foi encontrado na posição {posicao_resultado}')

# FIM BUSCA LINEAR
