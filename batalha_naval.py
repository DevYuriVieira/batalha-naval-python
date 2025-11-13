import random

mapa = [["~", "~", "~"],
        ["~", "~", "~"],
        ["~", "~", "~",]]

linha_escolhida = random.randint(0, 2)
coluna_escolhida = random.randint(0 , 2)

chances = 3

def exibir_mapa(mapa):
    for linha in mapa:
        print(linha)

print("Seja bem-vindo a batalha naval !!")
exibir_mapa(mapa)

for i in range(3):
    linha_digitida = int(input("Digite um numero de linha de 0 a 2: "))
    coluna_digitada = int(input("Digite um numero da coluna de 0 a 2: "))
    if linha_digitida == linha_escolhida and coluna_digitada == coluna_escolhida:
        print("\nAbate !!!!!!!!\n")
        mapa[linha_digitida][coluna_digitada] = "O"
        break
    else:
        print("\nerrou ! Tente novamente !!!\n")
        mapa[linha_digitida][coluna_digitada] = "X"
        exibir_mapa(mapa)
        print("\n")

exibir_mapa(mapa)
mapa[linha_digitida][coluna_digitada] = "O"

       
        


        
