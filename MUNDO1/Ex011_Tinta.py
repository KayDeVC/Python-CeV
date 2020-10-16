print('=====QUANTO DE TINTA?=====')
alt = float(input('Qual a altura da parede?'))
lar = float(input('Qual a largura da parede?'))
area = alt*lar
print('A área da parede é de {:.2f}m²!'.format(area))
print('Serão necessários {} litros de tinta para pintar a parede'.format(area/2))