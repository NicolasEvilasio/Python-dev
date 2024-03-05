import veiculo


class Carro(veiculo.Veiculo):
    """Essa é a classe Carro. Essa classe é utilizada para instanciar novos carros."""
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas

