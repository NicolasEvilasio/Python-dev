import veiculo


class Moto(veiculo.Veiculo):
    """Essa é a classe Moto. Essa classe é utilizada para instanciar novas motos."""
    def __init__(self, cor, tipo_combustivel, potencia, qtd_cilindradas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_cilindradas = qtd_cilindradas
        self._libras = 20

    def abastecer(self, qtd_combustivel):
        print('O método foi chamado a partir da classe moto')
        if self.qtd_combustivel >= 15:  # usando o getter qtd_combustivel definido na superclasse
            print('O tanque da moto está cheio')
        else:
            super().abastecer(qtd_combustivel)  # usando o método definido na superclasse

    def acelerar(self, velocidade=15):
        if self.is_ligado:
            self._velocidade += velocidade
        else:
            print('A moto está desligada!')
