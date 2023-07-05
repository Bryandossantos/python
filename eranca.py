class Pessoa:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def nome(self):
        return self.__nome


class Cliente(Pessoa):
    def __init__(self, nome, cpf, limite):
        super().__init__(nome, cpf)
        self.__limite = limite

    def nome(self):
        return f'{super().nome()} Limite: {self.__limite}'


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.__matricula = matricula

    def matricula(self):
        return f'Matricula: {self.__matricula}'


func1 = Funcionario('Suele', '441.458.254.555-33', '52121345')
print(func1.nome())
print(func1.matricula())

'''cliente1 = Cliente('Samer Magaldi Almerindo', '855.748.995.87', 10000)

print(cliente1.nome())'''
