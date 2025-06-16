nota = int(input("Digite a nota do aluno: "))

# Complete aqui com if, elif ou else
if nota >=9:
    print('muito bom, meus parabens :) ')
elif nota >=6:
    print('esta bonzinho poderia melhoraaaaaaaaar')
else:
    print('nota horrivel vc é muito burro')

def onemensager ():
    print('Olá mundo ')

def segmensager ():
    print('como voce esta {nome}')
def tercemensager ():
    print('empresa esta sem o seu {nome}')

onemensager()
segmensager()


frutas = ['uva', 'laranja', 'limão', 'pera', 'manga']
for indice, frutas in enumerate(frutas):
  print(f'{indice}: {frutas}')



while

contador = 1
while contador <=5:
    print('contando:', contador)
    contador +=1
senha = ''
while senha!='1234':
    senha = input('digite a senha: ')
print('Acesso liberado')

nomes = ['chris', 'liu', 'jax']
for nome in nomes:
    print('Olá', nome)
carros = []

for i in range(10):
    meus_carros = input(f'Digite o seu carro {i + 1}: ')
    carros.append(meus_carros)
print('Meus carros são: ', carros)
