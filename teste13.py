print('===== Desafio 13 =====')
salario = float(input('Informe seu salário: '))
aumento = (15/100) * salario
novo_salario = salario + aumento
print('Seu salário de {:.2f} passará a ser de {:.2f} ápos um aumento de 15% !'.format(salario, novo_salario))