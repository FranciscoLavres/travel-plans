'''
A primeira calcula quanto tudo vai custar de fato, utilizando um valor base e um multiplicador que aumenta o
valor dependendo do fator que recebeu previamente definido e do clima, que pode somar +1, +2 ou +3

A segunda da um score para o objeto, com base no valor do preço e do clima, quanto menor o custo e melhor o clima,
mais caro fica
'''

def calcular_custo(fator, clima):
    base = 1000
    multiplicador = fator

    if clima == "ruim":
        multiplicador += 1

    if clima == "normal":
        multiplicador += 2

    if clima == "bom":
        multiplicador += 3

    return base * multiplicador


def calcular_score(viagem):
    if viagem.clima == "bom":
        score_clima = 3
    elif viagem.clima == "normal":
        score_clima = 2
    else:
        score_clima = 1

    score_custo = max(0, 5000 - viagem.custo_aproximado) / 1000

    score_final = score_clima + score_custo
    return score_final
