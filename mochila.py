import itertools
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Função de força bruta para mochila binária sem repetição
def knapsack_bruteforce(items, capacity):
    max_value = -1
    n = len(items)
    for r in range(1, n+1):
        for subset in itertools.combinations(items, r):
            total_weight = sum(item[1] for item in subset)
            if total_weight <= capacity:
                total_value = sum(item[0] for item in subset)
                if total_value > max_value:
                    max_value = total_value
    return max_value

# Função de programação dinâmica para mochila binária sem repetição
def knapsack_dynamic(items, capacity):
    n = len(items)
    values = [item[0] for item in items]
    weights = [item[1] for item in items]
    M = np.zeros((n + 1, capacity + 1), dtype=int)

    for j in range(1, n+1):
        for X in range(capacity + 1):
            if weights[j-1] > X:
                M[j][X] = M[j-1][X]
            else:
                use = values[j-1] + M[j-1][X - weights[j-1]]
                not_use = M[j-1][X]
                M[j][X] = max(use, not_use)

    return M[n][capacity]

# Função de programação dinâmica para mochila com repetição
def knapsack_dynamic_repetition(items, capacity):
    n = len(items)
    values = [item[0] for item in items]
    weights = [item[1] for item in items]
    dp = [0] * (capacity + 1)

    for X in range(capacity + 1):
        for j in range(n):
            if weights[j] <= X:
                dp[X] = max(dp[X], dp[X - weights[j]] + values[j])

    return dp[capacity]

def generate_random_items(n):
    return [(random.randint(1, 2*n), random.randint(1, 2*n)) for _ in range(n)]

# Medir tempo de execução e verificar solução ótima
def measure_and_compare(n, m, items_list, capacities):
    bruteforce_times = []
    dynamic_times = []
    dynamic_repetition_times = []
    optimal_values_match = []

    for i in range(m):
        items = items_list[i]
        capacity = capacities[i]

        # Medir tempo e valor ótimo para força bruta
        start_time = time.time()
        bruteforce_value = knapsack_bruteforce(items, capacity)
        bruteforce_time = time.time() - start_time
        bruteforce_times.append(bruteforce_time)

        # Medir tempo e valor ótimo para programação dinâmica sem repetição
        start_time = time.time()
        dynamic_value = knapsack_dynamic(items, capacity)
        dynamic_time = time.time() - start_time
        dynamic_times.append(dynamic_time)

        # Medir tempo e valor ótimo para programação dinâmica com repetição
        start_time = time.time()
        dynamic_repetition_value = knapsack_dynamic_repetition(items, capacity)
        dynamic_repetition_time = time.time() - start_time
        dynamic_repetition_times.append(dynamic_repetition_time)

        # Verificar se os valors ótimos são iguais
        optimal_values_match.append(
            bruteforce_value == dynamic_value == dynamic_repetition_value
        )

        # Tabela
        if i == 0: 
            print("\nTabela de Itens:")
            print("Item\tValor\tPeso")
            for idx, (value, weight) in enumerate(items):
                print(f"{idx+1}\t{value}\t{weight}")
            print(f"Capacidade da Mochila: {capacity}")

    return (
        bruteforce_times,
        dynamic_times,
        dynamic_repetition_times,
        optimal_values_match,
    )

# Plotar gráficos comparativos
def plot_comparative_growth():
    k = 7  
    input_sizes = sorted(random.sample(range(10, 41), k))  
    m = 3  
    bruteforce_avg_times = []
    dynamic_avg_times = []
    dynamic_repetition_avg_times = []

    for n in input_sizes:
        # Gerar m conjuntos de itens e capacidades para o tamanho n
        items_list = [generate_random_items(n) for _ in range(m)]
        capacities = [random.randint(1, 2*n) for _ in range(m)]

        # Medir e comparar tempos
        (
            bruteforce_times,
            dynamic_times,
            dynamic_repetition_times,
            optimal_values_match,
        ) = measure_and_compare(n, m, items_list, capacities)

        # Calcular médias
        bruteforce_avg_times.append(sum(bruteforce_times) / m)
        dynamic_avg_times.append(sum(dynamic_times) / m)
        dynamic_repetition_avg_times.append(sum(dynamic_repetition_times) / m)

        if not all(optimal_values_match):
            print(f"Atenção: Valores ótimos divergem para n = {n}!")

    # Plotar gráfico comparativo
    plt.figure(figsize=(12, 6))
    plt.plot(input_sizes, bruteforce_avg_times, label="Força Bruta", marker='o')
    plt.plot(input_sizes, dynamic_repetition_avg_times, label="Programação Dinâmica (Com Repetição)", marker='s')
    plt.xlabel('Tamanho da Entrada (n)')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Comparação entre Força Bruta e Programação Dinâmica (Com Repetição)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  
    plt.show()

    # Plotar gráfico comparativo
    plt.figure(figsize=(12, 6))
    plt.plot(input_sizes, bruteforce_avg_times, label="Força Bruta", marker='o')
    plt.plot(input_sizes, dynamic_avg_times, label="Programação Dinâmica (Sem Repetição)", marker='s')
    plt.xlabel('Tamanho da Entrada (n)')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Comparação entre Força Bruta e Programação Dinâmica (Sem Repetição)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  
    plt.show()

# Executar a comparação
plot_comparative_growth()