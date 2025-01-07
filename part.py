import os 
import random as rn
from colorama import Fore, Style, Back

players = 2
vitoria = False
turno_Max = 9
turno = 0
velha = [
    ["","",""],
    ["","",""],
    ["","",""],
]
def tela():
    global velha
    global turno
    os.system("cls")
    print("0    1   2")
    print(f"0:  {velha[0][0]} | {velha[0][1]} | {velha[0][2]}")
    print("------------------------------")
    print(f"1:  {velha[1][0]} | {velha[1][1]} | {velha[1][2]}")
    print("------------------------------")
    print(f"2:  {velha[2][0]} | {velha[2][1]} | {velha[2][2]}")
    print("------------------------------")
    print("jogadas: " + Fore.GREEN+str(turno)+ Fore.RESET )

while True:
    tela()