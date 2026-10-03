# Escreva um programa que pede ao usuário dois números e exiba no final a soma deles:
# OUTPUT ESPERADO:

# Digite um número: 10
# Digite outro número: 30
# A soma entre 10 e 30 é: 40


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print("------- Calculadora ------")
number1 = int(input("Digite um número: \n"))
number2 = int(input("Digite outro número: \n"))

soma = (number1 + number2)

print(f"A soma entre {number1} e {number2} é: {soma}")