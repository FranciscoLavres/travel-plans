import requests
from src.exceptions import APIError
import os

chave = os.getenv("API_KEY")

def obter_densidade(nome):
    dados = requests.get(f"https://restcountries.com/v3.1/name/{nome}")
    dados_json = dados.json()

    area_pais = dados_json[0]["area"]

    populacao_pais = dados_json[0]["population"]

    densidade = populacao_pais / area_pais

    if densidade < 50:
        fator = 0.8
    elif densidade < 150:
        fator = 1.1
    else:
        fator = 1.5

    return fator


def obter_clima(cidade):
    dados = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&units=metric")

    dados_json = dados.json()

    clima = dados_json["weather"][0]["description"]

    nota_clima = None

    if "rain" in clima:
        nota_clima = "ruim"

    if "clouds" in clima:
        nota_clima = "normal"

    if "clear" in clima:
        nota_clima = "bom"

    return nota_clima
