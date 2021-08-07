class Animal(object):

    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        raise NotImplementedError

    def comer(self):
        print(f'{self.nome} Está se alimentando')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        print(f'{self.nome} Miau....')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        print(f'{self.nome} Latido...')



class Ratazana(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        print(f'{self.nome} Faz grunhido')

class Cavalo(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def som(self):
        print(f'{self.nome}, sai correndo...')


Gatinho = Gato('Gatinho')
Gatinho.comer()
Gatinho.som()
Dog = Cachorro('Dog')
Dog.comer()
Dog.som()
Ratazana = Ratazana('Rato')
Ratazana.comer()
Ratazana.som()
Cavalo = Cavalo('cavalinho')
Cavalo.comer()
Cavalo.som()