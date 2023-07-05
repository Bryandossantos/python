from calcular import *

horas_trab = input('Digite quantas horas foram trabalhadas: ')
valor_hora = input('Digite o valor por hora: ')

total_salario = calcular_pagamento(horas_trab, valor_hora)
print('O total do seu salário é de: ',total_salario)
