if __name__ == '__main__':
    l1 = int(input("tamanho do lado l1: "))
    l2 = int(input("tamanho do lado l2: "))
    l3 = int(input("tamanho do lado l3: "))
    def triangulo(l1,l2,l3):
        if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 +l2):
            return True
        else:
            return False
    def equilatero(l1,l2,l3):
        if (l1 == l2 ) and (l2 == l3):
            return True
        else:
            return False
    def escaleno(l1,l2,l3):
        if (l1 != l2) and (l2 != l3) and (l3 != l1):
            return True
        else:
            return False
    def isoceles(l1,l2,l3):
        if (l1 != l2) and (l1 != l3) or (l2 != l1) and (l2 != l3) or (l3 != l1) and (l1 == l2) or (l2 ==l3) or (l3 == l1):
            return True
        else:
            return False

    if triangulo(l1,l2,l3):
        if equilatero(l1,l2,l3):
            print("triangulo equilatero")
        elif escaleno(l1,l2,l3):
            print("triangulo escaleno")
        elif isoceles(l1,l2,l3):
            print("triangulo isoceles")
    else:
        print("não é um triangulo")