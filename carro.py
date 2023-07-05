class Carro:
    def __init__(self, nome, marca, ano, veloc):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.veloc = veloc
        '''self é construtor'''

    def acelerar(self, acelera):
        self.veloc =self.veloc + acelera
        print(f'Velocidade atual acelerando {self.veloc}km/h')
        if self.veloc > 110:
            print(f'Multa!{self.veloc} km/h acimado permitido!')
            return

    def freiar(self, freiar):
        self.veloc =self.veloc - freiar
        print(f'Velocidade atual freiando {self.veloc}km/h')
        print(f'Velocidade freiando {self.veloc} km/h ')
        return