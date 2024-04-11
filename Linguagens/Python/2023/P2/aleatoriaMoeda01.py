import random

def simulacao_lancamento_moedas(semente):
    random.seed(semente)  # define a semente para gerar resultados consistentes

    premios = []  # lista para armazenar os prêmios obtidos

    for _ in range(100):  # simula 100 jogadas
        lancamentos = ""  # sequência de lançamentos
        n = 1  # número da jogada

        while True:
            lancamento = random.choice(["Cara", "Coroa"])  # escolhe aleatoriamente entre Cara e Coroa
            lancamentos += lancamento[0]  # adiciona a primeira letra do lançamento à sequência

            if lancamento == "Cara":
                premio = 2 ** n  # calcula o prêmio com base no número da jogada
                premios.append(premio)  # adiciona o prêmio à lista
                break

            n += 1  # incrementa o número da jogada

    media_premios = sum(premios) / len(premios)  # calcula a média dos prêmios

    return media_premios

# Entrada da semente
semente = int(input("Digite a semente: "))

# Executa a simulação e imprime a média dos prêmios
media = simulacao_lancamento_moedas(semente)
print("Média dos prêmios: R$", media)
