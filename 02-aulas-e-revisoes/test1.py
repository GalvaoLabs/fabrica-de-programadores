contador = 0
while contador <15:
    contador = contador +1
    arquivo = open("arquivo.text", "a", encoding="utf-8")
    nome = input("Digite uma cidade: ")
    arquivo.write("-"*60)
    arquivo.write("\n\nCidades Bonitas\n\n")
    arquivo.write("-"*60)
    arquivo.write(f"\n\nCidade: {nome}\n\n")

arquivo.close()

print("Lista das cidades bonitas gerada com sucesso")