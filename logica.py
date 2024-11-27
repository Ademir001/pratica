from string import ascii_letters, digits, punctuation
import random as rn

# Conjunto de caracteres disponíveis
characters = ascii_letters + digits + punctuation

# Tamanho da senha
password_length = 8

# Calcula o número total de combinações possíveis
total_combinations = len(characters) ** password_length
print(f"Total de combinações possíveis: {total_combinations}")


if __name__ == '__main__':
    def soma(lista):
        return sum(num for num in lista if num % 2 == 0)
print(soma([1,2,3,4,5,6,7,8,9,10]))

if __name__ == '__main__':
    def palindro(frase):
        frase = frase.replace(" ","").lower()
        return frase == frase[::-1]
print(palindro("A base do teto desaba"))

print(rn.randrange(1,10))
class perso:
    def __init__(car, age, name):
        car.age = age
        car.name = name
        
p1 = perso(43, "Rzober")
print(p1.age)
print(p1.name)






