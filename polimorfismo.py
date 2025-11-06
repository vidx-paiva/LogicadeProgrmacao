class Carro:
    def acelerar(self):
        print("O carro está acelerndo de forma padrão.")

class CarroEsportivo(Carro):
    def acelerar(self):
        print("O carro esportivo acelera muito rápido!")

#criando objetos
carro_comum = Carro()
carro_espotivo = CarroEsportivo() 

#chamando metodo acelerar
carro_comum.acelerar()
carro_espotivo.acelerar()