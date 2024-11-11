
if __name__ == '__main__':
    def soma(lista):
        return sum(num for num in lista if num % 2 == 0)
print(soma([1,2,3,4,5,6,7,8,9,10]))

if __name__ == '__main__':
    def palindro(frase):
        frase = frase.replace(" ","").lower()
        return frase == frase[::-1]
print(palindro("A base do teto desaba"))


