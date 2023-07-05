def calcular_pagamento(qtd_horas, valor_horas):
    horas = float(qtd_horas)
    valorhoras = float(valor_horas)

    if horas <= 44:
        salario = horas * valorhoras
    else:
        extra = horas - 44
        salario = (44 * valorhoras) + (extra * (valorhoras * 1.5))

    return salario