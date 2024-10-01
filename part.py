import random
from datetime import datetime

if __name__ == '__main__':
    # creusa está comemorando seu aniversario sabe aniversario mais não sabe a quantidade de velas no bolo (lembrar idade)
   
    data_atual = datetime.now().year
    ano_nacimento = random.randint(data_atual - 80, data_atual)
    idade = data_atual - ano_nacimento

    print(f"Ano que ela nasceu: {ano_nacimento}")
    print(f"quantidade para idade: {idade}")
    print()


if __name__ == '__main__':
    dinheiro_em_real = random.randint(0, 10000)
    dinheiro_em_dolar = 5

    dinheiro_em_atual = dinheiro_em_real / dinheiro_em_dolar
    taxa_aufandeigara = (dinheiro_em_atual*60) /100
    
    print(f"valor qu ela possuia {dinheiro_em_real}")
    print(f"valor que ela tem {dinheiro_em_atual}")
    print(f"taxa alfandeigara apos {taxa_aufandeigara:.1f}")
    print()

def valor_final(emprestimo):
    montante = emprestimo * (1 + 0.20) ** 12
    return montante
if __name__ == '__main__':
    emprestimo = random.randint(100, 10000)
    parcelas_12 = emprestimo / 12
    valor = valor_final(emprestimo)
    print(f"tirado do banco: {emprestimo}")
    print(f"valor das parcelas: {parcelas_12:.2f}")
    print(f"valor final: {valor:.2f}")
meses_passados = 0 

while valor > 0:
    valor -= parcelas_12
    meses_passados += 1
print(f"total de meses {meses_passados}")
