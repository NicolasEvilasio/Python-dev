class Veiculo:
    """Essa é a classe Veiculo. Essa classe é utilizada para instanciar novos veículos."""

    def __init__(self, cor, tipo_combustivel, potencia):
        self.cor = cor
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = 0
        self.is_ligado = False
        self.velocidade = 0

    def __del__(self):
        print('O objeto foi removido da memória.')

    def abastecer(self, qtd_combustivel):
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado:
            print('O veículo já está ligado!')
        else:
            self.is_ligado = True
            print('O veículo foi ligado!')

    def desligar(self):
        if not self.is_ligado:
            print('O veículo já está desligado!')
        else:
            self.is_ligado = False
            print('O veículo foi desligado!')

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print('O veículo está desligado!')
