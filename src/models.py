from src.api import obter_densidade, obter_clima
from src.utils import calcular_custo

'''
Cria o objeto Viagem, permite chamar dois métodos que necessitam manipular parametros no próprio objeto
'''

class Viagem:

    def __init__(self, pais, cidade, orcamento):
        if not pais:
            raise ValueError("Pais invalido.")

        if not cidade:
            raise ValueError("Cidade invalida.")

        if orcamento < 0:
            raise ValueError("Orcamento invalido por ser valor negativo.")

        self.pais = pais
        self.cidade = cidade
        self.orcamento = orcamento
        self.custo_aproximado = 0
        self.clima = None

    def classificando(self):
        try:
            densidade = obter_densidade(self.pais)
            clima = obter_clima(self.cidade)

            if densidade is None or clima is None:
                print("Nao foi possivel planejar a viagem.")
                return False

            self.clima = clima
            self.custo_aproximado = calcular_custo(densidade, clima)
            return True

        except Exception:
            print("Erro ao planejar a viagem.")
            return False

    def pode_viajar(self):
        return self.orcamento >= self.custo_aproximado
