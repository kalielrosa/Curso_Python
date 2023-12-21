velocidade = int(input("Informe a velocidade do carro: "))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print("Você foi Multado !")
    print("Você foi multado em R$ {:.2f}".format(multa))
else:
    print("Você está na velocidade permitida =)")