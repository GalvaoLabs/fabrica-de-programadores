arquivo = open("arquivo.txt", "a", encoding="utf-8")
#w cria um arquivo caso não exista, caso exista, o w substitui este arquivo
#"a" append, adicona ao final. Importante usar \n
nome = input("Digite o nome do(a) aluno(a):\n")
nota = int(input("Digite a nota do aluno(a):\n"))
arquivo.write("-"*20)
arquivo.write(f"\nAluuno: {nome}\n")
arquivo.write(F"\nNota: {nota}\n")
arquivo.write("-"*20)
arquivo.close()