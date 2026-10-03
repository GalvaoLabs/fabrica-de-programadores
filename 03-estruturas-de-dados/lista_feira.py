print("------Lista da Feira------")

lista = ["Abacaxi"]

opçao = input("Digite uma fruta que você queira procurar: \n\n")

if opçao in lista:
    print(f"A fruta {opçao} está na lista...")

else:
    nova_fruta = input(f"A fruta {opçao} não está na lista!!!\n\nVocê quer adicionar uma nova fruta a lista ? (sim/não)").lower

    if nova_fruta == "sim":
        nova_lista = input("Digite a fruta você quer adicionar: \n\n")
        lista.append(nova_lista)

    else:
        print(f"A lista de frutas da feira é: {lista}")