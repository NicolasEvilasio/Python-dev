class Veiculo:
    """Essa é a classe Veiculo. Essa classe é utilizada para instanciar novos veículos."""

    def __init__(self, cor, tipo_combustivel, potencia):
        self.__cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self.__qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0
        self._libras = 0

    def __del__(self):
        print('O objeto foi removido da memória.')

    # Definiçao dos métodos da classe
    def abastecer(self, qtd_combustivel):
        self.__qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            print('O veículo já está ligado!')
        else:
            self.__is_ligado = True
            print('O veículo foi ligado!')

    def desligar(self):
        if not self.__is_ligado:
            print('O veículo já está desligado!')
        else:
            self.__is_ligado = False
            print('O veículo foi desligado!')

    def acelerar(self, velocidade=10):
        if self.__is_ligado:
            self.__velocidade += velocidade
        else:
            print('O veículo está desligado!')

    # Getters e Setters
    @property
    def cor(self):
        return self.__cor

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @property
    def potencia(self):
        return self.__potencia

    @property
    def qtd_combustivel(self):
        return self.__qtd_combustivel

    @property
    def is_ligado(self):
        return self.__is_ligado

    @property
    def velocidade(self):
        return self.__velocidade

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo_combustivel):
        self.__tipo_combustivel = tipo_combustivel

    @potencia.setter
    def potencia(self, potencia):
        self.__potencia = potencia


# Testes rápidos
if __name__ == '__main__':
    uno = Veiculo('Vermelho', 'Gasolina', 1.0)

    print(uno.cor)
    uno.cor = 'Azul'
    print(uno.cor)

    print(uno.potencia)
    uno.potencia = 2.0
    print(uno.potencia)

    print(uno.tipo_combustivel)
    uno.tipo_combustivel = 'Etanol'
    print(uno.tipo_combustivel)
