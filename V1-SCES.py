##variáveis:
#coluna 0 - ID do Produto
#coluna 1 - Nome do Produto
#coluna 2 - Quantidade em Estoque 
#coluna 3 - Localização 

estoque = [
    [0, "Arroz", 34, 1], 
    [1, "Uva", 12, 2], 
    [2, "Morango", 5, 9], 
    [3, "Feijão", 23, 1], 
           ]
id = 3 

#funções:
def travarMenu():
    input("\nPressione <ENTER> para continuar...")

#1
def adicionar_produto():
    global estoque
    global id 

    nome = input("Insira o nome produto: ")
    nomeProcurado = -1

    for i in range(len(estoque)): #varre linha por linha na matriz
        if(estoque[i][1] == nome): #verifica se o nome já existe
            nomeProcurado = i
            print(f"Esse produto já está no estoque!")

    if nomeProcurado == -1: 
        id = id + 1
        qntEstoque = int(input("Insira a quantidade do produto presente no estoque: "))
        localizacao = input("Insira onde se localiza o produto: ")

        estoque.append([id, nome, qntEstoque, localizacao])
        print("Produto registrado com sucesso!")

    travarMenu()

#2
def lista_estoque():
    print("-------------ESTOQUE--------------")
    for linha in estoque:
        print(linha)

    travarMenu()

#3
def buscar_produto():
    global id
    produtoProcurado = int(input("Insira o ID do produto que deseja procurar: "))
    colunaProcurada = -1

    for i in range(len(estoque)): 
        if(estoque[i][0] == produtoProcurado): #verifica se a posição do id é igual ao id procurado
            colunaProcurada = i
            
            print(f"\nO ID {produtoProcurado} procurado está na linha {colunaProcurada}")
            print(estoque[i])
            break
    
    if colunaProcurada == -1:
        print("O ID procurado não está registrado!")

    travarMenu()

#4
def atualizarQNTproduto():
    global qntEstoque
    global estoque
    produtoProcurado = -1
    qntEstoque = 0

    id = int(input("Insira o ID que deseja alterar a quantidade do estoque: "))

    for i in range(len(estoque)): 
        if(estoque[i][0] == id):
            produtoProcurado = i
            novaqnt = int(input("Insira a nova quantidade presente no estoque: "))

            if novaqnt <= 0: #exclui o produto
                estoque.pop(produtoProcurado)
                print("O produto foi excluído do estoque!")

            else:
                estoque[i][2] = (novaqnt)
                print(f"Quantidade do ID{id} redefinido para: {novaqnt} ")
                    
    if produtoProcurado == -1: ##confirma que o ID no existe
        print("Produto não cadastrado!")
        

    travarMenu()
    

##menu
    print("\n---------SISTEMA DE ESTOQUE--------")
while True: ##roda para sempre
   
    print("\n1- Adicionar produto\n2- Listar todos os produtos  \n3- Buscar produto por ID \n4- Atualizar quantidade do produto no estoque \n5- Sair do programa")
    opcao = input("R: ")
    print("-----------------------------------\n") 
    

    if opcao == "1":
       adicionar_produto()

    elif opcao == "2":
        lista_estoque()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        atualizarQNTproduto()

    elif opcao == "5":
       print("Você saiu do estoque")
       break