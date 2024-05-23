'''
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

'''


pessoa = {'nome':'Marcelo', 'Idade': 38, 'Time do coração': 'Fluminense', 'Religião':'Protestante', 'Estado Civil':'Casado'}
print (pessoa['Estado Civil'])

for atributos in pessoa.values():
    print(atributos)

for atributos in pessoa.items():
    print(atributos)

for atributos, valor in pessoa.items():
    print(valor)