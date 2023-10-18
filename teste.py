n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, soma))

n = input('Digite Algum: ')
#qual é o tipo
print(type(n))
#é um número 
print(n.isnumeric())
#é uma letra
print(n.isalpha())
#é maiúsculo
print(n.isupper())
#é minúsculo
print(n.islower())
#tem espaco
print(n.isspace())