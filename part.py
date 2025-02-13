import os
import random as ran
from colorama import Fore, Style, Back

jogar_novamente = "s"
vit = False
jogador = 2
turno = 0
turno_max = 9
velha = [["" for _ in range(3)] for _ in range(3)]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def jogo():
    global velha, turno
    limpar_tela()
    print("   0   1   2")
    print(f"0: {velha[0][0] or ' '} | {velha[0][1] or ' '} | {velha[0][2] or ' '}")
    print("  ---+---+---")
    print(f"1: {velha[1][0] or ' '} | {velha[1][1] or ' '} | {velha[1][2] or ' '}")
    print("  ---+---+---")
    print(f"2: {velha[2][0] or ' '} | {velha[2][1] or ' '} | {velha[2][2] or ' '}")
    print(f"\n[Número de jogadas: {turno}]" + Fore.BLUE + Back.BLACK + Style.DIM)

def jogador_player():
    global jogador, turno
    if jogador == 2 and turno < turno_max:
        try:
            l = int(input("Linha....: "))
            c = int(input("Coluna...: "))
            while velha[l][c] != "":
                print("Posição já ocupada! Escolha outra.")
                l = int(input("Linha....: "))
                c = int(input("Coluna...: "))
            velha[l][c] = "X"
            jogador = 1
            turno += 1
        except (IndexError, ValueError):
            print("Entrada inválida! Tente novamente.")
            os.system("pause")

def jogador_pc():
    global turno, jogador
    if jogador == 1 and turno < turno_max:
        l, c = ran.randint(0, 2), ran.randint(0, 2)
        while velha[l][c] != "":
            l, c = ran.randint(0, 2), ran.randint(0, 2)
        velha[l][c] = "O"
        turno += 1
        jogador = 2

def vitoria_verificar():
    global velha
    for s in ["X", "O"]:
        # Verifica linhas e colunas
        for i in range(3):
            if all(velha[i][j] == s for j in range(3)) or all(velha[j][i] == s for j in range(3)):
                return s
        # Verifica diagonais
        if all(velha[i][i] == s for i in range(3)) or all(velha[i][2 - i] == s for i in range(3)):
            return s
    return None

# Loop principal do jogo
while jogar_novamente.lower() == "s":
    velha = [["" for _ in range(3)] for _ in range(3)]
    turno = 0
    jogador = 2
    vencedor = None

    while turno < turno_max and not vencedor:
        jogo()
        jogador_player()
        vencedor = vitoria_verificar()
        if vencedor or turno >= turno_max:
            break
        jogador_pc()
        vencedor = vitoria_verificar()

    jogo()

    if vencedor:
        print(f"Jogador '{vencedor}' venceu!")
    else:
        print("Empate!")

    jogar_novamente = input("Jogar novamente? (s/n): ")