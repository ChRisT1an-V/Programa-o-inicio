import os

#  Lista de consoles de videogame
consoles = [
    "PlayStation 5",
    "Xbox Series X",
    "Nintendo Switch",
    "PlayStation 4",
    "Xbox One",
    "Nintendo Wii",
    "PlayStation 3",
    "Xbox 360",
    "Super Nintendo",
    "Sega Genesis"
]

print("Lista de consoles de videogame:")
for console in consoles:
    print(f"- {console}")

print("\nArquivos e pastas no diretório atual:")

# Listando arquivos e pastas do diretório atual
diretorio_atual = os.getcwd()           # Obtém o diretório atual
itens = os.listdir(diretorio_atual)     # Lista os arquivos e pastas

for item in itens:
    print(f"- {item}")
