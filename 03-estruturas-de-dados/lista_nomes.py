x = []

print("------Bem-vindo(a) a chamada------\n\n\n")

nomes = input("Deseja adicionar um(a) aluno(a) ?\n\n").lower()

if nomes == "sim":
    a = input("Digite o nome que deseja adicionar:\n\n")
    x.append(a)
    b = input("Digite o nome que deseja adicionar:\n\n")
    x.append(b)
    c = input("Digite o nome que deseja adicionar:\n\n")
    x.append(c)
    d = input("Digite o nome que deseja adicionar:\n\n")
    x.append(d)
    e = input("Digite o nome que deseja adicionar:\n\n")
    x.append(e)
    f = input("Digite o nome que deseja adicionar:\n\n")
    x.append(f)
    g = input("Digite o nome que deseja adicionar:\n\n")
    x.append(g)
    h = input("Digite o nome que deseja adicionar:\n\n")
    x.append(h)
    i = input("Digite o nome que deseja adicionar:\n\n")
    x.append(i)
    j = input("Digite o nome que deseja adicionar:\n\n")
    x.append(j)
    print(f"As pessoas que estão na chamada: {x}")

else: 
    print(f"A lista de alunos é: {x}")
    print("Até logo...")