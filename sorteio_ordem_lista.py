import random

n1= input("Primeira Pessoa : " )
n2= input("Segunda pessoa: ")
n3= input("Terceira pessoa: ")

Lista= [n1, n2, n3]

Ordem_ale= random.shuffle(Lista)

print('A ordem é:', Lista)