from src.api import obter_densidade, obter_clima
from src.utils import calcular_custo


class Viagem:

    def __init__(self, pais, cidade, orcamento):
        if not pais:
            raise ValueError("País inválido.")

        if not cidade:
            raise ValueError("Cidade inválida.")

        if orcamento < 0:
            raise ValueError("Orçamento inválido por ser valor negativo.")

        self.pais = pais
        self.cidade = cidade
        self.orcamento = orcamento
        self.custo_aproximado = 0
        self.clima = None

    def pode_viajar(self):
        return self.orcamento >= self.custo_aproximado

    def planejar_viagem(self):

        densidade = obter_densidade(self.pais)
        clima = obter_clima(self.cidade)

        self.custo_aproximado = calcular_custo(densidade, clima)

