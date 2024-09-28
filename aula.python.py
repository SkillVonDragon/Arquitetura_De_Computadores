lista=[0]*10
soma=0
for i in range(10):
    lista[i]=int(input(f"Digite o {i+1} elemento: "))
    soma+=lista[i]
print("números digitados são: ")
print(lista)
print(f"O somatório é {soma}")
