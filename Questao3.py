from collections import deque

def verificar_carregador(sequencia):
    fila = deque(sequencia)
    posicao = 1
    
    while fila:
        bala = fila.popleft()
        
        if posicao % 4 == 0:
            if bala != 0:
                return False
        
        posicao += 1
    
    return True

def main():
    print("Sistema de Verificação de Carregador (HAMBO)")
    
    entrada = input("Digite a sequência de munições separadas por espaço (use 0 para vazia, ex: 1 2 3 0 5 6 7 0): ")
    sequencia = [int(x) for x in entrada.split()]
    
    print(f"\nVerificando carregador: {sequencia}")
    
    if verificar_carregador(sequencia):
        print("RESULTADO: Soldado conseguiu salvar o mundo")
    else:
        print("RESULTADO: Morreu")

if __name__ == "__main__":
    main()
