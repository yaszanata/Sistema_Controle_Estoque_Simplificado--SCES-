##variáveis:
#coluna 0 - ID do Produto
#coluna 1 - Nome do Produto
#coluna 2 - Quantidade em Estoque 
#coluna 3 - Localização 

estoque = []
    

#funções:

def adicionar_produto(): ##adicionar verificamento para não aceitar produtos repetidos!!!!
    global estoque
    nome = input("Insira o nome produto: ")
    nomeProcurada = -1

    for i in range(len(estoque)): #varre linha por linha na matriz
        if(estoque[i][1] == nome): #verifica se o nome já existe
            nomeProcurada = i
            
            print(f"Esse produto já está no estoque! {nomeProcurada}")
    
    id = input("Insira o ID do produto: ")
    for i in range(len(estoque)): #varre linha por linha na matriz
            if(estoque[i][1] == id): #verifica se o id já existe
                idProcurada = i
                
                print(f"Esse ID já  foi cadastrado no estoque! {idProcurada}")

    qntEstoque = input("Insira a quantidade do produto presente no estoque: ")
    localizacao = input("Insira onde se localiza o produto: ")

    estoque.append([id, nome, qntEstoque, localizacao])
    print("Produto registrado com sucesso!")

def lista_estoque():
    print("-------------ESTOQUE--------------")
    print()

def buscar_produto():
    global id
    produtoProcurado = input("Insira o ID do produto que deseja procurar: ")
    colunaProcurada = -1

    for i in range(len(estoque)): #varre linha por linha na matriz
        if(estoque[i][0] == produtoProcurado): #verifica se a posição do id é igual ao id procurado
            colunaProcurada = i


##menu
    print("\n---------SISTEMA DE ESTOQUE--------")
while True: ##roda para sempre
   
    print("\n1- Adicionar produto\n2- Listar todos os produtos  \n3- Buscar produto por ID \n4- Atualizar estoque \n5- Remover produto do estoque  \n6- Sair do programa")
    opcao = input("R: ")
    print("-----------------------------------") 
    

    if opcao == "1":
       adicionar_produto()

    elif opcao == "2":
        lista_estoque()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        print("")