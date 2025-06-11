
DICA PARA DIFERENCIAR O WHILE COM O FOR
usamos o for, quando sabemos a quantidade de vezes que algo deve se repetir
usamos while quando não sabemos a quantidade de vezes que algo deve se repetir

1
peça ao usuário para inserir o preço de um produto e aplique 5% de desconto.

preco = float(input("Digite o preço do produto: "))

if preco > 0:
    desconto = preco * (5 / 100)
    preco -= desconto
    print(f"\n Preço com 5% de desconto: R$ {preco:.2f}")
else:
    print(" Preço inválido. Digite um valor maior que zero.")

2
solicite ao usuario um numero e use o operador de atribuição *= para dobrar o valor e exibir o resultado.

x = int(input('Digite um numero: '))
x *=2
print(x)

//
# 3
peça para o usuário se ele é maior de idade para obter a habilitação e quanto tempo de duração para fazer a renovação.

idade = int(input('Digite sua idade: '))
if idade>=65:
    print('Autorizado ter a habilitação, e sua renovação é de 5 em 5 anos')
elif idade>=18:
    print('Autorizado ter a habilitação, e sua renovação é de 10 em 10 anos')
else:
    print('Não autorizado, vai pegar onibus :D')
# //
4
peça ao usuario e:
mostre numero grande, se o numero for maior que 100, caso contrario, mostre 'numero pequeno'

numero = int (input('digite algum numero: '))
if numero >100:
    print('numero grande')
else:
    print('numero pequeno')
//

5
Verificação de Notas Aprovadas:
Escreva um programa que peça duas notas de um aluno. Use operadores
lógicos para verificar se as duas notas são maiores ou iguais a 7.

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
media = (nota1 + nota2) / 2

if media >=7:
    print('Aprovado')
elif media >=4:
    print('Reprovado, ficou de recuperação.')
else:
    print('Reprovado')
print(f'Sua nota é {media}')
//
6 peça para o usuario colocar apenas uma letra e definir se é consoante ou vogal a letra.
letra = input ('Digite uma letra: ')
if letra == 'a' or letra == 'e' or letra =='i' or letra =='o' or letra =='u':
    print('vogal')
else:
    print('Consoante')


//
7
Par ou impar

x = int(input('Digite um numero: '))

if x %2:
    print('Impar')
else:
    print('Par')

//
8
JOGO DA ADIVINHAÇÃO
numero_fixo = 7
tentativas = 0
max_tentativas = 3

print("Jogo da Adivinhação!")
print(f"Tente adivinhar um número de 1 até . Você tem {max_tentativas} tentativas.")

while tentativas < max_tentativas:
    tentativa = int(input("Digite um numero: "))
    tentativas += 1

    if tentativa == numero_fixo:
        print("Parabéns! Você acertou o número! :) ")
        break
    else:
        print("Errou! Tente novamente.")

if tentativa != numero_fixo:
    print("Perdeu! Acabou suas tentativas :( ")
    print(f"O número correto era {numero_fixo}")
