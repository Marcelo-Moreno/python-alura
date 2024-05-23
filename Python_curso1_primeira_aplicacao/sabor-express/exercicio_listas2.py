'''
Imagine que você é um desenvolvedor na Hermex Log, uma empresa de logística especializada em serviços de entrega.
Sua tarefa é criar um sistema para gerenciar as encomendas, onde cada encomenda deve ser armazenada em uma lista.
Durante o desenvolvimento, você percebe a importância de validar as entradas no sistema para evitar interrupções inesperadas devido a erros de dados.

Considerando o contexto apresentado,
qual trecho de código Python representa corretamente a criação de uma lista de encomendas
e a iteração segura sobre ela, tratando possíveis erros de entrada?
'''

encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda))
except ValueError:
    print("Uma das entradas não é um número válido.")