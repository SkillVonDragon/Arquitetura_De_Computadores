Produtos = int(input("Digite a quantidade de produtos que deseja cadastrar: "))
ProdSuficiente = ProdAlerta = ProdAbaixo = 0

for i in range(1, Produtos+1):
    Nome = input(f"Digite a digite o nome do {i}º produto: ")
    Estoque = int(input(f"Digite a quantidade que será adicionada ao estoque do {i}º produto: "))
    if Estoque >= 100:
        ProdSuficiente+=1
    elif Estoque >= 50:
        ProdAlerta+=1
    else:
        ProdAbaixo+=1;
        
print(f"A quantidade de produtos com nível suficiente no estoque é {ProdSuficiente}")
print(f"A quantidade de produtos com nível em estado de alerta no estoque é {ProdAlerta}")
print(f"A quantidade de produtos com nível em estado de falta no estoque é {ProdAbaixo}")
