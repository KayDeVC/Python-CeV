print('\n \33[1;32m====== PROJETO MÉDIA 2.0 ======\33[m')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('\nSua média é {:.1f}'.format(media))
if media < 5:
    print('\n\33[1;31mALUNO REPROVADO!\33[m')
elif 5 <= media < 7:
    print('\n\33[33mAluno em recuperação!\33[m')
else:
    print('\n\33[1;32mALUNO APROVADO!\33[m')
