Alunos = int(input("Digite a quantidade de alunos: "))
Aprovado = Recuperacao = Reprovado = 0

for i in range(Alunos):
    Nota1 = float(input(f"Digite a 1º nota do aluno {i+1}: "))
    Nota2 = float(input(f"Digite a 2º nota do aluno {i+1}: "))
    Media = (Nota1 + Nota2)/2
    if Media >= 7.0:
        Aprovado+= 1
    elif Media >= 4.0:
        Recuperacao+=1
    else:
        Reprovado+=1
    
print(f"A quantidade de alunos aprovados é {Aprovado} corresponde a {Aprovado/Alunos*100}%");
print(f"A quantidade de alunos em recuperação é {Recuperacao} corresponde a {Recuperacao/Alunos*100}%");
print(f"A quantidade de alunos em reprovados é {Reprovado} corresponde a {Reprovado/Alunos*100}%");
    
