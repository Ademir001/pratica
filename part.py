import os
import random as ran
from colorama import Fore, Style, Back

jogar_nomevamente = "s"
vit = False
jogador = 2
turno = 0
turno_max = 9
velha = [
    ["","",""],
    ["","",""],
    ["","",""]
]
def jogo():
    global velha
    global turno
    os.system("cls s    ")
    turno += 1
    print( "0    1   2")
    print(f"0: {velha[0][0]} | {velha[0][1]} | {velha[0][2]}")
    print("..............................")
    print(f"1: {velha[1][0]} | {velha[1][1]} | {velha[1][2]}")
    print("..............................")
    print(f"2: {velha[2][0]} | {velha[2][1]} | {velha[2][2]}")
    print("..............................")
    print(f"[Número de jogadas: {str(turno)}]" + Fore.BLUE + Back.BLACK + Style.DIM)

def jogador_player():
    global jogador
    global turno
    global turno_max
    global vit 
    if jogador == 2 and turno < turno_max:
        l = int(input("Linha....:"))
        c = int(input("Coluna...:"))
        try:
            while velha[l][c] != "":
                l = int(input("Linha....:"))
                c = int(input("Coluna...:"))
            velha[l][c] = "X"
            jogador = 1
            turno += 1
        except:
            print("Linha e coluna invalida ")
            os.system("pause")

def jogador_pc():
    global turno
    global turno_max
    global jogador
    if jogador == 1 and turno < turno_max:
            l = ran.randrange(0,3)
            c = ran.randrange(0,3)
            while velha[l][c] != "":
                l = ran.randrange(0,3)
                c =ran.randrange(0,3)
                velha[l][c] = "O"
                turno += 1
                jogador= 2

def vitoria_verificar():
    global velha
    vitoria = False
    simbo = ["X","O"]
    for s in simbo:
        vitoria = False
        il=ic=0
        while ic <3:
            soma=0
            il=0
            while ic<3:
                if(velha[il][ic]==s):
                    soma += 1
                ic+=1 
            if(soma==3):
                vitoria = True
                break
            il+=1
        if(vitoria != "n"):
            break

          
for i in range(turno_max):
    jogo()
    jogador_player()
    jogador_pc()
