menu = """
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

=> """

saldo = 0
limete = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == "d":
    #print("Deposito")
    valor = float(input("Informe o valor do deposito:"))
    if valor > 0:  # Regra 1 para saber se o valor do deposito é negativo
      saldo += valor
      extrato += f"Deposito: R${valor:.2f}\n"
    else:
      print("Operação falhou! O valor informado é invalido!")
  
  elif opcao == "s":
    #print("Saque")
    valor = float(input("Informe o valor do saque:"))
    
    excedeu_saldo = valor > saldo  #saber se tem saldo disponivel.
    
    excedeu_limite = valor > limete  #saber se excedeu o limite do saque de 500 reais.
    
    excedeu_saque = numero_saque >= LIMITE_SAQUES #Verificar se o usuário já realizou os 3 saques
    
    if excedeu_saldo:
      print("Operação falou! vc não tem saldo suficiente")
    
    elif excedeu_limite:
      print("Operação falou! o valor do saque excedeu o limete de 500 reais")
    
    elif excedeu_saque:
      print("Operação falhou, Numero maximo de saques excedido em mais de 3x.")
    
    elif valor > 0:
      saldo -= valor
      extrato += f"saque: R${valor:.2f}\n"
      numero_saque += 1
    
    else:
      print("Operação falhou! O valor informado é invalido.")

  elif opcao == "e":
    print("Extrato")
    print("\n=================== EXTRATO ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("\n=================== FIM =================")
  
  elif opcao == "q":
    break
  
  else:
    print("Operação invalida, por favo selecione novamente a operação desejada.")