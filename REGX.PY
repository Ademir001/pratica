import re
t = "Texto para rengal em python do curso de FBA de tudo de vai de texto"
pesq = input("Pesquisar: ")
se = re.findall(pesq, t)
print(se)
quant = len(se)
print("Qtde: " + str(quant))

res = re.search("rengal", t)
print("pesquisa rengal")

if (res != None):
    ri = res.start()
    rf = res.end()
    tam = rf - ri  
    print(res.start())
    print(res.end())
    print(tam)
else:
    print(res)
rese = re.split(r"\s",t)
print(rese)