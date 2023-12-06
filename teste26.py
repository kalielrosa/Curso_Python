frase = str(input("Digite uma frase: ")).upper()
print("Quantas vezes aparece a letra A {}".format(frase.count("A")))
print("Posição que aparece pela primeira vez {} ".format(frase.find("A")))
print("Posição que aparece pela última vez {}".format(frase.rfind("A")))