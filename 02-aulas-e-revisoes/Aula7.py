lista_de_usuarios = ["Vanessa", "Carla", "Enzo"]
senha_de_usuario = ["Van123", "C4rly", "En_z0"]

nome_digitado = input("Digite o seu nome:\n\n")
senha_digitada = input("Digite sua senha:\n\n")

index_nome = lista_de_usuarios.index(nome_digitado)
index_senha = senha_de_usuario.index(senha_digitada)

if index_nome == index_senha:
    print("Login bem-sucedido")

else:
    print("Usuário ou senha inválidos")