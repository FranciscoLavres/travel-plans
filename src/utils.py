import json
import os

ARQUIVO_DADOS = "dados_viagens.json"


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


# --- Simulacao de investimento ---

def simular_investimento(valor_inicial, aporte_mensal, taxa_mensal, meses):
    saldo = valor_inicial
    total_investido = valor_inicial
    historico = []

    for mes in range(1, meses + 1):
        saldo = saldo * (1 + taxa_mensal / 100)
        saldo = saldo + aporte_mensal
        total_investido = total_investido + aporte_mensal

        historico.append({
            "mes": mes,
            "saldo": round(saldo, 2),
            "investido": round(total_investido, 2)
        })

    lucro = saldo - total_investido

    resultado = {
        "valor_final": round(saldo, 2),
        "total_investido": round(total_investido, 2),
        "lucro": round(lucro, 2),
        "historico": historico
    }

    return resultado


# --- Persistencia com JSON ---

def salvar_viagens(viagens):
    try:
        lista = []
        for v in viagens:
            lista.append({
                "pais": v.pais,
                "cidade": v.cidade,
                "orcamento": v.orcamento,
                "custo_aproximado": v.custo_aproximado,
                "clima": v.clima
            })

        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=2, ensure_ascii=False)

        print(f"Dados salvos em {ARQUIVO_DADOS}!")
    except Exception:
        print("Erro ao salvar os dados.")


def carregar_viagens():
    try:
        if not os.path.exists(ARQUIVO_DADOS):
            print("Nenhum dado salvo encontrado.")
            return []

        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)

        print(f"{len(lista)} viagem(ns) carregada(s)!")
        return lista
    except Exception:
        print("Erro ao carregar os dados.")
        return []
