def calcular_troco(total_compra, valor_recebido):
    troco = valor_recebido - total_compra
    return troco

def calcular_notas_moedas(troco):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

    notas = {}
    for cedula in cedulas:
        if troco >= cedula:
            qtd_notas = troco // cedula
            notas[cedula] = qtd_notas
            troco -= qtd_notas * cedula

    troco = round(troco, 2)

    for moeda in moedas:
        if troco >= moeda:
            qtd_moedas = int(troco / moeda)
            notas[moeda] = qtd_moedas
            troco -= qtd_moedas * moeda

    return notas

def main():
    total_compra = float(input("Digite o valor total da compra: "))
    valor_recebido = float(input("Digite o valor recebido: "))

    troco = calcular_troco(total_compra, valor_recebido)

    if troco >= 0:
        print("Troco: R$", troco)
        notas_moedas = calcular_notas_moedas(troco)
        print("Notas e moedas a serem entregues como troco:")

        for nota_moeda, quantidade in notas_moedas.items():
            if nota_moeda >= 1:
                print("{} nota(s) de R$ {}".format(quantidade, nota_moeda))
            else:
                print("{} moeda(s) de R$ {}".format(quantidade, nota_moeda))
    else:
        print("Valor insuficiente. Faltam R$", abs(troco))

if __name__ == "__main__":
    main()