class No:
    def __init__(self, tipo, id_vagao):
        self.tipo = tipo # 'Cabine', 'Passageiro', 'Carga', 'Mineral'
        self.id_vagao = id_vagao
        self.esq = None
        self.dir = None

class Trem:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir_final(self, tipo, id_vagao):
        novo = No(tipo, id_vagao)
        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.dir = novo
            novo.esq = self.fim
            self.fim = novo
        self.tamanho += 1

    def imprimir(self):
        aux = self.inicio
        if not aux:
            print("Trem vazio.")
            return
        while aux:
            print(f"[{aux.tipo} {aux.id_vagao}]", end=" <-> " if aux.dir else "")
            aux = aux.dir
        print("")

def conectar_e_organizar(trem1, trem2):
    if trem1.inicio is None: return trem2
    if trem2.inicio is None: return trem1
    

    trem1.fim.dir = trem2.inicio
    trem2.inicio.esq = trem1.fim
    
    nova_lista_inicio = trem1.inicio
    

    cabines = []
    meio = []
    minerais = []
    
    aux = nova_lista_inicio
    while aux:
        proximo = aux.dir
        aux.esq = None
        aux.dir = None
        
        if aux.tipo == '1': # Cabine
            aux.tipo_nome = 'Cabine'
            cabines.append(aux)
        elif aux.tipo == '3': # Mineral
            aux.tipo_nome = 'Mineral'
            minerais.append(aux)
        else: # Passageiro/Carga
            aux.tipo_nome = 'Passageiro/Carga'
            meio.append(aux)
        aux = proximo
        
    cabine_unica = []
    if cabines:
        cabine_unica = [cabines[0]]
            
    todos_vagoes = cabine_unica + meio + minerais
    
    resultado = Trem()
    for vagao in todos_vagoes:
        vagao.tipo = vagao.tipo_nome
        if resultado.inicio is None:
            resultado.inicio = vagao
            resultado.fim = vagao
        else:
            resultado.fim.dir = vagao
            vagao.esq = resultado.fim
            resultado.fim = vagao
        resultado.tamanho += 1
        
    return resultado

def ler_trem(nome_trem):
    trem = Trem()
    print(f"\n--- Configurando {nome_trem} ---")
    n = int(input(f"Quantos vagões o {nome_trem} possui? "))
    for i in range(n):
        print(f"Vagão {i+1}:")
        id_v = input("  Identificador (ex: A, B, 101): ")
        print("  Tipo: 1-Cabine | 2-Passageiro/Carga | 3-Mineral")
        tipo = input("  Escolha o tipo: ")
        trem.inserir_final(tipo, id_v)
    return trem

def main():
    print("Sistema de alocação de vagões de trem")
    t1 = ler_trem("Trem 1")
    t2 = ler_trem("Trem 2")
    
    print("\nTrem 1 original:")
    t1.imprimir()
    print("Trem 2 original:")
    t2.imprimir()
    
    trem_final = conectar_e_organizar(t1, t2)
    print("\nNovo trem organizado:")
    trem_final.imprimir()

if __name__ == "__main__":
    main()
