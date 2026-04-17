from src.models import Viagem
from src.utils import calcular_score

'''
Define o main que vaii ser a interface onde o usuário interage e da possibilidade de chamar as funções que manipulam e 
organizam as outras.
'''


def main():
    print("====== PLANO DE VIAGENS ======")

    viagens = []

    while True:
        print("\n--- MENU ---")
        print("1 - Planejar uma viagem")
        print("2 - Ver ranking dos destinos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            planejar_viagem(viagens)

        elif opcao == "2":
            mostrar_ranking(viagens)

        elif opcao == "0":
            print("Ate logo!")
            break

        else:
            print("Opcao invalida!")


# --- Planejar viagem ---

def planejar_viagem(viagens):
    try:
        pais = input("\nDiga o nome do pais (em ingles): ").lower()
        cidade = input("Diga o nome da cidade: ")
        orcamento = float(input("Seu orcamento previsto (R$): "))
    except ValueError:  
        print("Valor invalido! Digite um numero para o orcamento.")
        return

    try:
        viagem = Viagem(pais, cidade, orcamento)
    except ValueError as erro:
        print(f"Erro: {erro}")
        return

    sucesso = viagem.classificando()

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

    def pegar_score(v):
        return v.score

    viagens_ordenadas = sorted(viagens, key=pegar_score, reverse=True)

    posicao = 1
    for viagem in viagens_ordenadas:
        print(f"\n{posicao}º lugar: {viagem.cidade}, {viagem.pais}")
        print(f"   Clima: {viagem.clima}")
        print(f"   Custo: R$ {viagem.custo_aproximado:.2f}")
        print(f"   Pontuacao: {viagem.score:.1f}")

        if viagem.pode_viajar():
            print("   Status: Cabe no orcamento!")
        else:
            print("   Status: Acima do orcamento")

        posicao += 1

    input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    main()
