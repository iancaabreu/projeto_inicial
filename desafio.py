Constante_bonus = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome:  ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu sálario:  "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus_usuario = float(input("Digite o seu BÔnus:  "))

# 4) Calcule o valor do bônus final

valor_do_bonus = Constante_bonus + salario_usuario * bonus_usuario


# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e valor do bônus
print(f"O usuário {nome_usuario} posusi o bonus de {valor_do_bonus}  ")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?