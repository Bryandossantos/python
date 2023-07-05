'''
x = 0
while x <= 50:
    print(x)
    #x += 1 forma de adicionar um pouco mais curta
    if x == 6:
        break
    x = x + 1
print('Fim do laço de repetição')

#calculadora em python
while True:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operador = input('Digite a operação')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número meu amigo!!!')
        continue
    num_1 = int(num_1)
    num_2 = int(num_2)
    #soma+ subtração- divisão/ multiplicação*
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador invalido')

    sair = input('Deseja sair?[S] Sim [N] Não')
    if sair == 'S':
        break
print('Você saiu da calculadora!')


for n in range(5):
    print(n)

for n in range(5, 20):
    print(n)


for n in range(5, 25, 3):
    print(n)

for n in range(20, 10, -1):
    print(n)

frutas = ["manga","melancia","morango",]
print(frutas[1])
for x in frutas:
    print(x)

procura = str(input('Digite a fruta procurada: '))
frutas = ["manga","melancia","morango","banana","kiwi","maracuja","cenoura"]
for x in frutas:
    if x == procura:
        print("Achou a fruta procurada",x)
        break
print('Pulou para fora do FOR')


Carro = ['Volksvagem', 'Gol', '2015', 'MLD8474', '1.8 16v', '4 Portas']
motoristas = ['João', 'pedro', 'Antonio', 'josemar']
frota = Carro + motoristas

frota.insert(6, 'banco de couro')
print(frota)
del(frota[7])
print(frota)
frota.pop()
print(frota)

frota.append('Bryan')
print(frota)
print(frota[-1])

Carro[1] = 'Virtus'
Carro[2] = '2022'
Carro[3] = 'MX08574'
print(frota)
print('Marca do carro:', Carro[0])
print('Modelo do carro:', Carro[1])
print('Ano do carro:', Carro[2])
print('Motorização do carro', Carro[-2])
print('Motorização do carro', Carro[4])
print('motorista:', frota[-3])
'''

Carro = ['Volksvagem', 'Gol', '2015']
marca, modelo, ano = Carro
print(marca)
print(modelo)
print(ano)
print(Carro)