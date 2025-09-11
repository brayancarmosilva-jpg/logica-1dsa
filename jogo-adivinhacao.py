import random

numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"Acertou em {tentativas} tentativa(s)!")
        break
    else:
        print("Errou! Tente novamente.")
