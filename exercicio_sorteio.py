
import random

aluno1= input("Primeiro aluno: ")
aluno2= input("Segundo aluno: ")
aluno3= input("Terceiro aluno: ")
aluno4= input("Quarto aluno: ")

Lista= [aluno1, aluno2, aluno3, aluno4]

escolha= random.choice(Lista)

print('-----------------------------''\n''Resultado do sorteio foi :', escolha, '\n''-----------------------------')