##variáveis:
#coluna 0 - ID do Produto
#coluna 1 - Nome do Produto
#coluna 2 - Quantidade em Estoque 
#coluna 3 - Localização 

estoque = [
    [0, "arroz", 33, 12]
]
id = 0  

#funções:
def travarMenu():
    input("\nPressione <ENTER> para continuar...")
    
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


def lista_estoque():
    print("-------------ESTOQUE--------------")
    for linha in estoque:
        print(linha)

    travarMenu()

def buscar_produto():
    global id
    produtoProcurado = input("Insira o ID do produto que deseja procurar: ")
    colunaProcurada = -1

    for i in range(len(estoque)): 
        if(estoque[i][0] == produtoProcurado): #verifica se a posição do id é igual ao id procurado
            colunaProcurada = i
            print(f"\nO ID {produtoProcurado} procurado está na linha {colunaProcurada}")

        else:
            ("O ID procurado não está registrado!")

    travarMenu()




##menu
    print("\n---------SISTEMA DE ESTOQUE--------")
while True: ##roda para sempre
   
    print("\n1- Adicionar produto\n2- Listar todos os produtos  \n3- Buscar produto por ID \n4- Atualizar quantidade do produto no estoque \n5- Remover produto do estoque  \n6- Sair do programa")
    opcao = input("R: ")
    print("-----------------------------------\n") 
    

    if opcao == "1":
       adicionar_produto()

    elif opcao == "2":
        lista_estoque()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        print("")