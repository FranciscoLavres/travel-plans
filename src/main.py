from src.models import Viagem
from src.utils import calcular_score


def main():
    print("====== PLANO DE VIAGENS ======")

    viagens = [] #Vai guardar todas as viagens que o usuário criar na lista

    while True: #menu infinito, o programa só para quando o usuário escolher a opção de sair
        print("\n--- MENU ---")
        print("1 - Planejar uma viagem")
        print("2 - Ver ranking dos destinos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opcao: ")

        if opcao == "1":
            planejar_viagem(viagens) #chama a função de planejar viagem, passando a lista de viagens como argumento para ela poder adicionar novas viagens planejadas nessa lista

        elif opcao == "2":
            mostrar_ranking(viagens)

        elif opcao == "0":
            print("Ate logo!")
            break   #Sai do programa (break para o loop)

        else:
            print("Opcao invalida!")


# --- Planejar viagem ---

def planejar_viagem(viagens): #Essa função cria uma viagem
    try:
        pais = input("\nDiga o nome do pais (em ingles): ").lower()
        cidade = input("Diga o nome da cidade: ")
        orcamento = float(input("Seu orcamento previsto (R$): "))
    except ValueError:  
        print("Valor invalido! Digite um numero para o orcamento.")
        return

    try:
        viagem = Viagem(pais, cidade, orcamento)
    except ValueError as erro:#valor invalido para funçao
        print(f"Erro: {erro}")
        return

    sucesso = viagem.planejar_viagem() #calculo importado da classe viagem, ele vai calcular o custo aproximado e o clima, usando as funções da API

    if not sucesso:
        print("Nao foi possivel planejar essa viagem.")
        return

    print(f"\nDestino: {viagem.cidade}, {viagem.pais}")
    print(f"Custo estimado: R$ {viagem.custo_aproximado:.2f}")
    print(f"Clima: {viagem.clima}")

    if viagem.pode_viajar():    #Verifica se o orçamento é suficiente para a viagem, usando o método da classe Viagem
        print("Viagem possivel! OK")
    else:
        print("Orcamento insuficiente! X")

    viagens.append(viagem) #Guarda na lista de viagens a viagem que acabou de ser planejada, para ela aparecer no ranking depois


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
        print(f"\n{posicao} lugar: {viagem.cidade}, {viagem.pais}")
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
