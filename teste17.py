print("===== Desafio 17 =====")
from math import hypot
co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))
tan = hypot(co, ca)
print("A Tangente é {:.2f}".format(tan))