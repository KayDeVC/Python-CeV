import math
print('@.@ T R I G O N O M Ê T R I A @.@')
ang = float(input('Diga o valor do ângulo:'))
sen = math.sin(math.radians(ang))
print('O SENO do ângulo {} é igual á: {:.2f}.'.format(ang, sen))
cos = math.cos(math.radians(ang))
print('O COSENO do ângulo {} é igual á: {:.2f}.'.format(ang, cos))
tan = math.tan(math.radians(ang))
print('A TANGENTE do ângulo {} é igual á: {:.2f}.'.format(ang, tan))
