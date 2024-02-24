import heapq

class Cidade:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
        self.vizinhos = {}

    def adicionar_vizinho(self, vizinho, distancia):
        self.vizinhos[vizinho] = distancia

def heuristic(cidade, objetivo):
    # Distância euclidiana entre as cidades
    return ((cidade.x - objetivo.x) ** 2 + (cidade.y - objetivo.y) ** 2) ** 0.5

def a_estrela(inicio, objetivo):
    fronteira = [(0, inicio)]  # (f, cidade)
    veio_de = {}
    custo_g = {inicio: 0}  # Inicializa o custo_g apenas com a cidade de início
    while fronteira:
        _, atual = heapq.heappop(fronteira)
        if atual == objetivo:
            caminho = []
            while atual in veio_de:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho
        for vizinho, distancia in atual.vizinhos.items():
            custo_g_tentativo = custo_g[atual] + distancia
            if vizinho not in custo_g or custo_g_tentativo < custo_g[vizinho]:
                veio_de[vizinho] = atual
                custo_g[vizinho] = custo_g_tentativo
                f_score = custo_g_tentativo + heuristic(vizinho, objetivo)
                heapq.heappush(fronteira, (f_score, vizinho))
    return None

# Criando as cidades
Brasilia = Cidade("Brasília", 0, 0)
Goiania = Cidade("Goiânia", 1, 1)
BeloHorizonte = Cidade("Belo Horizonte", 2, 0)
SaoPaulo = Cidade("São Paulo", 1, 2)

# Adicionando vizinhos e distâncias
Brasilia.adicionar_vizinho(Goiania, 1)
Brasilia.adicionar_vizinho(BeloHorizonte, 2)
Goiania.adicionar_vizinho(Brasilia, 1)
Goiania.adicionar_vizinho(SaoPaulo, 1)
BeloHorizonte.adicionar_vizinho(Brasilia, 2)
BeloHorizonte.adicionar_vizinho(SaoPaulo, 1)
SaoPaulo.adicionar_vizinho(Goiania, 1)
SaoPaulo.adicionar_vizinho(BeloHorizonte, 1)

# Executando A* e exibindo o caminho encontrado
caminho = a_estrela(Brasilia, SaoPaulo)
if caminho:
    print("Caminho encontrado:")
    for cidade in caminho:
        print(cidade.nome)
else:
    print("Não foi possível encontrar um caminho.")

