# Esse código será para um controle de usuários no sistema, com base no username e password.
# Só deverá ser logado no sistema o usuário "admin" com senha "123".

print("Login Logoso Firmeza do Sistema da Hora")
username = input("Por favor, insira o nome de usuário: ")
password = input("Por favor, insira a senha: ")

if username == "admin" and password == "123":
    print("Usuário logado!")
else:
    print("Usuário ou senha incorretos. Acesso negado.")