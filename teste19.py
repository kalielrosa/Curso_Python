print("===== Desafio 19 =====")
import random
a1 = input("1º aluno: ")
a2 = input("2º aluno: ")
a3 = input("3º aluno: ")
a4 = input("4º aluno: ")
a = [a1, a2, a3, a4]
sorteio = random.choice(a)
print("O professor escolheu o aluno(a) {}".format(sorteio))
