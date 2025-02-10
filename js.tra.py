import os
import shutil


with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Correr\n")
    arquivo.write("Comer\n")
    arquivo.write("Andar\n")

print(" Arquivo 'tarefas.txt' criado com as tarefas iniciais!")


with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("\n📄 Tarefas registradas inicialmente:")
    print(conteudo)


nova_tarefa = input(" Escreva uma nova tarefa: ")
while True:
    nova_tarefa = input(" Escreva uma nova tarefa (ou digite 'sair' para parar): ").strip()
    
    if nova_tarefa.lower() == "sair":
        print(" Encerrando a adição de tarefas.")
        break
    
    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nova_tarefa + "\n")
    print(" Tarefa adicionada com sucesso!")
print(" Tarefa adicionada com sucesso!")


with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("\n Tarefas atualizadas:")
    print(conteudo)

