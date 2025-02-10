import requests
from bs4 import BeautifulSoup

# URL do site de notícias
url = "https://www.cnnbrasil.com.br/politica/"
res = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")

    # Encontrar os títulos das notícias (precisa inspecionar o site para saber a classe correta)
    titulos = soup.find_all("h2", class_="home__title")  # Substituir pela classe real do site

    print("📢 Títulos das notícias:")

    # Abrindo o arquivo no modo "a" (append) para não sobrescrever
    with open("noticias.txt", "w", encoding= "utf-8") as arquivo:
        with open("noticias.txt", "a", encoding="utf-8") as arquivo:
            for titulo in titulos:
                texto_titulo = titulo.text.strip()
                print(f"- {texto_titulo}")
                arquivo.write(texto_titulo + "\n")


    # Exibindo o conteúdo salvo
    with open("noticias.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("\n📄 Títulos registrados:")
        print(conteudo)

else:
    print("❌ Erro ao acessar o site. Código:", res.status_code)
