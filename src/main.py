from src.models import Viagem
from src.api import obter_clima

#from src.plano import planejar_viagem


def main():
    print("====== PLANO DE VIAGENS ======")
    while True:

        pais = input("\nDiga o nome do país: ").lower()
        cidade = input("\nDiga o nome do cidade: ")
        orcamento = float(input("\nSeu orçamento previsto: "))

        viagem = Viagem(pais, cidade, orcamento)
        viagem.planejar_viagem()

        #if viagem is None:
           # print("Não foi possível planejar a viagem.")
            #continue

        print(f"\nDestino: {viagem.cidade}, {viagem.pais}")
        print(f"Custo estimado: {viagem.custo_aproximado:.2f}")
        print(f"Clima: {obter_clima(viagem.cidade)}")

        if not viagem.pode_viajar():
            print("Orçamento insuficiente X")
        else:
            print("Viagem possível OK")


        opcao = input("\nDeseja continuar? (s/n): ").lower()
        if opcao != "s":
            break


if __name__ == "__main__":
    main()