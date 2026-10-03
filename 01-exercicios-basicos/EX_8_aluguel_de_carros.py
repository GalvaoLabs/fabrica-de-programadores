# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

km_percorridos = float(input("Quantos quilômetros você percorreu com o carro ?\n"))
dias_alugados = float(input("Por quantos dias você alugou esse carro ?\n"))
preco_km = km_percorridos * 0.15
preco_dias = dias_alugados * 60
soma = preco_km + preco_dias

print(f"Por quantos dias o carro foi alugado: {dias_alugados}\n")
print(f"Quantos km o carro rodou: {km_percorridos}\n")
print(f"Você andou {km_percorridos}km por {dias_alugados} dias, então o preço a pagar é R${soma}.")