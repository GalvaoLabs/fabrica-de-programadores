# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = input("Qual o nome do produto ? \n")
preco = float(input("Qual o preço do produto ? \n"))
porcentagem = float(input("Qual o valor da porcentagem do desconto ?"))
desconto = preco * (porcentagem/100)

print(f"Produto: {produto}\n")
print(f"Preço: {preco}\n")
print(f"Porcentagem de desconto: {porcentagem}\n")
print(f"O {produto} com {porcentagem}% de desconto, custará {desconto}")