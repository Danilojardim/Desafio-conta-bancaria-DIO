#função para criar menu.
def menu(): 
    # Cria uma variável que armazena o texto do menu
    menu = """ 
    ================ MENU ================
    +\t[1] Novo Usuario                 +
    +\t[2] Criar Conta                  +
    +\t[3] Depositar                    +
    +\t[4] Sacar                        + 
    +\t[5] Extrato                      +
    +\t[0] Sair                         +
    ======================================
    """

    # 'input' exibe o menu para o usuário digitar algo
    # a opção digitardigitada será retornado pela função para onde foi chamada
    return input(menu)

#função para validar se o CPF já existe.
def validar_cpf(usuarios, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario  # CPF encontrado, retorna o usuario
    return False  # Se não encontrou, retorna False

#função para criar_usuario.
def criar_usuario(usuarios):
    
    #coleta de dados cpf e faz a conferencia na usuarios[] se ja existe o cpf. 
    cpf = input("Informe o CPF (somente número): ")
    if validar_cpf (usuarios, cpf):
        print("""\t===============================\n\t     Usuário já cadastrado!\n\t===============================""")
        return  # Sai da função sem adicionar
    
    #se nao tiver cadastro coleta nome, data de nascimento e endereço
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    # salva na usuarios[] os dados coletados
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("""\t===============================\n\t  Usuário criado com sucesso!\n\t===============================""")

#função para criar_conta.
def criar_conta(usuarios, contas, AGENCIA):
    cpf = input("Informe o CPF do usuário: ") #coleta cpf
    usuario = validar_cpf(usuarios, cpf) #valida se o cpf esta cadastrado dentro da lista usuarios[]
    
    if usuario: #se sim existe cadastro
        numero_conta = len(contas) + 1 #verefica se existe item e adciona mais 1
        conta = {
            "agencia": AGENCIA, #agencia e fixa na variavel AGENCIA
            "numero_conta": numero_conta, #adciona o nuemro da conta
            "usuario": usuario #usa o usuario retornado do validar_cpf
        }
        contas.append(conta) #gera o dicionario{} com as informações e armazena na lista conta[]
        print("\nConta criada com sucesso!")
        print(f"Agência: {AGENCIA}")
        print(f"Número da conta: {numero_conta}")
        print(f"Titular: {usuario['nome']}")
    else: #se não existe cadastro, solicita cadastro do mesmo
        print("""\t======================================================================\n\t Usuário não encontrado. Cadastre o usuário antes de criar uma conta.\n\t======================================================================""")

#função depositar dinheiro na conta.
def depositar(saldo, valor_a_depositar, extrato, /):
    if valor_a_depositar > 0: #verefica se o valor informado para deposito e maior que 0.
        saldo += valor_a_depositar #adciona o valor informado ao saldo.
        extrato += (f"Deposito\tR$ {valor_a_depositar:.2f}\n") #peaga os dados anterior salvao na variavel e adciona ao final quebrando linha a nova operação
        print(f"\t==================================================\n\t   Depósito de R$ {valor_a_depositar:.2f} realizado com sucesso! \n\t==================================================") #informa valor e sucesso da operacao de deposito.
    else:#caso seja menor ou zero
        print("\t===============================================================================\n\t  Operação falhou! O valor informado é inválido. Digite um valor maior que 0!\n\t===============================================================================")#informa que o valor é invalido
    return saldo, extrato #retorna os valores de saldo e extrato pra ambas variaveis

#função para fazer o saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo #verefica se valor do saque é maior que o saldo.
    excedeu_limite = valor > limite #verefica se o valor e maior que o limite de saque.
    excedeu_saques = numero_saques >= limite_saques #verefica o numero de saques feito e compara com o limite de saques.

    if excedeu_saldo:
        print("\t=====================================================\n\t   Operação falhou! Você não tem saldo suficiente.\n\t=====================================================")
    elif excedeu_limite:
        print("\t=====================================================\n\tOperação falhou! O valor do saque excede o limite permitido.\n\t=====================================================")
    elif excedeu_saques:
        print("\t=====================================================\n\t  Operação falhou! Número máximo de saques excedido.\n\t=====================================================")
    elif valor > 0:
        saldo -= valor
        extrato += (f"Saque:  \tR$ {valor:.2f}\n") #peaga os dados anterior salvao na variavel e adciona ao final quebrando linha a nova operação
        numero_saques += 1
        print(f"\t================================================\n\t  Saque de R$ {valor:.2f} realizado com sucesso!\n\t================================================")
    else:
        print("\t=====================================================\n\t   Operação falhou! O valor informado é inválido.\n\t=====================================================")

    return saldo, extrato, numero_saques #retorna os valores gerados que seram utilizdos como parametros

#função para gerar o extrato
def mostrar_extrato(saldo_conta,/, *, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Não foram realizadas movimentações.") #verefica se extrato esta vazio com o retorno logico true ou false.
    print(f"\nSaldo: R$ {saldo_conta:.2f}")
    print("=============================")


#funcao principal para executar e ordenar o sistema
def main():
    
    #numero de saques permitidos
    LIMITE_SAQUES = 3

    #como precisamos ter AGENCIA fixa setamos ela em variavel para reutlizar em varias contas
    AGENCIA = "0001"
    
    #criando uma lista vazia chamada usuarios.
    #vai armazenar todos os usuários criados, cada um sendo representado como um dicionário (dict).
    usuarios= []

    #criando uma lista vazia chamada contas.
    #vai armazenar todos as contas criadas e seu vinculo com um usuario, cada um sendo representado como um dicionário (dict).
    #representada assim conta[{"AGENCIA": "0001", "numero_conta": 1, "usuario": {"nome": "Danilo","cpf": "12345678900",.,.,.}}]
    contas= []

    #saldo da conta corrente inicia o sistema em zero
    saldo_conta = 0

    #extrato inicia vazio
    extrato = ""

    #valor limite de saque
    limite = 500

    #contadoe de saques efetuados
    numero_saques = 0

    #loop para controlar as funcoes e fazer o sistema funcionar
    while True:
        # Chamar a função para exibir o menu
        opicao=menu()

        #chama a opção 1 e traz a função responsavel pelo cadastro de novo usuario
        if opicao == "1":
            criar_usuario(usuarios)
        
        elif opicao == "2":
            criar_conta(usuarios, contas, AGENCIA)

        elif opicao == "3":
            valor_a_depositar = float(input("Informe o valor a ser depositado: "))
            saldo_conta, extrato = depositar(saldo_conta, valor_a_depositar, extrato)
        
        elif opicao == "4":
            valor = float(input("Informe o valor do saque: "))
            saldo_conta, extrato, numero_saques = sacar(
             saldo=saldo_conta,
             valor=valor,
             extrato=extrato,
             limite=limite,
             numero_saques=numero_saques,
             limite_saques=LIMITE_SAQUES)

        elif opicao == "5":
             mostrar_extrato(saldo_conta, extrato=extrato)

        


        #chama a opção 0 e traz a função responsavel por finalizar o sistema
        elif opicao == "0":
            print("""\t==========================\n\t  Saindo do sistema... 👋\n\t==========================""")
            break
        #responsalvel por avisar que a opção foi invalida e retornar ao menu incicial
        else:
            print("""\t==================================\n\t Opção inválida, tente novamente \n\t==================================""")
        
main()



