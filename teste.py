#24/05/2025
# Mostre para o usuario se o numero é Par ou Impar
# # Solicita ao usuário um número inteiro
# numero = int(input('Digite algum numero:  '))

# # TODO: Verifique se o número é par ou ímpar e imprima o resultado:
# if numero %2:
#   print('Ímpar')
# else:
#   print('Par')


# Mostre ao Usuario os anos que são Bissexto 
# def verificador_ano_bissexto():
#    ano = int(input('Digite um ano:  '))

# # TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:
#    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print("SIM")
#    else:
# #     print("NÃO")
# # verificador_ano_bissexto()


# #Mostre ao usuario a quatidade de vogais que tem uma palavra
# def conta_vogais(texto):
#     # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
#     vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#     # TODO: Inicialize um contador para contar as vogais:
#     contador = 0
    
#     # Iteramos pelos caracteres da string
#     for char in texto:
#         # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
#         if char in vogais:
#             contador += 1
    
#     return contador

# # Solicitamos ao usuário que insira uma string
# texto = input('Digite qualquer palavra:  ')

# # Chamamos a função conta_vogais e exibimos o resultado
# resultado = conta_vogais(texto)
# print(f"O número de vogais na string '{texto}' é: {resultado}")
# prova 4 For
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# Solicita os valores de início e fim do intervalo
primeiro = int(input("Digite o primeiro número do intervalo: "))
ultimo = int(input("Digite o ultimo número do intervalo: "))


som_par = 0
encontra_par = False

for numero in range(primeiro, ultimo + 1):
    if numero % 2 == 0:    #verifica se o numero será par
        som_par += numero
        encontra_par = True
else:
    if not encontra_par:
        print("Não há números pares no intervalo.")
    else:
        print(f"A soma dos números pares no intervalo é: {som_par}")

