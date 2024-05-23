class Restaurante:    
    restaurantes = []


    def __init__(self, nome, categoria): # Sabemos que um método é especial quando ele tem dois underlines, antes e depois. #
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)


    def __str__(self): #self é a referência da instância que estamos usando naquele momento.
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()

# restaurantes = [restaurante_praca, restaurante_pizza]
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))

# print(restaurante_praca)
# print(restaurante_pizza)
# Quando substítuimos o dir() por var(), queremos um dicionário desses atributos e métodos.
# print(vars(restaurante_praca)) # O VARS define todas as variáveis e os atributos de um objeto.
# print(dirs(restaurante_praca)) # O DIRS mostra tudo que já nasce com um determinado objeto (ao definirmos com a palavra "class").