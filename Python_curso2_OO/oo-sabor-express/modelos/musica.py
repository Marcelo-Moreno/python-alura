'''
class Musica():
    nome = ''
    artista = ''
    # duracao = ''
    duracao = int

musica_classica = Musica()
musica_classica.nome = '9 Sinfonia'
musica_classica.artista = 'Beethoven'
musica_classica.duracao = 877
# musica_classica.duracao = '00:14:37'


musica_rock = Musica()
musica_rock.nome = 'Somos todos iguais'
musica_rock.artista = 'Banda Catedral'
musica_rock.duracao = 192
# musica_rock.duracao = '00:03:12'

musica_pop = Musica()
musica_pop.nome = 'Esperando na Janela'
musica_pop.artista = 'Cogumelo Plutão'
musica_pop.duracao = 238
# musica_pop.duracao = '00:03:58'

musicas = [musica_classica, musica_rock, musica_pop]

print(vars(musica_pop))
'''
# Nesta versão, utilizamos o método especial __init__ para inicializar os atributos da classe.
# A sintaxe do Python permite definir os atributos diretamente no construtor, tornando o código mais claro e legível.
# Lembrando: A simplicidade do Python nos permite criar
#            classes de maneira mais elegante e expressiva, facilitando a compreensão do código.

class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self): #self é a referência da instância que estamos usando naquele momento.
        return f'{self.nome} | {self.artista} | {self.duracao}'

musica1 = Musica(nome='9 Sinfonia', artista='Beethoven', duracao=877)
musica2 = Musica(nome='Somos todos iguais', artista='Banda Catedral', duracao=192)
musica3 = Musica(nome='Esperando na Janela', artista='Cogumelo Plutão', duracao=238)

print(musica3)