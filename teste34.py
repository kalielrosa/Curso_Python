salario = float(input('Informe seu salário: '))
if salario > 1250:
	aumento = salario + (salario * (10 /100))
	print('O seu salário é de R${} reais e com um aumento de 10% passará a receber  R${} reais'.format(salario, aumento))
else:
	aumento = salario + (salario * (15 /100))
	print('\033[31mO seu salário era de R${} reais e com um aumento de 15% passará receber R${} reais'.format(salario, aumento))

