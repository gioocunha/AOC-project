# Código para trabalho de AOC sobre benchmarks usando a biblioteca timeit
# Criação: 13/04/2022

import timeit

# Definir a função que será testada
def exemplo_func():
    soma = 0
    for i in range(600000):
        soma += i
    return soma

# Medir o tempo de execução da função usando a biblioteca timeit
num_execucoes = 10
tempo_execucoes = timeit.repeat("exemplo_func()", setup="from __main__ import exemplo_func", repeat=num_execucoes, number=55)

# Calcular as estatísticas dos tempos de execução
tempo_medio = sum(tempo_execucoes) / num_execucoes
tempo_desvio_padrao = (sum((tempo - tempo_medio) ** 2 for tempo in tempo_execucoes) / num_execucoes) ** 0.5
tempo_minimo = min(tempo_execucoes)
tempo_maximo = max(tempo_execucoes)

# Imprimir os resultados
print("Número de execuções:", num_execucoes)
print("Tempo médio de execução: {:.5f} segundos".format(tempo_medio)) # Resultado adotado como estatística para a tabela do relatório 
print("Desvio padrão: {:.5f} segundos".format(tempo_desvio_padrao))
print("Tempo mínimo: {:.5f} segundos".format(tempo_minimo))
print("Tempo máximo: {:.5f} segundos".format(tempo_maximo))
