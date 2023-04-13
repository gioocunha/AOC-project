# bench_refcode.py
#
# Código de referência para trabalho de AOC sobre benchmarks
# 
# Criação: 12 de setembro de 2022
# Atualização:
#
# Uso: na linha de comando, digitar 'python3 bench_refcode.py'
# 
# Obs.: O Python 3 deve estar instalado.

# importação do módulo time
import time

tempos = [] # inicia lista vazia

for repete in range(3):
    inicio = time.time() # marca o início da contagem de tempo
    
    #--- Seu programa de benchmark inicia aqui ---#
    def f(x):
        m, n = 0, 1
        a = 0
        while a < x:
            m, n = n, m+n
            n += 1
        return m
    
    for i in range(0, 10000000):
       f(0)
    #--- Seu programa de bechmark encerra aqui ---#
    
    fim = time.time() # marca o final da contagem de tempo

    tempos.append(fim-inicio)

print('Tempos de execução em segundos: ', tempos)
