import time

tempos = []

inicio = time.time()
a1 = 1
r = 3.14159265359
n = 1
for n in range(1,1000000):
    an = a1 + (n - 1) * r

fim = time.time()
tempos.append(fim-inicio)

print('Tempos de execução em segundos: ', tempos)
