#import classes as cl
from classes import *

if __name__ == '__main__':
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    email = input('Informe a e-mail:')

    #instancia a classe
    usuario = Pessoa(nome,idade,email)
    #saida de dados

    print(f'\nNome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'E-mail: {usuario.email}')