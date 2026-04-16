from src.models import Viagem
from src.utils import calcular_score, simular_investimento, salvar_viagens, carregar_viagens
from src.api import obter_cotacao_dolar


def main():
    print("====== PLANO DE VIAGENS ======")

    viagens = []

    while True:
        print("\n--- MENU ---")
        print("1 - Planejar uma viagem")
        print("2 - Ver ranking dos destinos")
        print("3 - Simular investimento para a viagem")
        print("4 - Comparar investimentos")
        print("5 - Converter valores para dolar")
        print("6 - Salvar viagens")
        print("7 - Carregar viagens salvas")
        print("0 - Sair")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            planejar_viagem(viagens)

        elif opcao == "2":
            mostrar_ranking(viagens)

        elif opcao == "3":
            menu_investimento()

        elif opcao == "4":
            comparar_investimentos()

        elif opcao == "5":
            converter_para_dolar()

        elif opcao == "6":
            salvar_viagens(viagens)

        elif opcao == "7":
            dados = carregar_viagens()
            if len(dados) > 0:
                print("\n--- Viagens salvas ---")
                for v in dados:
                    print(f"  {v['cidade']}, {v['pais']} - Custo: R$ {v['custo_aproximado']:.2f} - Clima: {v['clima']}")

        elif opcao == "0":
            print("Ate logo!")
            break

        else:
            print("Opcao invalida!")


# --- Planejar viagem ---

def planejar_viagem(viagens):
    try:
        pais = input("\nDiga o nome do pais: ").lower()
        cidade = input("Diga o nome da cidade: ")
        orcamento = float(input("Seu orcamento previsto: "))
    except ValueError:
        print("Valor invalido! Digite um numero para o orcamento.")
        return

    try:
        viagem = Viagem(pais, cidade, orcamento)
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    sucesso = viagem.planejar_viagem()

    if not sucesso:
        print("Nao foi possivel planejar essa viagem.")
        return

    print(f"\nDestino: {viagem.cidade}, {viagem.pais}")
    print(f"Custo estimado: R$ {viagem.custo_aproximado:.2f}")
    print(f"Clima: {viagem.clima}")

    if viagem.pode_viajar():
        print("Viagem possivel! OK")
    else:
        print("Orcamento insuficiente! X")

    viagens.append(viagem)


# --- Ranking ---

def mostrar_ranking(viagens):
    if len(viagens) == 0:
        print("\nNenhuma viagem planejada ainda.")
        return

    print("\n====== RANKING DOS MELHORES DESTINOS ======")

    for viagem in viagens:
        viagem.score = calcular_score(viagem)

    viagens_ordenadas = sorted(viagens, key=lambda v: v.score, reverse=True)

    posicao = 1
    for viagem in viagens_ordenadas:
        print(f"\n{posicao} lugar: {viagem.cidade}, {viagem.pais}")
        print(f"   Clima: {viagem.clima}")
        print(f"   Custo: R$ {viagem.custo_aproximado:.2f}")
        print(f"   Pontuacao: {viagem.score:.1f}")

        if viagem.pode_viajar():
            print("   Status: Cabe no orcamento!")
        else:
            print("   Status: Acima do orcamento")

        posicao += 1


# --- Simulacao de investimento ---

def menu_investimento():
    print("\n--- SIMULACAO DE INVESTIMENTO ---")

    try:
        valor_inicial = float(input("Valor inicial (R$): "))
        aporte_mensal = float(input("Aporte mensal (R$): "))
        taxa_mensal = float(input("Taxa de juros mensal (%): "))
        meses = int(input("Quantidade de meses: "))
    except ValueError:
        print("Valor invalido! Digite apenas numeros.")
        return

    resultado = simular_investimento(valor_inicial, aporte_mensal, taxa_mensal, meses)

    print(f"\n--- RESULTADO ---")
    print(f"Total investido: R$ {resultado['total_investido']:.2f}")
    print(f"Valor final: R$ {resultado['valor_final']:.2f}")
    print(f"Lucro (juros): R$ {resultado['lucro']:.2f}")

    ver_historico = input("\nVer historico mes a mes? (s/n): ").lower()
    if ver_historico == "s":
        print("\n--- HISTORICO ---")
        for h in resultado["historico"]:
            print(f"  Mes {h['mes']}: Saldo R$ {h['saldo']:.2f} | Investido R$ {h['investido']:.2f}")


# --- Comparar investimentos ---

def comparar_investimentos():
    print("\n--- COMPARAR INVESTIMENTOS ---")
    print("Vamos comparar 2 cenarios diferentes.\n")

    resultados = []

    for i in range(1, 3):
        print(f"-- Cenario {i} --")
        try:
            valor_inicial = float(input("Valor inicial (R$): "))
            aporte_mensal = float(input("Aporte mensal (R$): "))
            taxa_mensal = float(input("Taxa de juros mensal (%): "))
            meses = int(input("Quantidade de meses: "))
        except ValueError:
            print("Valor invalido!")
            return

        resultado = simular_investimento(valor_inicial, aporte_mensal, taxa_mensal, meses)
        resultado["cenario"] = i
        resultados.append(resultado)
        print()

    print("--- COMPARACAO ---")
    for r in resultados:
        print(f"Cenario {r['cenario']}: Valor final R$ {r['valor_final']:.2f} | Lucro R$ {r['lucro']:.2f}")

    if resultados[0]["valor_final"] > resultados[1]["valor_final"]:
        print("\nO Cenario 1 e mais vantajoso!")
    elif resultados[1]["valor_final"] > resultados[0]["valor_final"]:
        print("\nO Cenario 2 e mais vantajoso!")
    else:
        print("\nOs dois cenarios sao iguais!")


# --- Conversao de moeda ---

def converter_para_dolar():
    print("\n--- CONVERSAO PARA DOLAR ---")

    try:
        valor_reais = float(input("Digite o valor em reais (R$): "))
    except ValueError:
        print("Valor invalido!")
        return

    cotacao = obter_cotacao_dolar()

    if cotacao is None:
        print("Nao foi possivel obter a cotacao.")
        return

    valor_dolar = valor_reais / cotacao

    print(f"\nCotacao atual: R$ {cotacao:.2f} = US$ 1.00")
    print(f"R$ {valor_reais:.2f} = US$ {valor_dolar:.2f}")


if __name__ == "__main__":
    main()
