#Calcular as notas e suas medias

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'Sua nota é: {media}')

if media >=9:
    print('Status: Excelente')
elif media >=6:
    print('Status: Bom')
else:
    print('Status: Horrivel estudar mais!')


