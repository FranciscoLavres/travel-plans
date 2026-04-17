# PLANEJAMENTO DE VIAGENS
Integrantes: Francisco Lavres, Sophia Gois, Guilherme Soares, Larissa Azevedo, Gabriel Rosas

Professor: Fernando Henrique Vieira Trindade

Universidade Tiradentes / SE

## Descrição do projeto
Sistema em Python que planeja viagens com base em dados externos. Ele utiliza as APIs da OpenMeteo e REST Countries 
para obter clima e informações do país, calcula um custo estimado e verifica se a viagem é viável conforme o orçamento do usuário, 
após isto, o sistema armazena as viagens anteriores e da a opção de ranquear todas.
## Instruções de execução

1. Certifique-se de ter o Python instalado (versão 3.x)
2. Instale as dependências do projeto:
   `py -m pip install -r requirements`
3. Execute o arquivo principal:
   `py -m main`
4. Usar o sistema, 

## Principais Funcionalidades

* **Planejamento de Viagens**
  
  Permite ter um planejamento melhor com base na classificação do clima do destino e no orçamento disponivel.
* **Integração com APIs externas**

  Consome duas APIs para obter informações do clima (OpenMeteo) e da densidade demográfica (REST Countries).
* **Análise de clima**

  Análise de clima, o classificando como "bom", "normal" ou "ruim".
* **Comparação de viagens**

  Compara os destinos simulados e diz qual o melhor para ir com base no clima e preço.
* **Calculo de custo da viagem**

  Permite visualizar uma média de quanto vai custar a ida para o seu destino.

* **Tratamento de erros**

  Caso ocorra algum erro, o próprio sistema irá tratá-lo.
