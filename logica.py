import random as ran

def lista_at():
    ini = ran.randint(1,101)
    final = ran.randint(1,101)
    tama = ran.randint(1, 101)


    return [ran.randint(ini,final +1) for _ in range(tama)]
lista = lista_at()
print(lista)
#if this page is executed with no errors, you have the "mysql.connector" module installed.


