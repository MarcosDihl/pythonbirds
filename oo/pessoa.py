class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return  f'Olá {id(self)}'


if __name__ == '__main__':
    marcos = Pessoa(nome='Marcos')
    dihl = Pessoa(marcos, nome='Dihl')
    print(Pessoa.cumprimentar(dihl))
    print(id(dihl))
    print(dihl.cumprimentar())
    print(dihl.nome)
    print(dihl.idade)
    for filho in dihl.filhos:
        print(filho.nome)

    print(dihl.filhos)