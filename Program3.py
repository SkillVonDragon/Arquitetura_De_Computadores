Pessoas = int(input("Digite o número de pessoas: "))
abaixo_peso = peso_normal = sobrepeso = obesidade_1 = obesidade_2 = obesidade_3 = 0

for i in range(Pessoas):
    print(f"\nPessoa {i + 1}:")
    peso = float(input("Digite o peso em KG: "))
    altura = float(input("Digite a altura em METROS: "))
    imc = peso / (altura * 2)
    break

    if imc > 39.0:
        obesidade_3 += 1
    elif imc > 34.9:
        obesidade_2 += 1
    elif imc > 29.9:
        obesidade_1 += 1
    elif imc > 24.9:
        sobrepeso += 1
    elif imc > 18.5:
        peso_normal += 1
    else:
        abaixo_peso += 1

print("\nVeja a lista de classificação dos IMCS\n")
print(f"Abaixo do peso: {abaixo_peso} pessoas")
print(f"Peso normal: {peso_normal} pessoas")
print(f"Sobrepeso: {sobrepeso} pessoas")
print(f"Obesidade Grau I: {obesidade_1} pessoas")
print(f"Obesidade Grau II: {obesidade_2} pessoas")
print(f"Obesidade Grau III: {obesidade_3} pessoas")
