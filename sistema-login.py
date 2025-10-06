import time

# Definindo a senha fixa
senha_correta = "1234"

# Número máximo de tentativas
max_tentativas = 3

# Tempo total para tentar o login (em segundos)
tempo_maximo = 30

# Marca o tempo de início
inicio = time.time()

# Número de tentativas restantes
tentativas_restantes = max_tentativas

while tentativas_restantes > 0:
    # Verifica o tempo restante
    tempo_decorrido = time.time() - inicio
    tempo_restante = tempo_maximo - tempo_decorrido

    if tempo_restante <= 0:
        print("Tempo expirado! Você excedeu o limite de tempo.")
        break
    
    print(f"Você tem {tentativas_restantes} tentativa(s) restante(s).")
    print(f"Tempo restante: {tempo_restante:.2f} segundos.")
    
    # Solicita a senha ao usuário
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Login bem-sucedido! Acesso concedido.")
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print("Senha incorreta. Tente novamente.")
        else:
            print("Número máximo de tentativas atingido. Acesso negado.")
