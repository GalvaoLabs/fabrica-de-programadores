# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com+
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
email = input("Digite o seu email: ")
senha = int(input("Digite a sua senha: "))

print("| ------------------------------ |\n")
print("| ---------- CADASTRO ---------- |\n")
print("| ------------------------------ |\n")
print(f"Nome: {nome}\n")
print(f"Idade: {idade}\n")
print(f"Email: {email}\n")
print(f"Senha: {senha}\n")
print("| ------------------------------ |\n")
print("| ----- USUÁRIO CADASTRADO ----- |\n")
print(f"| Seja bem vindo(a) {nome}!\n")
print(f"| Email: {email}\n")
print("| ------------------------------ |\n")