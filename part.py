import random as rs
import os

erros= 0 
sorteio = rs.randrange(0,100)
jogador = int(input("DIgite um numero "))


while(sorteio != jogador):
    os.system("cls")
    if (sorteio > jogador):
        print("Numero de valor maior")
    elif (sorteio < jogador):
        print("Numero de valor menor")
    erros += 1
    print(f"numero de erros ate agora {erros}")
    jogador= int(input("Escolha outro numero"))
print(f"Numero de erros é {erros} o numero sorteado foi {sorteio} igual a numero do jogador {jogador}") 
