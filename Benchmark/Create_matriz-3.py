# bench_refcode.py
#
# Código de referência para trabalho de AOC sobre benchmarks
#
# Criação: 13 de abril de 2023
# Atualização:
#
# Uso: na linha de comando, digitar 'python3 bench_refcode.py'
#
# Obs.: O Python 3 deve estar instalado.

# importação do módulo time
import time
import numpy as np

tempos = []  # inicia lista vazia

for repete in range(3):
    inicio = time.time()  # marca o início da contagem de tempo


    # --- Seu programa de benchmark inicia aqui ---#

    def f(x, y):
        r = np.full((x, y), x + y)
        return r


    for i in range(0, 200):
        for k in range(0, 200):
            x = k + i
            y = k + 2 * i
            f(x, y)

    # --- Seu programa de bechmark encerra aqui ---#

    fim = time.time()  # marca o final da contagem de tempo

    tempos.append(fim - inicio)

print('Tempos de execução em segundos: ', tempos)
