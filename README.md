# SISTEMA DE INVESTIMENTO
Integrantes: Francisco Lavres, Sophia Gois, Guilherme Soares, Larissa Azevedo, Gabriel Rosas

Professor: Fernando Henrique Vieira Trindade

Universidade Tiradentes / SE

## Descrição do projeto
Sistema em Python que planeja viagens com base em dados externos. Ele utiliza as APIs da OpenWeather e REST Countries 
para obter clima e informações do país, calcula um custo estimado e verifica se a viagem é viável conforme o orçamento do usuário.
## Instruções de execução

1. Certifique-se de ter o Python instalado (versão 3.x)
2. Instale as dependências do projeto:
   `pip install -r requirements.txt`
3. Configurar a API
    no seu arquivo `api.py`, substitua: `API_KEY` por sua chave da OpenWeather.
4. Execute o arquivo principal:
   `py main`
5. Usar o sistema, 

## Principais Funcionalidades

* **Simulação de investimento**
  
  Permite calcular o rendimento de um investimento com base em juros compostos e aportes mensais.
* **Cálculo detalhado**

  Exibe o valor final, total investido e o lucro obtido (juros).
* **Histórico da simulação**

  Mostra a evolução do saldo ao longo do tempo (mês a mês).
* **Comparação de investimentos**

  Possibilita comparar diferentes cenários e identificar o mais vantajoso.
* **Conversão de moeda**

  Permite visualizar os resultados em reais ou em dólar por meio de integração com API de cotação.

* **Persistência de dados**

  Salva e carrega simulações utilizando arquivos JSON.
