'''
Como já vimos, programação é prática! Criamos mais uma lista de atividades (não obrigatórias) para você exercitar e
reforçar ainda mais seu aprendizado e o conteúdo da vez são listas, blocos de repetição e try except. Bora praticar?

Exercícios
1 - Crie uma lista para cada informação a seguir:

- Lista de números de 1 a 10;
- Lista com quatro nomes;
- Lista com o ano que você nasceu e o ano atual.

2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

'''
# RESPOSTA PARA A QUESTÃO 1
lista_numeros = list(range(11))
lista_nomes = ['Anatoly', 'Iryna', 'Alexey', 'Alice']
lista_datas = ['1986', '2024']
lista_teste = []


print(type(lista_numeros))
print(type(lista_nomes))
print(type(lista_datas))
print()


# RESPOSTAS PARA A QUESTÃO 2
for elemento in lista_numeros:
    print(elemento)
print()

for nome in lista_nomes:
    print(nome)
print()

for ano in lista_datas:
    print(ano)
print()


# RESPOSTA PARA A QUESTÃO 3
soma_impares = 0
for elemento in lista_numeros:
   
    if elemento % 2 != 0:
        soma_impares = soma_impares + elemento
        print(elemento)
print('A soma dos elementos ÍMPARES é: ', soma_impares)
print()

# RESPOSTA DO PROFESSOR PARA A QUESTÃO 3
# O segundo argumento de da função range é exclusivo,
# então range(1, 11) inclui números de 1 a 10) com um passo de 2 (o terceiro argumento de range).
# Isso garante que apenas números ímpares sejam considerados.

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)


# RESPOSTA DO PROFESSOR PARA A QUESTÃO 4
for i in range(10, 0, -1):
    print(i)

# RESPOSTA DO PROFESSOR PARA A QUESTÃO 5

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")


# RESPOSTA DO PROFESSOR PARA A QUESTÃO 6
# Exception é uma classe base para todas as exceções em Python.
# Capturar Exception permite lidar com qualquer tipo de exceção que possa ocorrer no bloco try.
# O as e é opcional, mas é frequentemente usado para acessar informações detalhadas sobre a exceção, como mensagens de erro.
    
    lista_numeros = [10, 5, None, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# RESPOSTA DO PROFESSOR PARA A QUESTÃO 7
# ZeroDivisionError é uma exceção específica que ocorre quando há uma tentativa de divisão por zero.
# Este bloco except é destinado a lidar especificamente com esse tipo de erro.

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")