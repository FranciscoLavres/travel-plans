import requests #essa biblioteca serve para fazer requisições HTTP (acessar APIs na internet)
                #requests faz isso via código.

def obter_densidade(nome): #nome do pais
    try:
        dados = requests.get(f"https://restcountries.com/v3.1/name/{nome}") #Faz uma requisição GET para a API restcountries
        dados_json = dados.json()   #Converte a resposta da API (texto) em dicionário Python
        #pegando valores
        area_pais = dados_json[0]["area"]
        populacao_pais = dados_json[0]["population"]
        densidade = populacao_pais / area_pais

        if densidade < 50: #aq tranformo um numero em fator/ Fator = um número que vai influenciar algum cálculo depoi
            fator = 0.8
        elif densidade < 150:
            fator = 1.1
        else:
            fator = 1.5

        return fator

    except Exception: #exception é um erro generioco, se qualque erro acontecer ele faz iso ai embaixo
        print("Erro ao buscar dados do pais. Verifique o nome digitado.")
        return None


def obter_clima(cidade): #recebe o nome de uma cidade e retorna se o clima é bom, normal ou ruim
    try:
        # Busca as coordenadas da cidade pelo nome
        geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1") #usa API de geolocalizaçao e converte nome da cidade em cordenadas
        geo_json = geo.json() #Converte a resposta da API para um dicionário Python
        #essa parte é acessar dados dentro de um JSON
        resultado = geo_json["results"][0] #0 pq pega o 1 num da lista
        latitude = resultado["latitude"]    #Pega o valor da chave "latitude"
        longitude = resultado["longitude"]

        # Mostra a localizacao encontrada para o usuario confirmar
        nome = resultado["name"]
        regiao = resultado.get("admin1", "") #get ta aq para evutar erro, ele tenta pegar o primmeor, se n der vai no outro
        pais = resultado.get("country", "")
        local_completo = f"{nome}, {regiao}, {pais}" if regiao else f"{nome}, {pais}"

        print(f"\nLocalizacao encontrada: {local_completo}")
        confirma = input("E essa a cidade correta? (s/n): ").lower() #converte tudo pro maisculo, para evitar erro de digitação do usuário

        if confirma != "s": #diferente de s
            print("Busca cancelada. Tente novamente com outro nome.")
            return None

        # Busca o clima usando as coordenadas
        clima = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        ) #faz uma requisição para a API de clima usando as coordenadas da cidade
        clima_json = clima.json() #convete a resposta da API para um dicionário Python

        codigo = clima_json["current_weather"]["weathercode"] #Pega o número que representa o clima

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
