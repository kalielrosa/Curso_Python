print("===== Desafio 18 =====")
from math import cos, sin, tan
angulo = int(input("Digite o Ângulo: "))
cos = cos(angulo)
sen = sin(angulo)
tan = tan(angulo)
print("O Ângulo {0} possui o um cosseno {:.2f}, seno {:.2f} e hipotenusa {:.2f}".format(angulo, cos, sen, tan))