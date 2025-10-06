# Lista com nomes fictícios de lojas
lojas = ["Loja Sol", "Loja Lua", "Loja Estrela"]

# Matriz com preços de produtos em cada loja (3 produtos por loja)
precos = [
    [10.99, 12.50, 9.75],     # Preços da Loja Sol
    [8.99, 11.20, 10.00],     # Preços da Loja Lua
    [9.50, 10.75, 12.30]      # Preços da Loja Estrela
]
#Estrutura de loops aninhados
# Loop externo percorre cada loja
for i in range(len(lojas)):
    print(f"{lojas[i]}:")  # Exibe o nome da loja atual

    # Loop interno percorre os preços da loja atual
    for preco in precos[i]:
        print(f"  R$ {preco:.2f}")  # Exibe o preço formatado com duas casas decimais

    print()  # Linha em branco para separar visualmente as lojas
