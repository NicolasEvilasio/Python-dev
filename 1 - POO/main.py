import carro
import moto


uno_vermelho = carro.Carro('vermelho', 'gasolina', 90, 4)
uno_vermelho.ligar()

print(uno_vermelho.cor)
uno_vermelho.cor = 'azul'
print(uno_vermelho.cor)

print(f'Combustível: {uno_vermelho.qtd_combustivel}')
uno_vermelho.abastecer(10)
print(f'Combustível: {uno_vermelho.qtd_combustivel}')

print(f'Velocidade: {uno_vermelho.velocidade}')
uno_vermelho.acelerar()
print(f'Velocidade: {uno_vermelho.velocidade}')
uno_vermelho.acelerar(50)
print(f'Velocidade: {uno_vermelho.velocidade}')

uno_vermelho.desligar()

moto_vermelha = moto.Moto('vermelho', 'gasolina', 90, 110)
moto_vermelha.ligar()
