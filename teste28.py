import random

num = random.randint(0, 5)
usuario =  str(input("Você pensou no número: "))
if num == usuario:
    print("Você ganhou ! =)")
else:
    print("Você perdeu !!! =(")
    print("Eu pensei no número {} !".format(num))
