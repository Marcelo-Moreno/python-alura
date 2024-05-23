'''
Exercícios:

1- Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

2- Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

3- Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

4- Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

5- Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.


'''
#Questão 1
class Carro:

    def __init__(self, modelo, cor, ano): # Sabemos que um método é especial quando ele tem dois underlines, antes e depois. #
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def __str__(self): #self é a referência da instância que estamos usando naquele momento.
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
carro1 = Carro(modelo = 'Volvo XC60', cor = 'Cinza', ano = '2024')

print(carro1)

#Questão 2

class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante_exemplo = Restaurante(nome='Comida Boa', categoria='Gourmet', ativo=True, capacidade=500, nota_avaliacao=4.5)
restaurante2 = Restaurante(nome = 'Bom Sabor', categoria = 'Portuguesa', ativo = True, capacidade=30, nota_avaliacao=9.1)
print(restaurante2)


class Cliente:
    def __init__(self, nome='', idade=0, email='', telefone=''):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor

cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')