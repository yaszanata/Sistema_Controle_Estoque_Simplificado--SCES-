##variáveis:
#coluna 0 - ID do Produto
#coluna 1 - Nome do Produto
#coluna 2 - Quantidade em Estoque 
#coluna 3 - Localização 

estoque = []
    

#funções:

def adicionar_produto():
    global estoque
    nome = input("Insira o nome produto: ")
    id = input("Insira o ID do produto: ")
    qntEstoque = input("Insira a quantidade do produto presente no estoque: ")
    localizacao = input("Insira onde se localiza o produto: ")

    estoque.append([id, nome, qntEstoque, localizacao])
    print("Produto registrado com sucesso!")

def lista_estoque():
    print("-------------ESTOQUE--------------")
    print()



##menu
    print("---------SISTEMA DE ESTOQUE--------")
while True: ##roda para sempre
   
    print("\n1- Adicionar produto\n2- Listar todos os produtos  \n3- Buscar produto por ID \n4- Atualizar estoque  \n5- Sair do programa")
    opcao = input("R: ")
    print("-----------------------------------") 
    

    if opcao == "1":
       adicionar_produto()

    elif opcao == "2":
        lista_estoque()