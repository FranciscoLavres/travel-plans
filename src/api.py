import requests


def obter_densidade(nome):
    try:
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

    except Exception:
        print("Erro ao buscar dados do pais. Verifique o nome digitado.")
        return None


def obter_clima(cidade):
    try:
        # Busca as coordenadas da cidade pelo nome
        geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1")
        geo_json = geo.json()

        latitude = geo_json["results"][0]["latitude"]
        longitude = geo_json["results"][0]["longitude"]

        # Busca o clima usando as coordenadas
        clima = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        )
        clima_json = clima.json()

        codigo = clima_json["current_weather"]["weathercode"]

        # Codigos WMO:
        # 0 = ceu limpo
        # 1, 2, 3 = parcialmente nublado
        # 51+ = chuva, neve, tempestade
        if codigo == 0:
            return "bom"
        elif codigo <= 3:
            return "normal"
        else:
            return "ruim"

    except Exception:
        print("Erro ao buscar clima. Verifique o nome da cidade.")
        return None


def obter_cotacao_dolar():
    try:
        dados = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        dados_json = dados.json()
        cotacao = dados_json["rates"]["BRL"]
        return cotacao
    except Exception:
        print("Erro ao buscar cotacao do dolar.")
        return None
