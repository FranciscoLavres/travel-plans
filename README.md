# SISTEMA DE INVESTIMENTO
Integrantes: Francisco Lavres, Sophia Gois, Guilherme Soares, Larissa Azevedo, Gabriel Rosas

Professor: Fernando Henrique Vieira Trindade

Universidade Tiradentes / SE

## Descrição do projeto
O projeto consiste em um Simulador de Investimentos desenvolvido em Python, capaz de calcular o crescimento de um capital ao longo do tempo com base em juros compostos. O sistema permite ao usuário definir um valor inicial, aportes mensais, taxa de juros e período de investimento, retornando o valor final, o total investido e os rendimentos obtidos.

Além disso, o simulador inclui funcionalidades extras como comparação entre diferentes cenários de investimento, armazenamento de simulações e conversão de valores para dólar utilizando uma API externa, tornando a aplicação mais completa e próxima de um sistema real.

## Instruções de execução

1. Certifique-se de ter o Python instalado (versão 3.x)
2. Instale as dependências do projeto:
   `pip install -r requirements.txt`
3. Execute o arquivo principal:
   `py main`
4. Utilize o menu interativo no terminal para realizar simulações, visualizar resultados e comparar investimentos.

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
