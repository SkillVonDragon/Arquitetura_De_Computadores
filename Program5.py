numero = 1
soma = 0
media = 0
cont = 0

while numero != 0:
    numero = int(input("Entre com um valor, caso digite zero o programa irá parar: "))
    soma += numero
    print(f"O somatorio dos números é {soma}")

    if soma != 0:
        cont+=1
        media = soma/cont;
        print(f"A média dos números é {media:.2f}")
