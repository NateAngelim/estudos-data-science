print("Bem-vindo ao Simulador de Caixa!")
print("1 para acessar o caixa eletrônico, 2 para pedir extratos, 3 para efetuar pagamentos, 4 para sair, 0 para sair")
opcao = int(input("Digite a opção desejada: ")) 
while opcao != 0:
    if opcao == 1:
        print("Acessando o caixa eletrônico...")
    elif opcao == 2:
        print("Pedindo extratos...")
    elif opcao == 3:
        print("Efetuando pagamentos...")
    elif opcao == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
    opcao = int(input("Digite a opção desejada: ")) 