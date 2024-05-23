'''
2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.


'''

pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}


# Atualização de Idade
pessoa['idade'] = 31

# Adicionando Profissão
pessoa['profissao'] = 'Engenheiro'

# Remoção de Elemento
del pessoa['cidade']


for atributos in pessoa.values():
    print(atributos)

for atributos in pessoa.items():
    print(atributos)

for atributos, valor in pessoa.items():
    print(valor)