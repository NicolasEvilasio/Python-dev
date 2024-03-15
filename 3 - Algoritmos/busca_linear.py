from gerar_lista import gerar_lista

numeros = gerar_lista()

# BUSCA LINEAR
numero_pesquisar = int(input('Digite o valor a ser pesquisado no vetor: '))
posicao_resultado = -1

for i in range(len(numeros)):
    if numeros[i] == numero_pesquisar:
        posicao_resultado = i
        break

if posicao_resultado < 0:
    print('O elemento não foi encontrado no vetor')
else:
    print(f'O elemento {numero_pesquisar} foi encontrado na posição {posicao_resultado}')

# FIM BUSCA LINEAR
