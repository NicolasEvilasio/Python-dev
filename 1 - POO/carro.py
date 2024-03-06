import veiculo


class Carro(veiculo.Veiculo):
    """Essa é a classe Carro. Essa classe é utilizada para instanciar novos carros."""
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas
        self._libras = 30

    def abastecer(self, qtd_combustivel):
        print('O método foi chamado a partir da classe carro')
        if self.qtd_combustivel >= 30:  # usando o getter qtd_combustivel definido na superclasse
            print('O tanque do carro está cheio')
        else:
            super().abastecer(qtd_combustivel)  # usando o método definido na superclasse

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self._velocidade += velocidade
        else:
            print('O carro está desligado!')