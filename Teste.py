alor=float(input("Digite o valor da casa:"));
salario=float(input("Digite o salário:"))
anos=input("Quantos anos para pagar:")
meses = anos * 12
prestacao = valor/meses
if prestacao > salario * 0.3:
    print(f"Infelizmente você não pode obter o empréstimo")
else :
    print(f"fValor da prestação: R$ {prestacao:.2f} Empréstimo OK" )
