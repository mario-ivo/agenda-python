class Contato:
  def __init__(self, nome, telefone, email):
    self.nome = nome
    self.telefone = telefone
    self.email = email

class Agenda:
  def __init__(self):
    self.contatos = []

  def adicionar_contato(self, contato):
    self.contatos.append(contato)

  def remover_contato(self, nome):
    for i in range(len(self.contatos)):
      if self.contatos[i].nome == nome:
        del self.contatos[i]
        break

  def buscar_contato(self, nome):
    for contato in self.contatos:
      if contato.nome == nome:
        return contato
    return None

  def imprimir_agenda(self):
    for contato in self.contatos:
      print(f"Nome: {contato.nome}")
      print(f"Telefone: {contato.telefone}")
      print(f"Email: {contato.email}")
      print("-" * 20)

agenda = Agenda()

while True:
  print("1 - Adicionar contato")
  print("2 - Remover contato")
  print("3 - Buscar contato")
  print("4 - Imprimir agenda")
  print("5 - Sair")

  opcao = int(input("Digite a opção desejada: "))

  if opcao == 1:
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    agenda.adicionar_contato(Contato(nome, telefone, email))
  elif opcao == 2:
    nome = input("Digite o nome do contato a ser removido: ")
    agenda.remover_contato(nome)
  elif opcao == 3:
    nome = input("Digite o nome do contato a ser buscado: ")
    contato = agenda.buscar_contato(nome)
    if contato:
      print(f"Nome: {contato.nome}")
      print(f"Telefone: {contato.telefone}")
      print(f"Email: {contato.email}")
    else:
      print(f"Contato {nome} não encontrado.")
  elif opcao == 4:
    agenda.imprimir_agenda()
  elif opcao == 5:
    break
  else:
    print("Opção inválida.")

print("Agenda encerrada.")
