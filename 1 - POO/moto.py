import veiculo


class Moto(veiculo.Veiculo):
    """Essa é a classe Moto. Essa classe é utilizada para instanciar novas motos."""
    def __init__(self, cor, tipo_combustivel, potencia, qtd_cilindradas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_cilindradas = qtd_cilindradas

