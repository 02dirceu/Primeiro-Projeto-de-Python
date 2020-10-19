# Projeto desenvolvido de acordo com o site do python Brasil https://wiki.python.org.br/ListaDeExerciciosProjetos

# O projeto é o seguinte:
# Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários, #
# está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema,
# o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos usuários, e identificar os
# usuários com maior espaço ocupado. Através de um aplicativo baixado da Internet, ele conseguiu gerar o seguinte
# arquivo, chamado relatorio.txt

from usuario import Usuario         # importa a classe Usuario, a qual irá criar um objeto para cada usuário

def format_string (user, espaco, total, i):         # função que formata as strings exibidas
    percentage = espaco / total * 100
    return f'{i+1: <5}{user: <12}{espaco: >10.2f} MB{percentage: >18.2f}%\n'

relatorio = open(r'relatorio.txt', 'r')         # abre o arquivo txt em modo de leitura

usuarios = []                           # define uma lista para armazenar os usuarios
soma = 0                                # soma é o parâmetro que irá somar o espaço utilizado

for line in relatorio:                  # Lê o arquivo linha a linha e armazena os dados em um objeto
    nome, espaco = line.split()
    soma += float(espaco) / 1024 ** 2
    usuarios.append(Usuario(nome, espaco))  # Acrescenta cada objeto à lista usuarios

media = soma / len(usuarios)                # define a media de espaco ocupado

usuarios = sorted(usuarios, key=lambda usuario: usuario.espaco, reverse=True)   #Classifica os usuários por ordem de
                                                                                #espaço gasto

# variavel escopo é responsável por dar a saída do projeto
escopo = '''
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

{}

Espaço total ocupado: {:.2f} MB
Espaço médio ocupado: {:.2f} MB
'''

n = int(input('Entre com a quantidade de linhas que queira visualizar: '))      #Verifica quantos usuários devem ser exibidos
while n > len(usuarios):
    print('O número digitado ultrapassa a quantidade de usuários.')
    n = input('Entre com a quantidade de linhas que queira visualizar: ')

users = ''                      #formata as strings na lista usuários de acordo com a entrada do usuário
for i in range(n):
    users += format_string(usuarios[i].usuario,usuarios[i].espaco, soma, i)

print(escopo.format(users, soma, media))        #imprime os resultados na tela


