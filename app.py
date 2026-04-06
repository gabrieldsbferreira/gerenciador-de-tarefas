# Lista para armazenar tarefas
tarefas = []

while True:
print("\n--- GERENCIADOR DE TAREFAS ---")
print("1 - Adicionar tarefa")
print("2 - Concluir tarefa")
print("3 - Ver tarefas")
print("4 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
tarefa = input("Digite a nova tarefa: ")
tarefas.append(tarefa)
print("Tarefa adicionada com sucesso!")

elif opcao == "2":
if len(tarefas) == 0:
print("Nenhuma tarefa para concluir.")
else:
print("\nTarefas:")
for i, t in enumerate(tarefas):
print(f"{i} - {t}")

indice = int(input("Digite o número da tarefa concluída: "))
if 0 <= indice < len(tarefas):
tarefas.pop(indice)
print("Tarefa concluída!")
else:
print("Índice inválido.")

elif opcao == "3":
if len(tarefas) == 0:
print("Nenhuma tarefa pendente.")
else:
print("\nTarefas pendentes:")
for t in tarefas:
print(f"- {t}")

elif opcao == "4":
print("Encerrando o programa...")
break

else:
print("Opção inválida.")
