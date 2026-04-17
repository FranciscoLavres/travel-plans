import requests

'''
Área onde pega as informações necessárias das APIs, as duas são abertas e não necessitam de API_KEY.

A primeira obtem a densidade demográfica do país a partir da divisão da população do país pela área em Km²,
após isto transforma em um fator de multiplicação para depois calcular o custo da viagem

A segunda pega a cidade destino e verifica o clima dela a partir da latitude e longitude, depois, 
confirma com o usuário se o local está certo e retorna "ruim", "normal" ou "bom" a partir do clima atual na região.
'''

def obter_densidade(pais):
    try:
        dados = requests.get(f"https://restcountries.com/v3.1/name/{pais}")
        dados_json = dados.json()
        area_pais = dados_json[0]["area"]
        populacao_pais = dados_json[0]["population"]
        densidade = populacao_pais / area_pais

        '''
        Transformação da densidade demográfica para um fator que vai 
        multiplicar o custo da viagem
        '''
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

        dados = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1")
        dados_json = dados.json()

        resultado = dados_json["results"][0]
        latitude = resultado["latitude"]
        longitude = resultado["longitude"]

        # Confirmação de localização
        nome = resultado["name"]
        regiao = resultado.get("admin1", "") #Esse get tenta pegar o primeiro, se não der, o segundo é o valor padrão
        pais = resultado.get("country", "")
        local_completo = f"{nome}, {regiao}, {pais}" if regiao else f"{nome}, {pais}"

        print(f"\nLocalizacao encontrada: {local_completo}")
        confirma = input("É essa a cidade correta? (s/n): ").lower()

        if confirma != "s":
            print("Busca cancelada. Tente novamente com outro nome.")
            return None

        clima = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
        clima_json = clima.json()

        codigo = clima_json["current_weather"]["weathercode"]


        ''' 0 = céu limpo
            1, 2, 3 = parcialmente nublado
            51+ = chuva, neve, tempestade '''

        if codigo == 0:
            return "bom"
        elif codigo <= 3:
            return "normal"
        else:
            return "ruim"

    except Exception:
        print("Erro ao buscar clima. Verifique o nome da cidade.")
        return None
