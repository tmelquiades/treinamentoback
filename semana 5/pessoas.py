'''
Crie uma classe "Pessoa" com os atributos nome e idade, 
e um método para imprimir essas informações na tela.
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar_info(self):
        return f'Olá, me chamo {self.nome} e tenho {self.idade} anos.'