#Crie uma classe Animal com os atributos nome e idade.
#Crie um método fazer_som() que imprime uma mensagem genérica.
#Crie duas classes filhas: Cachorro e Gato, que herdam de Animal.
#Sobrescreva o método fazer_som() nas classes filhas para imprimir
# sons específicos ("Au Au" para cachorro e "Miau" para gato).

#Cria Classe Animal:Nome e idade
class  Animal:
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, idade: {self.idade} anos")
        

#Crie um metodo fazer_som() que imprime uma mensagem generica.
    def fazer_som(self):
        print(f"Fazendo som de animal")

#Crie Cachorro e Gato, que herdam de animal.

class Cachorro(Animal):
#sobescreva o metodo fazer_som() nas classes filhas para imprimir
# sons epecificos ("AU AU" para cachorro e "Miau" para gato).
    def fazer_som(self):
        print(f"AU AU")

    
    def mostrar_dados(self):
        super().mostrar_dados()
        print("Tipo: cachorro")


class Gato(Animal):
    def fazer_som(self):
        print(f"MIAU")

    def mostrar_dados(self):
        super().mostrar_dados()
        print("Tipo: Gato")

#gato1 = Gato()
#gato1.fazer_som()
#gato1.mostrar_dados()

#cachorro1 = Cachorro()
#cachorro1.fazer_som()
#cachorro1.mostrar_dados()

#animal = Animal()
#animal.fazer_som()

#com input
nome = input("Digite o nome do animal:")
idade = int(input("Digite a idade do animal (em anos); "))
tipo = input("Digite o tipo do animal: (cachorro, gato ou animal)").strip().lower()

#Criar o objeto baseado no tipo
if tipo == "cachorro":
    animal = Cachorro(nome, idade)
elif tipo == "gato":
    animal = Gato(nome, idade)
else:
    animal = Animal(nome, idade)

animal.fazer_som()
animal.mostrar_dados()
