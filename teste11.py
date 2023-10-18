print('===== Desafio 1 =====')
largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura 
tinta = area / 2
print('A parede tem uma Área de {}'.format(area))
print('Você precisará de {:.2f} litros de tinta para pintar uma área de {:.2f} m²'.format(tinta, area)) 