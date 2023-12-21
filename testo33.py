n1 = int(input("1º número: "))
n2 = int(input("2º número: "))
n3 = int(input("3º número: "))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

menor = n1 
if n2 < n1 and n2 < n3:
    menor = n2
elif n2 < n1 and n3 < n2:
    menor = n3

print("Menor {}".format(menor))
print("Maior {}".format(maior))