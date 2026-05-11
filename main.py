"""
Simulador de ATM (cash dispenser)

UNICSUL - 2026 | Programaçao de Computadores

Desenvolvido por:
Matheus Souza Anselmo | Engenharia de Software
------
Aplicar conhecimentos de algoritmos utilizando estruturas de controle de fluxo e estruturas de
dados básicas para modelar e simular comportamentos computacionais no desenvolvimento do
simulador de cash dispenser de ATM.
"""

from datetime import datetime as dt

import os, re, math

# Ok
def LimparTela():
  os.system('cls' if os.name == 'nt' else 'clear')

# Ok
def Continuar():
  input("\nPressione ENTER para continuar...")

# Lista de objetos representando os tipos de moedas, suas quantidades e seu valor de referência - quantidade começa em 0
caixa = [
  { "valor": 100, "qtd": 10 },
  { "valor": 50, "qtd": 10 },
  { "valor": 20, "qtd": 10 },
  { "valor": 10, "qtd": 10 }
]

# Ok
def ExibirMenu(opcoes):
  while True:
    print(f"""\nUNICSUL - Simulador de Saque de ATM - versão 2026 | {dt.now().strftime("%d/%m/%Y")}\n
  Menu:
  0 - Mostrar quantidade de notas disponíveis de cada valor
  1 - Abastecer ATM com quantidade de notas para cada valor
  2 - Sacar dinheiro no ATM
  9 - Sair\n""")
    
    entrada = input("Digite uma opção: ")

    if entrada in (opcoes):
      return entrada
    else:
      print("\nOpção inválida, digite uma das opções do menu!")
      input("Pressione ENTER para limpar a tela e continuar...")
      LimparTela()

def MostrarQtdNotas():
  LimparTela()

  total = 0
  print(f"\nQuantidade de notas disponíveis atualizada | {dt.now().strftime("%d/%m/%Y")} - {dt.now().strftime("%H:%M")}\n")
  for i in range(len(caixa)):
    print(f"Notas R$ {caixa[i]["valor"]}: {caixa[i]["qtd"]}")
    total += caixa[i]["valor"] * caixa[i]["qtd"]
  
  print(f"\nTotal em caixa: R$ {total}")

# Ok
def AbastecerATM():
  LimparTela()

  print("\nAbastecimento de ATM\n")

  for i in range(len(caixa)):
    question = True
    while question:
      valor = input(f"Notas R$ {caixa[i]["valor"]}: ").strip()

      if re.fullmatch(r"\d+", valor):
        caixa[i]["qtd"] += int(valor)
        question = False
      elif valor == "":
        question = False
      else:
        print("\nValor inválido!")
        Continuar()
        print()
  print(f"\nATM abastecido em {dt.now().strftime("%d/%m/%Y")} às {dt.now().strftime("%H:%M")}")

# Ok
def SacarDinheiro():
  LimparTela()

  question = True

  while question:
    saque = input("\nInforme o valor do saque: R$ ").strip().replace(',', '.')
    
    if saque == "" or re.fullmatch(r"^0([.,]0+)?$", saque):
      print("\nCampo vazio! É necessário informar um valor")
      Continuar()
    elif re.fullmatch(r"\d+(\.\d{1,2})?", saque):
      saque_float = float(saque)
      if saque_float % 10 != 0: 
        print("\nValor inválido para saque!")
        Continuar()
      else:
        question = False
    else:
      print("\nFormato inválido! É necessário informar um valor numérico")
      Continuar()

  notas_usadas = [
    { "valor": 100, "qtd": 0 },
    { "valor": 50, "qtd": 0 },
    { "valor": 20, "qtd": 0 },
    { "valor": 10, "qtd": 0 }
  ]

  resto = saque_float

  for nota in range(len(caixa)):
    ideal = math.floor(resto / caixa[nota]["valor"])
    minimo = min(ideal, caixa[nota]["qtd"])
    resto -= (minimo * caixa[nota]["valor"])
    notas_usadas[nota]["qtd"] += minimo
    
  if resto == 0:
    for nota in range(len(caixa)):
      caixa[nota]["qtd"] -= notas_usadas[nota]["qtd"]
      print(f"Saque de notas R$ {caixa[nota]["valor"]}: {notas_usadas[nota]["qtd"]}")
    print("\nSucesso ao realizar saque!")
  else:
    print("\nSaque impossível de realizar, quantidade em caixa insuficiente")
  
opcoes = ("0", "1", "2", "9")
running = True

while running:
  entrada = ExibirMenu(opcoes)
  # entrada = ValidarEntrada(opcoes)

  # Mostrar a quantidade de notas do ATM
  if entrada == "0":
    MostrarQtdNotas()
    Continuar()
    LimparTela()

  # Abastecer ATM
  elif entrada == "1":
    AbastecerATM()
    Continuar()
    LimparTela()

  # Sacar dinheiro do ATM
  elif entrada == "2":
    SacarDinheiro()
    Continuar()
    LimparTela()
    
  elif entrada == "9":
    running = False
    print("\nSimulador encerrado, até logo!\n")
