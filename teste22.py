nome = str(input("Digite seu Nome: "))
#todas letras maiúsculas 
print(nome.upper())
#todas as letras minúsculas
print(nome.lower())
#mostra quantas letras  tem sem espaços
print(len(nome) - nome.count(' '))
#quantas letras tem o primeiro nome
nome = nome.split()
print(len(nome[0]))