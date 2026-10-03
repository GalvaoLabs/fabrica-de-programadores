arquivo = open("arquivo.texto", "a", encoding="utf-8")

nome = input("\n\nDigite o nome do aluno programador:\n\n")

arquivo.write(f"\n\nNome do programador: {nome}\n\n")
arquivo.write("-"*60)
arquivo.close()