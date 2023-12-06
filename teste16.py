#print("===== Desafio 16 =====")
#import math
#a = float(input('Digite um número: '))
#print("A parte inteira do número {} é {} ".format(a, math.floor(a)))

print("===== Desafio 18 =====")
from math import cos, sin, tan
angulo = int(input("Digite o Ângulo: "))
cos = cos(angulo)
sen = sin(angulo)
tan = tan(angulo)
print("O Ângulo {0} possui o um cosseno {1}, seno {2} e hipotenusa {3}".format(angulo, cos, sen, tan))