# Sistema de Controle de Estoque Simplificado (SCES) 
## Menu interativo que ajuda na organização do estoque
Esse é um MENU interativo que, ao selecionar uma opção, permite adicionar produtos ao estoque informando a quantidade do item e a sua localização. Também é possível modificar a quantidade do produto no estoque a qualquer momento. Este projeto foi desenvolvido durante o curso do SENAI para praticarmos e trabalharmos com a linguagem Python.

### ESTOQUE:
- O estoque é organizado da seguinte forma:

**ID, Nome do produto, Quantidade no estoque, Localização**

### MENU
*Quando selecionado a opção 1:*
- Insira o nome do produto, caso ele já esteja cadastrado você será avisado; (`ex:Arroz`)
- Insira a quantidade desse produto no estoque, números negativos não são aceitos; (`ex: 65`)
- Adicione a localização do produto no estoque; (`ex: prateleira 2`)
- O ID é criado de forma automática.

*opção 2:*
- Será mostrado o estoque.

*opção 3:*
- Adicione o ID do produto que deseja procurar; caso o ID não exista você será avisado.

*opção 4:*
- Adicione o ID do produto que deseja alterar a quantidade no estoque; caso o ID não exista você será avisado;
- Insira a nova quantidade do item no estoque:
     * Se a quantidade for negativa ou zero o produto será excluído do estoque;
     * Se a quantidade digitada for positiva a quantidade do produto será alterada.

*opção 5:*
- Sairá do código.
