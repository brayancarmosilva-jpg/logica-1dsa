def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        # Linhas
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        # Colunas
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def jogar():
    # Inicialização do tabuleiro 3x3
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    turno = 0  # Começa com o jogador X

    while True:
        imprimir_tabuleiro(tabuleiro)
        jogador_atual = jogadores[turno % 2]
        print(f"Jogador {jogador_atual}, é a sua vez!")

        # Captura a jogada
        while True:
            try:
                linha = int(input("Escolha a linha (0, 1, 2): "))
                coluna = int(input("Escolha a coluna (0, 1, 2): "))
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_atual
                    break
                else:
                    print("Essa posição já está ocupada. Tente novamente.")
            except (ValueError, IndexError):
                print("Entrada inválida. Tente novamente com valores entre 0 e 2.")

        # Verificar vitória
        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
            break

        # Verificar empate
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate! O jogo acabou.")
            break

        # Alternar para o próximo jogador
        turno += 1

# Iniciar o jogo
jogar()
