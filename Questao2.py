def pile_shuffle(cartas, k):
    # Distribuição em k pilhas (LIFO)
    pilhas = [[] for _ in range(k)]
    for i, carta in enumerate(cartas):
        pilhas[i % k].append(carta)
    
    # Recolhimento (LIFO - esvaziando as pilhas do topo)
    nova_sequencia = []
    for i in range(k):
        while pilhas[i]:
            nova_sequencia.append(pilhas[i].pop())
            
    return nova_sequencia

def main():
    print("Sistema de Embaralhamento (Pile Shuffle)")
    
    entrada = input("Digite a sequência de cartas separadas por espaço (ex: 1 2 3 4 5 6 7 8 9): ")
    cartas = [int(x) for x in entrada.split()]
    
    k = int(input("Digite o valor de k (número de pilhas na 1ª iteração): "))
    m = int(input("Digite o valor de m (número de pilhas na 2ª iteração - deve ser primo em relação a k): "))
    
    # Primeira Iteração
    passo1 = pile_shuffle(cartas, k)
    
    # Segunda Iteração
    resultado = pile_shuffle(passo1, m)
    print(f"Resultado final (após m={m}): {resultado}")

if __name__ == "__main__":
    main()
