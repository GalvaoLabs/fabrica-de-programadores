#o quer são variáveis

#lista = ["Vanessao", "Carlota", "Enzo do pix"]

#x = input("Digite seu nome: \n\n")

#if x in lista:
#    print("Esse nome esta dentro da lista")

#else:
#    print("Esse nome não está na lista")

#-----------------------------------------------------------------------#

#Verificação se o usuario ele pode ou não votar, o voto é a patir dos 16 anos

#lista = ["Enzo","Pedro","Mariazinha","Rita"]
#idade = [21,18,15,70]

#nome_digitado = input("Digite o nome do Eleitor: \n\n")
#idade_digitada = int(input("Digite a idade do Eleitor:\n\n"))

#index_lista = lista.index(nome_digitado)
#index_idade = idade.index(idade_digitada)

#if index_lista == index_idade:
    #if idade_digitada >=16: 
        #print("Você pode votar!!!")
    #else:
        #print("Você não pode votar")

#else:
    #("Eleitor ou idade inválidos...")

#-----------------------------------------------------------------------------------#

#minha_garagem = ["BMW", "Mercedes-Bens", "Audi", "Aston Martin"]
#preço = [35000, 40000, 20000, 80000]

estoque = ["Chevy", "Fiat", "Peugeot", "Wolkswagen", "Lexus", "Ferrari"]
preco_loja = [1000, 500, 1.99, 20000, 60000, 90000]

loja_barato = [] #abaixo de 20 mil
loja_caro = [] #acima de 20 mil

i = 0
for preco in preco_loja:
    if preco_loja > 25000:
        loja_caro.append(estoque[i])

    else:
        loja_barato.append(estoque[i])

    i = i + 1

print(loja_caro)

print(loja_barato)